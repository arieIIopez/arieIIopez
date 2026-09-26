#!/usr/bin/env python3
"""
Construye un archivo histórico de entrevistas y apariciones en prensa de
Ariel López desde las páginas anuales publicadas en blog.ariellopez.cl.

La vía primaria usa el modelo JSON estructurado de cada publicación de Medium
a partir de su ID estable. Esto evita depender del HTML renderizado del blog y
permite recuperar fechas, títulos y enlaces embebidos de forma reproducible.

Salidas:
  archivo/prensa/index.md
  archivo/prensa/prensa.csv
  archivo/prensa/estado.json

El README del perfil no se modifica.
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
    "pauta.cl": "Radio Pauta",
    "uchile.cl": "Universidad de Chile",
    "revistacapital.cl": "Revista Capital",
    "df.cl": "Diario Financiero",
    "dfmas.df.cl": "DF MAS",
    "24horas.cl": "TVN / 24 Horas",
}

MEDIA_ALIASES = [
    "Chilevisión", "Chilevision", "Canal 13", "Teletrece", "T13", "TVN",
    "Canal 24 Horas", "Canal 24 horas", "24 Horas", "Meganoticias",
    "Megavisión", "Mega", "La Tercera", "LUN", "El Mercurio",
    "El Mercurio de Valparaíso", "Radio Bío Bío", "Radio Biobío",
    "Radio Biobio", "Biobío", "Biobio", "Radio ADN", "ADN Radio",
    "Radio 13C", "Radio T13C", "Tele13 Radio", "Súbela Radio",
    "CNN Chile", "CNN", "The Clinic", "El Dínamo", "El Dinamo",
    "El Desconcierto", "Contrapoder", "Diario Usach", "Diario USACH",
    "Doble Espacio", "FastCheck", "Fast Check", "Revista Pedalea",
    "Latamobility", "Experiencia Tech", "LaBot", "El Mostrador",
    "Radio Pauta", "Pauta", "Revista Capital", "Diario Financiero",
    "DF MAS", "Turno",
]

SKIP_LINK_DOMAINS = {
    "blog.ariellopez.cl", "ariellopez.cl", "medium.com",
    "miro.medium.com", "x.com", "twitter.com", "bcn.cl",
    "patents.google.com", "archivos.lascondes.cl", "seia.sea.gob.cl",
    "avo.cl", "linkedin.com",
}

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


def post_id(url: str) -> str:
    m = re.search(r"-([0-9a-f]{12})/?(?:\?.*)?$", url)
    if not m:
        raise ValueError(f"No se pudo extraer el post ID de {url}")
    return m.group(1)


def unwrap_url(url: str) -> str:
    if not url:
        return ""
    url = html.unescape(url).strip()
    p = urlparse(url)
    if p.netloc.lower().endswith("medium.com") and p.path.startswith("/r/"):
        q = parse_qs(p.query)
        if q.get("url"):
            return unquote(q["url"][0])
    return url


def domain(url: str) -> str:
    try:
        return urlparse(url).netloc.lower().removeprefix("www.")
    except Exception:
        return ""


def fetch_medium_post(url: str):
    pid = post_id(url)
    endpoint = f"https://medium.com/post/{pid}?format=json"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/128.0 Safari/537.36"
        ),
        "Accept": "application/json,text/plain,*/*",
    }
    r = requests.get(endpoint, headers=headers, timeout=60, allow_redirects=True)
    r.raise_for_status()
    raw = r.text
    pos = raw.find("{")
    if pos < 0:
        raise RuntimeError(
            f"Medium JSON sin objeto JSON para post {pid}; status={r.status_code}; "
            f"len={len(raw)}"
        )
    data = json.loads(raw[pos:])
    value = data.get("payload", {}).get("value")
    if not isinstance(value, dict):
        raise RuntimeError(f"Medium JSON sin payload.value para post {pid}")
    paragraphs = (
        value.get("content", {})
        .get("bodyModel", {})
        .get("paragraphs", [])
    )
    if not paragraphs:
        raise RuntimeError(f"Medium JSON sin párrafos para post {pid}")
    return value, paragraphs, endpoint, len(raw)


def paragraph_links(p: dict):
    found = []

    def add(label, href):
        href = unwrap_url(str(href or ""))
        if href.startswith(("http://", "https://")) and not any(u == href for _, u in found):
            found.append((clean_text(label), href))

    add(p.get("text", ""), p.get("href"))

    for m in p.get("markups") or []:
        if isinstance(m, dict):
            text = p.get("text", "")
            start, end = m.get("start"), m.get("end")
            label = ""
            if isinstance(start, int) and isinstance(end, int):
                label = text[start:end]
            add(label, m.get("href"))

    mm = p.get("mixtapeMetadata") or {}
    if isinstance(mm, dict):
        add(p.get("text", ""), mm.get("href"))

    iframe = p.get("iframe") or {}
    if isinstance(iframe, dict):
        res = iframe.get("mediaResource") or {}
        if isinstance(res, dict):
            add(p.get("text", ""), res.get("href"))
            add(p.get("text", ""), res.get("iframeSrc"))

    return found


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
        "24 Horas": "TVN / 24 Horas",
        "Megavisión": "Mega",
        "Biobío": "Radio Bío Bío",
        "Biobio": "Radio Bío Bío",
        "Radio Biobío": "Radio Bío Bío",
        "Radio Biobio": "Radio Bío Bío",
        "ADN Radio": "Radio ADN",
        "Radio 13C": "Radio T13C",
        "El Dinamo": "El Dínamo",
        "FastCheck": "Fast Check",
        "Pauta": "Radio Pauta",
    }
    return mapping.get(n, n)


def infer_media(text: str, links: list[tuple[str, str]]) -> str:
    # Pie explícito: "Canal 13 | 20.09.2026".
    for line in text.splitlines():
        line = clean_text(line)
        if "|" in line and len(line) < 120:
            left = clean_text(line.split("|", 1)[0])
            if 2 <= len(left) <= 55 and not left.lower().startswith(("fuente", "pág", "pagina")):
                return canonical_media(left)

    combined = clean_text(text)
    for alias in MEDIA_ALIASES:
        if re.search(rf"(?<!\w){re.escape(alias)}(?!\w)", combined, re.I):
            return canonical_media(alias)

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

    # Prioridad 1: la nota original en un medio reconocido.
    for _, u, d in candidates:
        if d in MEDIA_BY_DOMAIN and d not in {"youtube.com", "youtu.be"}:
            return u, "original"

    # Prioridad 2: video de YouTube documentado en el mismo recorte.
    for _, u, d in candidates:
        if d in {"youtube.com", "youtu.be"}:
            return u, "youtube"

    # Prioridad 3: primer enlace externo, siempre conservando su naturaleza
    # explícita en el CSV para una futura auditoría manual.
    if candidates:
        return candidates[0][1], "externo_documentado"

    return "", "sin_url_documentada"


def detect_expected(paragraphs, year):
    text = "\n".join(clean_text(p.get("text", "")) for p in paragraphs[:12])
    m = re.search(r"\b(\d{1,3})\s+Recortes de prensa", text, re.I)
    if m:
        return int(m.group(1))
    return EXPECTED_KNOWN.get(year)


def extract_year(year: int, url: str):
    value, paragraphs, endpoint, raw_len = fetch_medium_post(url)

    # En el modelo JSON de Medium los subtítulos de cada recorte están marcados
    # como H3. Si Medium cambia la representación, el diagnóstico conserva la
    # distribución de tipos y el año queda "por revisar", nunca se inventan datos.
    heading_idx = [
        i for i, p in enumerate(paragraphs)
        if str(p.get("type", "")).upper() == "H3" and clean_text(p.get("text", ""))
    ]

    entries = []
    for pos, i in enumerate(heading_idx):
        title = clean_text(paragraphs[i].get("text", ""))
        j = heading_idx[pos + 1] if pos + 1 < len(heading_idx) else len(paragraphs)
        block_pars = paragraphs[i + 1:j]

        lines = [clean_text(p.get("text", "")) for p in block_pars if clean_text(p.get("text", ""))]
        block_text = "\n".join(lines)
        links = []
        for p in block_pars:
            links.extend(paragraph_links(p))

        # Evita encabezados editoriales no vinculados con el archivo de prensa.
        iso, date_txt = parse_date(block_text, year)
        if iso == str(year) and not re.search(
            r"entrevista|reportaje|cobertura|nota|radio|canal|diario|revista|"
            r"lun|mercurio|televisión|television|prensa",
            block_text,
            re.I,
        ):
            continue

        media = infer_media(block_text, links)
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
    entries = list(dedup.values())

    types = Counter(str(p.get("type", "")) for p in paragraphs)
    expected = detect_expected(paragraphs, year)
    return entries, {
        "url": url,
        "medium_post_id": post_id(url),
        "medium_endpoint": endpoint,
        "title": value.get("title"),
        "paragraphs": len(paragraphs),
        "paragraph_types": dict(types),
        "h3_headings": len(heading_idx),
        "records": len(entries),
        "expected": expected,
        "raw_chars": raw_len,
        "complete": expected is not None and len(entries) == expected,
    }, expected


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
        "Catálogo histórico de entrevistas y apariciones en prensa documentadas por "
        "Ariel López en las páginas anuales de blog.ariellopez.cl.",
        "",
        "Este archivo está separado del README del perfil. Cada registro conserva "
        "fecha, medio, título y, cuando está documentado en la publicación original, "
        "el enlace a la noticia o al video.",
        "",
        f"- Registros indexados: {len(entries)}",
        f"- Con enlace original/video documentado: {linked}",
        f"- Sin URL original documentada: {len(entries) - linked}",
        "",
        "## Cobertura por año",
        "",
        "| Año | Indexados | Declarados en la fuente | Estado | Fuente |",
        "|---:|---:|---:|---|---|",
    ]

    for year in sorted(PAGES, reverse=True):
        n = counts.get(year, 0)
        exp = expected.get(year)
        complete = exp is not None and n == exp
        status = "completo" if complete else ("por revisar" if exp is not None else "sin total declarado")
        exp_txt = str(exp) if exp is not None else "—"
        lines.append(
            f"| {year} | {n} | {exp_txt} | {status} | "
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
        "- La fuente de verdad del inventario son las páginas anuales mantenidas por Ariel López.",
        "- El contenido se recupera desde el modelo estructurado de la publicación de Medium usando su ID estable.",
        "- El año de la página es el año canónico del registro; esto evita propagar errores tipográficos de año dentro de un recorte.",
        "- Se prioriza el enlace a la noticia original; cuando no existe y el recorte documenta un video de YouTube, se conserva ese video.",
        "- Enlaces técnicos o auxiliares no se presentan como si fueran la noticia original.",
        "- El CSV es la versión estructurada y reutilizable del catálogo.",
        "",
        "## Actualización",
        "",
        "El archivo puede regenerarse con:",
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

    for year, url in PAGES.items():
        try:
            entries, diag, exp = extract_year(year, url)
            all_entries.extend(entries)
            diagnostics[str(year)] = diag
            expected[year] = exp
            print(
                f"{year}: {len(entries)} registros; esperado={exp}; "
                f"H3={diag.get('h3_headings')}; types={diag.get('paragraph_types')}"
            )
        except Exception as exc:
            expected[year] = EXPECTED_KNOWN.get(year)
            diagnostics[str(year)] = {
                "url": url,
                "medium_post_id": post_id(url),
                "error": repr(exc),
            }
            print(f"ERROR {year}: {exc}", file=sys.stderr)

    write_outputs(all_entries, diagnostics, expected)


if __name__ == "__main__":
    main()
