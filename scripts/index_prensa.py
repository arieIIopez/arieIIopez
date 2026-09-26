#!/usr/bin/env python3
"""
Valida el catálogo curado de prensa del perfil de Ariel López.

Fuente de verdad:
    archivo/prensa/prensa.csv

Este script NO descarga Medium, NO modifica el catálogo y NO genera registros.
Su función es impedir regresiones: valida esquema, fechas, URLs, duplicados y
conteos de los años ya cerrados documentalmente.

Los años 2021 y 2022 permanecen pendientes hasta recuperar una fuente completa.
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "archivo" / "prensa" / "prensa.csv"

REQUIRED_FIELDS = {
    "fecha",
    "anio",
    "medio",
    "titulo",
    "enlace",
    "categoria",
    "fuente_blog",
    "estado",
    "nota",
}

EXPECTED_COMPLETE = {
    2026: 88,
    2025: 50,
    2024: 36,
    2023: 30,
    2020: 46,
}

PENDING_YEARS = {2021, 2022}
ALLOWED_CATEGORIES = {"entrevista", "cobertura", "columna_opinion"}
ALLOWED_STATES = {"curado"}


def valid_http_url(value: str) -> bool:
    if not value:
        return True
    p = urlparse(value)
    return p.scheme in {"http", "https"} and bool(p.netloc)


def main() -> int:
    errors: list[str] = []

    if not CSV_PATH.exists():
        print(f"ERROR: no existe {CSV_PATH}", file=sys.stderr)
        return 1

    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fields = set(reader.fieldnames or [])
        missing = REQUIRED_FIELDS - fields
        if missing:
            errors.append(f"Faltan columnas obligatorias: {sorted(missing)}")
        rows = list(reader)

    counts: Counter[int] = Counter()
    seen: set[tuple[str, str, str]] = set()

    for i, row in enumerate(rows, start=2):
        fecha = (row.get("fecha") or "").strip()
        anio_txt = (row.get("anio") or "").strip()
        medio = (row.get("medio") or "").strip()
        titulo = (row.get("titulo") or "").strip()
        enlace = (row.get("enlace") or "").strip()
        categoria = (row.get("categoria") or "").strip()
        fuente = (row.get("fuente_blog") or "").strip()
        estado = (row.get("estado") or "").strip()

        try:
            parsed = date.fromisoformat(fecha)
        except ValueError:
            errors.append(f"Fila {i}: fecha no ISO válida: {fecha!r}")
            continue

        try:
            anio = int(anio_txt)
        except ValueError:
            errors.append(f"Fila {i}: año inválido: {anio_txt!r}")
            continue

        if parsed.year != anio:
            errors.append(
                f"Fila {i}: fecha {fecha} no coincide con año {anio}"
            )

        if not medio:
            errors.append(f"Fila {i}: medio vacío")
        if not titulo:
            errors.append(f"Fila {i}: título vacío")
        if categoria not in ALLOWED_CATEGORIES:
            errors.append(
                f"Fila {i}: categoría no permitida: {categoria!r}"
            )
        if estado not in ALLOWED_STATES:
            errors.append(f"Fila {i}: estado no permitido: {estado!r}")
        if not valid_http_url(enlace):
            errors.append(f"Fila {i}: enlace inválido: {enlace!r}")
        if not valid_http_url(fuente):
            errors.append(f"Fila {i}: fuente_blog inválida: {fuente!r}")

        key = (fecha, medio.casefold(), titulo.casefold())
        if key in seen:
            errors.append(
                f"Fila {i}: duplicado exacto fecha+medio+título: {key}"
            )
        seen.add(key)
        counts[anio] += 1

    for year, expected in EXPECTED_COMPLETE.items():
        actual = counts.get(year, 0)
        if actual != expected:
            errors.append(
                f"{year}: {actual} registros; se esperaban {expected}"
            )

    for year in PENDING_YEARS:
        if counts.get(year, 0):
            errors.append(
                f"{year}: contiene {counts[year]} registros aunque el año "
                "sigue marcado como pendiente; revisar antes de incorporarlos."
            )

    expected_total = sum(EXPECTED_COMPLETE.values())
    if len(rows) != expected_total:
        errors.append(
            f"Total: {len(rows)} registros; se esperaban {expected_total}"
        )

    print("Cobertura validada:")
    for year in sorted(EXPECTED_COMPLETE, reverse=True):
        print(f"  {year}: {counts.get(year, 0)} / {EXPECTED_COMPLETE[year]}")
    print("  2022: pendiente")
    print("  2021: pendiente")
    print(f"Total curado: {len(rows)}")

    if errors:
        print("\nERRORES:", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        return 1

    print("\nOK: catálogo de prensa consistente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
