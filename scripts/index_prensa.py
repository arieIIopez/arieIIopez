#!/usr/bin/env python3
"""
Valida el catálogo de prensa de Ariel López.

Estados:
- curado: aparición confirmada en el índice anual del blog.
- reconstruido: aparición recuperada para un año cuyo índice aún no está completo.
- hallazgo_externo: aparición verificada que no figura en el índice anual del blog.
"""
from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "archivo" / "prensa" / "prensa.csv"

REQUIRED_FIELDS = {
    "fecha","anio","medio","titulo","enlace","categoria",
    "fuente_blog","estado","nota",
}
EXPECTED_CURATED = {2026:88, 2025:50, 2024:36, 2023:30, 2022:24, 2021:14, 2020:46}
RECONSTRUCTED_MINIMUM = {}
EXTERNAL_MINIMUM = {2022:6, 2021:5}
ALLOWED_CATEGORIES = {"entrevista","cobertura","columna_opinion"}
ALLOWED_STATES = {"curado","reconstruido","hallazgo_externo"}

def valid_http_url(value: str) -> bool:
    if not value:
        return True
    p=urlparse(value)
    return p.scheme in {"http","https"} and bool(p.netloc)

def main() -> int:
    errors=[]
    if not CSV_PATH.exists():
        print(f"ERROR: no existe {CSV_PATH}",file=sys.stderr)
        return 1

    with CSV_PATH.open(newline="",encoding="utf-8") as fh:
        reader=csv.DictReader(fh)
        missing=REQUIRED_FIELDS-set(reader.fieldnames or [])
        if missing:
            errors.append(f"Faltan columnas obligatorias: {sorted(missing)}")
        rows=list(reader)

    total_by_year=Counter()
    state_counts=defaultdict(Counter)
    seen=set()

    for i,row in enumerate(rows,start=2):
        fecha=(row.get("fecha") or "").strip()
        anio_txt=(row.get("anio") or "").strip()
        medio=(row.get("medio") or "").strip()
        titulo=(row.get("titulo") or "").strip()
        enlace=(row.get("enlace") or "").strip()
        categoria=(row.get("categoria") or "").strip()
        fuente=(row.get("fuente_blog") or "").strip()
        estado=(row.get("estado") or "").strip()

        try:
            parsed=date.fromisoformat(fecha)
        except ValueError:
            errors.append(f"Fila {i}: fecha no ISO válida: {fecha!r}")
            continue
        try:
            anio=int(anio_txt)
        except ValueError:
            errors.append(f"Fila {i}: año inválido: {anio_txt!r}")
            continue

        if parsed.year!=anio:
            errors.append(f"Fila {i}: fecha {fecha} no coincide con año {anio}")
        if not medio:
            errors.append(f"Fila {i}: medio vacío")
        if not titulo:
            errors.append(f"Fila {i}: título vacío")
        if categoria not in ALLOWED_CATEGORIES:
            errors.append(f"Fila {i}: categoría no permitida: {categoria!r}")
        if estado not in ALLOWED_STATES:
            errors.append(f"Fila {i}: estado no permitido: {estado!r}")
        if not valid_http_url(enlace):
            errors.append(f"Fila {i}: enlace inválido: {enlace!r}")
        if not valid_http_url(fuente):
            errors.append(f"Fila {i}: fuente_blog inválida: {fuente!r}")

        key=(fecha,medio.casefold(),titulo.casefold())
        if key in seen:
            errors.append(f"Fila {i}: duplicado exacto fecha+medio+título: {key}")
        seen.add(key)
        total_by_year[anio]+=1
        state_counts[anio][estado]+=1

    for year,expected in EXPECTED_CURATED.items():
        actual=state_counts[year]["curado"]
        if actual!=expected:
            errors.append(f"{year}: {actual} registros curados; se esperaban {expected}")

    for year,minimum in RECONSTRUCTED_MINIMUM.items():
        actual=state_counts[year]["reconstruido"]
        if actual<minimum:
            errors.append(f"{year}: {actual} reconstruidos; mínimo esperado {minimum}")

    for year,minimum in EXTERNAL_MINIMUM.items():
        actual=state_counts[year]["hallazgo_externo"]
        if actual<minimum:
            errors.append(f"{year}: {actual} hallazgos externos; mínimo esperado {minimum}")

    minimum_total=sum(EXPECTED_CURATED.values())+sum(RECONSTRUCTED_MINIMUM.values())+sum(EXTERNAL_MINIMUM.values())
    if len(rows)<minimum_total:
        errors.append(f"Total: {len(rows)} registros; mínimo esperado {minimum_total}")

    print("Cobertura validada:")
    for year in sorted(total_by_year,reverse=True):
        c=state_counts[year]
        print(f"  {year}: total={total_by_year[year]}, curado={c['curado']}, reconstruido={c['reconstruido']}, externo={c['hallazgo_externo']}")
    print(f"Total registrado: {len(rows)}")

    if errors:
        print("\nERRORES:",file=sys.stderr)
        for err in errors:
            print(f"- {err}",file=sys.stderr)
        return 1

    print("\nOK: catálogo de prensa consistente.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
