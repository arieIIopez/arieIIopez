#!/usr/bin/env python3
"""
Valida el catálogo curado de columnas de opinión de Ariel López.

Fuente de verdad:
    archivo/columnas/columnas.csv

No descarga ni modifica fuentes externas. Comprueba integridad estructural,
fechas, enlaces, tipos, duplicados y consistencia básica del catálogo.
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "archivo" / "columnas" / "columnas.csv"

FIELDS = {
    "fecha", "precision_fecha", "anio", "medio", "titulo", "enlace",
    "tipo", "tema", "coautores", "fuente_indice", "estado", "nota"
}
PRECISION = {"día", "mes", "año"}
TIPOS = {"columna", "carta_opinion", "newsletter_columna"}
ESTADOS = {"verificado"}


def valid_url(value: str) -> bool:
    p = urlparse(value)
    return p.scheme in {"http", "https"} and bool(p.netloc)


def valid_date(value: str, precision: str) -> bool:
    try:
        if precision == "día":
            date.fromisoformat(value)
            return len(value) == 10
        if precision == "mes":
            if len(value) != 7:
                return False
            y, m = value.split("-")
            return len(y) == 4 and 1 <= int(m) <= 12
        if precision == "año":
            return len(value) == 4 and value.isdigit()
    except (ValueError, TypeError):
        return False
    return False


def main() -> int:
    errors = []

    if not CSV_PATH.exists():
        print(f"ERROR: no existe {CSV_PATH}", file=sys.stderr)
        return 1

    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        missing = FIELDS - set(reader.fieldnames or [])
        if missing:
            errors.append(f"Faltan columnas: {sorted(missing)}")
        rows = list(reader)

    seen = set()
    counts_year = Counter()
    counts_outlet = Counter()

    for n, row in enumerate(rows, start=2):
        fecha = (row.get("fecha") or "").strip()
        precision = (row.get("precision_fecha") or "").strip()
        anio = (row.get("anio") or "").strip()
        medio = (row.get("medio") or "").strip()
        titulo = (row.get("titulo") or "").strip()
        enlace = (row.get("enlace") or "").strip()
        tipo = (row.get("tipo") or "").strip()
        tema = (row.get("tema") or "").strip()
        fuente = (row.get("fuente_indice") or "").strip()
        estado = (row.get("estado") or "").strip()

        if precision not in PRECISION:
            errors.append(f"Fila {n}: precision_fecha inválida: {precision!r}")
        elif not valid_date(fecha, precision):
            errors.append(f"Fila {n}: fecha {fecha!r} incompatible con {precision!r}")

        try:
            year = int(anio)
        except ValueError:
            errors.append(f"Fila {n}: año inválido: {anio!r}")
            continue

        if not fecha.startswith(str(year)):
            errors.append(f"Fila {n}: fecha {fecha!r} no coincide con año {year}")
        if not medio:
            errors.append(f"Fila {n}: medio vacío")
        if not titulo:
            errors.append(f"Fila {n}: título vacío")
        if not tema:
            errors.append(f"Fila {n}: tema vacío")
        if tipo not in TIPOS:
            errors.append(f"Fila {n}: tipo inválido: {tipo!r}")
        if estado not in ESTADOS:
            errors.append(f"Fila {n}: estado inválido: {estado!r}")
        if not valid_url(enlace):
            errors.append(f"Fila {n}: enlace inválido: {enlace!r}")
        if not valid_url(fuente):
            errors.append(f"Fila {n}: fuente_indice inválida: {fuente!r}")

        key = (fecha, medio.casefold(), titulo.casefold())
        if key in seen:
            errors.append(f"Fila {n}: duplicado exacto: {key}")
        seen.add(key)

        counts_year[year] += 1
        counts_outlet[medio] += 1

    print(f"Registros: {len(rows)}")
    print("Por año:")
    for year in sorted(counts_year, reverse=True):
        print(f"  {year}: {counts_year[year]}")
    print("Por medio:")
    for outlet, count in counts_outlet.most_common():
        print(f"  {outlet}: {count}")

    if errors:
        print("\nERRORES:", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        return 1

    print("\nOK: catálogo de columnas consistente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
