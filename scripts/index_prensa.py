#!/usr/bin/env python3
"""
Genera el archivo histórico de apariciones en prensa de Ariel López a partir de
las páginas anuales publicadas en blog.ariellopez.cl.

Medium bloquea algunas lecturas automatizadas directas; por eso se usa Jina
Reader como capa de lectura pública y reproducible. Jina renderiza la URL y
devuelve Markdown, sin modificar la fuente original.

Salida:
  archivo/prensa/index.md
  archivo/prensa/prensa.csv
  archivo/prensa/estado.json

El README del perfil NO se modifica.
"""
from __future__ import annotations

import csv
import html
import json
import re
import sys
import time
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "archivo" / "prensa"
OUT.mkdir(parents=True, exist_ok=True)

PAGES = {
    2026: "https://blog.ariellopez.cl/en-la-prensa-2026-ab565e1372b4",
    2025: "https://blog.ariellopez.cl/en-la-prensa-2025-e0bdc343bba6",
    2024: "https://blog.ariellopez.cl/en-la-prensa-2024-ee71aa3b0fdf",
    2023: "https://blog.ariellopez.cl/en-la-prensa-e39e770d85d2",
    2022: "https://blog.ariellopez.cl/en-la-prensa-2022-aebe4412f9d5",
    2021: "https://blog.ariellopez.cl/en-la-prensa-2021-7192a2541e1e",
    2020: "https://blog.ariellopez.cl/en-la-prensa-2020-e95ebbc5518c",
}

# Conteos conocidos a partir de las propias páginas. Los restantes se detectan
# automáticamente desde la frase "N Recortes de prensa...".
EXPECTED_KNOWN = {2026: 88, 2024: 36, 2023: 30, 2020: 46}

MONTHS = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "setiembre": 9, "octubre": 10,
    "noviembre": 11, "diciembre": 12,
}

MEDIA_BY_DOMAIN = {
    "latercera.com": "La Tercera",
    "lun.com": "LUN",
    "biobiochile.cl": "Radio Bío Bío",
    "t13.cl": "Canal 13",
    "youtube.com": "YouTube",
    "youtu.be": "YouTube",
    "cnnchile.com": "CNN Chile",
    "theclinic.cl": "The Clinic",
    "eldinamo.cl": "El Dínamo",
    "contrapoderchile.cl": "Contrapoder",
    "radio13c.cl": "Radio T13C",
    "adnradio.cl": "Radio ADN",
    "doble-espacio.uchile.cl": "Doble Espacio",
    "diariousach.cl": "Diario USACH",
    "eldesconcierto.cl": "El Desconcierto",
    "fastcheck.cl": "Fast Check",
    "legacy.fastcheck.cl": "Fast Check",
    "revistapedalea.com": "Revista Pedalea",
    "latamobility.com": "Latamobility",
    "elmostrador.cl": "El Mostrador",
    "mercuriovalpo.cl": "El Mercurio de Valparaíso",
    "digital.elmercurio.com": "El Mercurio",
    "elmercurio.com": "El Mercurio",
    "tvn.cl": "TVN",
    "chvnoticias.cl": "Chilevisión",
    "chilevision.cl": "Chilevisión",
    "meganoticias.cl": "Meganoticias",
    "mega.cl": "Mega",
    "emol.com": "Emol",
    "cooperativa.cl": "Cooperativa",
    "robotlabot.substack.com": "LaBot",
    "institutoferroviario.cl": "Instituto Ferroviario",
}

MEDIA_ALIASES = [
    "Chilevisión", "Chilevision", "Canal 13", "Teletrece", "T13", "TVN",
    "Canal 24 Horas", "Canal 24 horas", "Meganoticias", "Megavisión", "Mega",
    "La Tercera", "LUN", "El Mercurio", "El Mercurio de Valparaíso",
    "Radio Bío Bío", "Radio Biobío", "Radio Biobio", "Biobío", "Biobio",
    "Radio ADN", "ADN Radio", "Radio 13C", "Radio T13C", "Tele13 Radio",
    "Súbela Radio", "CNN Chile", "CNN", "The Clinic", "El Dínamo",
    "El Dinamo", "El Desconcierto", "Contrapoder", "Diario Usach",
    "Diario USACH", "Doble Espacio", "FastCheck", "Fast Check",
    "Revista Pedalea", "Latamobility", "Experiencia Tech", "LaBot",
    "El Mostrador", "Turno",
]

