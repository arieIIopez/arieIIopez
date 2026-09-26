#!/usr/bin/env python3
"""
Genera el archivo histórico de apariciones en prensa de Ariel López a partir de
las páginas anuales publicadas en blog.ariellopez.cl.

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
from bs4 import BeautifulSoup, Tag

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

EXPECTED = {
    2026: 88,
    2024: 36,
    2023: 30,
    2020: 46,
}

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
    "El Dinamo", "El Desconcierto", "Contrapoder", "Diario USACH",
    "Doble Espacio", "FastCheck", "Fast Check", "Revista Pedalea",
    "Latamobility", "Experiencia Tech", "LaBot", "El Mostrador",
]

SKIP_LINK_DOMAINS = {
    "blog.ariellopez.cl", "ariellopez.cl", "medium.com", "www.medium.com",
    "miro.medium.com", "x.com", "twitter.com", "www.twitter.com",
    "bcn.cl", "www.bcn.cl", "patents.google.com", "archivos.lascondes.cl",
    "seia.sea.gob.cl", "avo.cl", "www.avo.cl",
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
    return re.sub(r"\s+", " ", html.unescape(s or "")).strip()


def unwrap_url(url: str) -> str:
    if not url:
        return ""
    url = html.unescape(url)
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


def fetch(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/128.0 Safari/537.36"
        ),
        "Accept-Language": "es-CL,es;q=0.9,en;q=0.7",
        "Accept": "text/html,application/xhtml+xml",
    }
    r = requests.get(url, headers=headers, timeout=35, allow_redirects=True)
    r.raise_for_status()
    return r.text


def visible_article(soup: BeautifulSoup) -> Tag:
    return soup.find("article") or soup.find("main") or soup.body or soup


def heading_candidates(article: Tag, year: int) -> list[Tag]:
    heads = article.find_all(["h1", "h2", "h3", "h4"])
    start = 0
    for i, h in enumerate(heads):
        if f"en la prensa {year}" in clean_text(h.get_text(" ", strip=True)).lower():
            start = i + 1
            break

    out = []
    for h in heads[start:]:
        title = clean_text(h.get_text(" ", strip=True))
        low = title.lower()
        if any(low.startswith(x) for x in STOP_HEADINGS):
            break
        if not title or title == "Ariel López":
            continue
        if low.startswith("en la prensa"):
            continue
        out.append(h)
    return out


def block_after_heading(h: Tag):
    texts = []
    links = []
    for el in h.next_elements:
        if el is h:
            continue
        if isinstance(el, Tag) and el.name in {"h1", "h2", "h3", "h4"}:
            break
        if isinstance(el, Tag) and el.name == "a":
            href = unwrap_url(el.get("href", ""))
            label = clean_text(el.get_text(" ", strip=True))
            if href:
                links.append((label, href))
        if isinstance(el, Tag) and el.name in {"p", "blockquote", "li", "figcaption"}:
            txt = clean_text(el.get_text(" ", strip=True))
            if txt and (not texts or texts[-1] != txt):
                texts.append(txt)
    return texts, links


def parse_date(text: str, year: int):
    low = text.lower()
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


def infer_media(text: str, links: list[tuple[str, str]]) -> str:
    # 1) Pie corto del tipo "Canal 13 | 20.09.2026".
    for chunk in [clean_text(x) for x in text.split("\n") if clean_text(x)]:
        if "|" in chunk and len(chunk) < 100:
            left = clean_text(chunk.split("|", 1)[0])
            if 2 <= len(left) <= 50 and not left.lower().startswith(("fuente", "pág")):
                return canonical_media(left)

    # 2) Nombres de medios mencionados explícitamente.
    for alias in MEDIA_ALIASES:
        if re.search(rf"\b{re.escape(alias)}\b", text, re.I):
            return canonical_media(alias)

    # 3) Dominio del enlace periodístico.
    for _, u in links:
        d = domain(u)
        if d in MEDIA_BY_DOMAIN:
            return MEDIA_BY_DOMAIN[d]
    return "Medio no identificado"


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


def choose_original_link(links: list[tuple[str, str]], media: str) -> tuple[str, str]:
    candidates = []
    for label, u in links:
        d = domain(u)
        if not d or d in SKIP_LINK_DOMAINS:
            continue
        if u.startswith(("mailto:", "javascript:")):
            continue
        candidates.append((label, u, d))

    # Video documentado tiene prioridad cuando existe.
    for _, u, d in candidates:
        if d in {"youtube.com", "youtu.be"}:
            return u, "youtube"

    # Luego un enlace reconocido a medio.
    for _, u, d in candidates:
        if d in MEDIA_BY_DOMAIN:
            return u, "original"

    # Finalmente, primer enlace externo no auxiliar.
    if candidates:
        return candidates[0][1], "original"
    return "", "sin_url_documentada"


def extract_year(year: int, url: str):
    raw = fetch(url)
    soup = BeautifulSoup(raw, "lxml")
    article = visible_article(soup)
    heads = heading_candidates(article, year)

    entries = []
    for h in heads:
        title = clean_text(h.get_text(" ", strip=True))
        texts, links = block_after_heading(h)
        block = "\n".join(texts)

        # Filtro conservador: un recorte debe tener fecha o lenguaje de prensa.
        iso, date_txt = parse_date(block, year)
        if iso == str(year) and not re.search(
            r"entrevista|reportaje|cobertura|nota|radio|canal|diario|revista|lun|mercurio",
            block, re.I,
        ):
            continue

        media = infer_media(block, links)
        link, link_type = choose_original_link(links, media)
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

    # Deduplicación por año+título.
    dedup = {}
    for e in entries:
        dedup[(e.anio, e.titulo.casefold())] = e
    return list(dedup.values()), len(raw), len(heads)


def write_outputs(entries: list[Entry], diagnostics: dict):
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
        "| Año | Registros | Fuente |",
        "|---:|---:|---|",
    ]
    for year in sorted(PAGES, reverse=True):
        lines.append(
            f"| {year} | {counts.get(year, 0)} | "
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
        "expected_counts_when_known": EXPECTED,
        "diagnostics": diagnostics,
    }
    (OUT / "estado.json").write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main():
    all_entries = []
    diagnostics = {}
    errors = {}

    for year, url in PAGES.items():
        try:
            entries, html_bytes, headings = extract_year(year, url)
            all_entries.extend(entries)
            diagnostics[str(year)] = {
                "url": url,
                "records": len(entries),
                "html_chars": html_bytes,
                "candidate_headings": headings,
                "expected": EXPECTED.get(year),
            }
            print(f"{year}: {len(entries)} registros; {headings} encabezados candidatos")
        except Exception as exc:
            errors[str(year)] = repr(exc)
            diagnostics[str(year)] = {"url": url, "error": repr(exc)}
            print(f"ERROR {year}: {exc}", file=sys.stderr)

    write_outputs(all_entries, diagnostics)

    # No abortamos por una página temporalmente inaccesible: el estado queda
    # explícito y el catálogo parcial sigue siendo auditable.
    if errors:
        print("Páginas con error:", json.dumps(errors, ensure_ascii=False), file=sys.stderr)


if __name__ == "__main__":
    main()