SKIP_LINK_DOMAINS = {
    "blog.ariellopez.cl", "ariellopez.cl", "medium.com",
    "miro.medium.com", "x.com", "twitter.com", "bcn.cl",
    "patents.google.com", "archivos.lascondes.cl", "seia.sea.gob.cl",
    "avo.cl",
}

STOP_HEADINGS = (
    "get ariel", "written by", "more from", "recommended from",
    "no responses", "responses", "about ariel",
)

@dataclass
class Entry:
    fecha: str
    anio: int
    medio: str
    titulo: str
    enlace: str
    tipo_enlace: str
    fuente_blog: str
    fecha_texto: str
    estado: str = "documentado"


def clean_text(s: str) -> str:
    s = html.unescape(s or "")
    s = re.sub(r"\[(.*?)\]\([^)]*\)", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def unwrap_url(url: str) -> str:
    if not url:
        return ""
    url = html.unescape(url).strip()
    p = urlparse(url)
    if p.netloc.endswith("medium.com") and p.path.startswith("/r/"):
        q = parse_qs(p.query)
        if q.get("url"):
            return unquote(q["url"][0])
    return url


def domain(url: str) -> str:
    try:
        return urlparse(url).netloc.lower().removeprefix("www.")
    except Exception:
        return ""


def fetch_markdown(url: str) -> str:
    reader = "https://r.jina.ai/" + url
    headers = {
        "User-Agent": "arieIIopez-profile-press-index/1.0",
        "Accept": "text/plain,text/markdown;q=0.9,*/*;q=0.1",
    }
    r = requests.get(reader, headers=headers, timeout=75)
    r.raise_for_status()
    text = r.text
    if len(text) < 500:
        raise RuntimeError(f"Jina Reader devolvió contenido demasiado corto ({len(text)} caracteres)")
    return text


def parse_links(block: str) -> list[tuple[str, str]]:
    out = []
    # Markdown inline links. Se toleran etiquetas con saltos simples.
    for m in re.finditer(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", block, re.S):
        out.append((clean_text(m.group(1)), unwrap_url(m.group(2))))
    # URLs sueltas (útil para algunos videos).
    for m in re.finditer(r"(?<!\()\bhttps?://[^\s<>)\]]+", block):
        u = unwrap_url(m.group(0).rstrip(".,;"))
        if u and not any(x[1] == u for x in out):
            out.append(("", u))
    return out


def parse_date(text: str, year: int):
    low = clean_text(text).lower()
    m = re.search(
        r"\b(\d{1,2})\s+de\s+"
        r"(enero|febrero|marzo|abril|mayo|junio|julio|agosto|"
        r"septiembre|setiembre|octubre|noviembre|diciembre)\b",
        low,
    )
    if m:
        d = int(m.group(1))
        mo = MONTHS[m.group(2)]
        return f"{year:04d}-{mo:02d}-{d:02d}", m.group(0)

    m = re.search(r"\b(\d{1,2})[./-](\d{1,2})[./-](\d{2,4})\b", low)
    if m:
        d, mo = int(m.group(1)), int(m.group(2))
        return f"{year:04d}-{mo:02d}-{d:02d}", m.group(0)
    return f"{year:04d}", ""


def canonical_media(name: str) -> str:
    n = clean_text(name)
    mapping = {
        "Chilevision": "Chilevisión",
        "Teletrece": "Canal 13",
        "T13": "Canal 13",
        "Canal 24 horas": "TVN / 24 Horas",
        "Canal 24 Horas": "TVN / 24 Horas",
        "Megavisión": "Mega",
        "Biobío": "Radio Bío Bío",
        "Biobio": "Radio Bío Bío",
        "Radio Biobío": "Radio Bío Bío",
        "Radio Biobio": "Radio Bío Bío",
        "ADN Radio": "Radio ADN",
        "Radio 13C": "Radio T13C",
        "El Dinamo": "El Dínamo",
        "FastCheck": "Fast Check",
    }
    return mapping.get(n, n)


def infer_media(block: str, links: list[tuple[str, str]]) -> str:
    text = clean_text(block)

    # 1) Pie explícito del tipo "Canal 13 | 20.09.2026".
    for line in block.splitlines():
        line = clean_text(line)
        if "|" in line and len(line) < 120:
            left = clean_text(line.split("|", 1)[0])
            if 2 <= len(left) <= 55 and not left.lower().startswith(("fuente", "pág", "pagina")):
                return canonical_media(left)

    # 2) Nombre de medio mencionado en el texto.
    for alias in MEDIA_ALIASES:
        if re.search(rf"(?<!\w){re.escape(alias)}(?!\w)", text, re.I):
            return canonical_media(alias)

    # 3) Dominio periodístico reconocido.
    for _, u in links:
        d = domain(u)
        if d in MEDIA_BY_DOMAIN:
            return MEDIA_BY_DOMAIN[d]

    return "Medio no identificado"


def choose_original_link(links: list[tuple[str, str]]) -> tuple[str, str]:
    candidates = []
    for label, u in links:
        d = domain(u)
        if not d or d in SKIP_LINK_DOMAINS:
            continue
        if u.startswith(("mailto:", "javascript:")):
            continue
        candidates.append((label, u, d))

    for _, u, d in candidates:
        if d in {"youtube.com", "youtu.be"}:
            return u, "youtube"

    for _, u, d in candidates:
        if d in MEDIA_BY_DOMAIN:
            return u, "original"

    if candidates:
        return candidates[0][1], "original"
    return "", "sin_url_documentada"


def detect_expected(md: str, year: int):
    # Busca cerca del título de la página; evita números de otros años.
    marker = re.search(rf"(?im)^#\s+En la prensa {year}\s*$", md)
    sample = md[marker.end():marker.end()+1500] if marker else md[:2500]
    m = re.search(r"\b(\d{1,3})\s+Recortes de prensa", sample, re.I)
    if m:
        return int(m.group(1))
    return EXPECTED_KNOWN.get(year)


def extract_year(year: int, url: str):
    md = fetch_markdown(url)
    marker = re.search(rf"(?im)^#\s+En la prensa {year}\s*$", md)
    if not marker:
        raise RuntimeError(f"No se encontró el título 'En la prensa {year}' en el Markdown")

    body = md[marker.end():]
    # Los recortes se publican como encabezados H3.
    matches = list(re.finditer(r"(?m)^###\s+(.+?)\s*$", body))
    entries = []

    for i, m in enumerate(matches):
        title = clean_text(m.group(1))
        low = title.lower()
        if any(low.startswith(x) for x in STOP_HEADINGS):
            break

        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        block = body[m.end():end]

        # Cortar si ya entramos en contenido editorial/recomendaciones de Medium.
        if re.search(r"(?im)^##\s+(Written by|More from|Recommended from|No responses)", block):
            block = re.split(
                r"(?im)^##\s+(?:Written by|More from|Recommended from|No responses)",
                block,
                maxsplit=1,
            )[0]

        iso, date_txt = parse_date(block, year)
        links = parse_links(block)

        # Conservador: si no hay fecha ni lenguaje de prensa, probablemente no es recorte.
        if iso == str(year) and not re.search(
            r"entrevista|reportaje|cobertura|nota|radio|canal|diario|revista|lun|mercurio",
            block,
            re.I,
        ):
            continue

        media = infer_media(block, links)
        link, link_type = choose_original_link(links)
        entries.append(
            Entry(
                fecha=iso,
                anio=year,
                medio=media,
                titulo=title,
                enlace=link,
                tipo_enlace=link_type,
                fuente_blog=url,
                fecha_texto=date_txt,
            )
        )

    # Deduplicación exacta por año + título.
    dedup = {}
    for e in entries:
        dedup[(e.anio, e.titulo.casefold())] = e

    expected = detect_expected(md, year)
    return list(dedup.values()), len(md), len(matches), expected


def write_outputs(entries: list[Entry], diagnostics: dict, expected: dict):
    entries = sorted(entries, key=lambda e: (e.fecha, e.titulo), reverse=True)

    csv_path = OUT / "prensa.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        fields = [
            "fecha", "anio", "medio", "titulo", "enlace", "tipo_enlace",
            "fuente_blog", "fecha_texto", "estado",
        ]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for e in entries:
            w.writerow(asdict(e))

    counts = Counter(e.anio for e in entries)
    linked = sum(bool(e.enlace) for e in entries)

    lines = [
        "# Archivo de entrevistas y apariciones en prensa",
        "",
        "Catálogo generado desde las páginas anuales de prensa de "
        "[blog.ariellopez.cl](https://blog.ariellopez.cl/).",
        "",
        "El índice se mantiene fuera del README del perfil. Cada registro conserva "
        "fecha, medio, título y, cuando está documentado en la fuente, enlace a la "
        "nota original o al video.",
        "",
        f"- Registros indexados: {len(entries)}",
        f"- Con enlace original/video documentado: {linked}",
        f"- Sin URL original documentada en el blog: {len(entries) - linked}",
        "",
        "## Cobertura por año",
        "",
        "| Año | Indexados | Declarados en la fuente | Estado | Fuente |",
        "|---:|---:|---:|---|---|",
    ]

    for year in sorted(PAGES, reverse=True):
        n = counts.get(year, 0)
        exp = expected.get(year)
        ok = "completo" if exp is not None and n == exp else ("por revisar" if exp else "sin total declarado")
        exp_txt = str(exp) if exp is not None else "—"
        lines.append(
            f"| {year} | {n} | {exp_txt} | {ok} | "
            f"[En la prensa {year}]({PAGES[year]}) |"
        )

    lines += [
        "",
        "## Catálogo",
        "",
        "> “Sin URL documentada” significa que la página anual registra el recorte "
        "y el medio, pero no contiene un enlace verificable a la publicación o video. "
        "No se inventan URLs.",
        "",
    ]

    for year in sorted(PAGES, reverse=True):
        yr = [e for e in entries if e.anio == year]
        lines += [
            f"### {year}",
            "",
            "| Fecha | Medio | Título | Enlace |",
            "|---|---|---|---|",
        ]
        for e in yr:
            title = e.titulo.replace("|", "\\|")
            media = e.medio.replace("|", "\\|")
            if e.enlace:
                label = "video" if e.tipo_enlace == "youtube" else "original"
                link = f"[{label}]({e.enlace})"
            else:
                link = "Sin URL documentada"
            lines.append(f"| {e.fecha} | {media} | {title} | {link} |")
        lines.append("")

    lines += [
        "## Criterio de indexación",
        "",
        "- La fuente primaria del catálogo son las páginas anuales mantenidas por Ariel López.",
        "- Jina Reader se usa únicamente como capa de lectura cuando Medium impide el acceso automatizado directo.",
        "- El año de la página se usa como año canónico para corregir errores tipográficos evidentes en fechas internas.",
        "- Se priorizan enlaces a YouTube cuando el video está explícitamente documentado.",
        "- Los enlaces auxiliares (normas, fuentes técnicas, redes sociales o material de apoyo) no se confunden con la noticia original.",
        "- El CSV es la versión estructurada y reutilizable del catálogo.",
        "",
        "## Actualización",
        "",
        "El archivo se regenera automáticamente cuando cambia el indexador o la lista de fuentes. "
        "También puede ejecutarse localmente con:",
        "",
        "```bash",
        "python scripts/index_prensa.py",
        "```",
        "",
    ]
    (OUT / "index.md").write_text("\n".join(lines), encoding="utf-8")

    state = {
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "total": len(entries),
        "with_link": linked,
        "without_link": len(entries) - linked,
        "counts_by_year": {str(y): counts.get(y, 0) for y in sorted(PAGES, reverse=True)},
        "expected_counts": {str(y): expected.get(y) for y in sorted(PAGES, reverse=True)},
        "diagnostics": diagnostics,
    }
    (OUT / "estado.json").write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main():
    all_entries = []
    diagnostics = {}
    expected = {}
    errors = {}

    for year, url in PAGES.items():
        try:
            entries, md_chars, headings, exp = extract_year(year, url)
            all_entries.extend(entries)
            expected[year] = exp
            diagnostics[str(year)] = {
                "url": url,
                "records": len(entries),
                "markdown_chars": md_chars,
                "candidate_headings": headings,
                "expected": exp,
                "complete": exp is not None and len(entries) == exp,
            }
            print(f"{year}: {len(entries)} registros; esperado={exp}; headings={headings}")
        except Exception as exc:
            errors[str(year)] = repr(exc)
            expected[year] = EXPECTED_KNOWN.get(year)
            diagnostics[str(year)] = {"url": url, "error": repr(exc)}
            print(f"ERROR {year}: {exc}", file=sys.stderr)

    write_outputs(all_entries, diagnostics, expected)

    if errors:
        print("Páginas con error:", json.dumps(errors, ensure_ascii=False), file=sys.stderr)


if __name__ == "__main__":
    main()
