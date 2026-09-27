#!/usr/bin/env python3
"""
Cruza la playlist audiovisual de prensa de Ariel López con archivo/prensa/prensa.csv.

- Enumera la playlist con yt-dlp.
- Genera archivo/prensa/youtube_playlist.csv.
- Completa enlaces vacíos sólo cuando la coincidencia es de alta confianza.
- Genera archivo/prensa/youtube_match_report.md con coincidencias, candidatos y videos no enlazados.
"""
from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRESS = ROOT / "archivo" / "prensa" / "prensa.csv"
PLAYLIST_CSV = ROOT / "archivo" / "prensa" / "youtube_playlist.csv"
REPORT = ROOT / "archivo" / "prensa" / "youtube_match_report.md"
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLAzCbyGKyDPBSXrZb5NctMaQwpZPmpUMG"

MEDIA_ALIASES = {
    "chilevision": ["chilevision", "chv"],
    "canal 13": ["canal 13", "t13", "teletrece"],
    "teletrece": ["t13", "teletrece", "canal 13"],
    "tvn": ["tvn", "24 horas"],
    "24 horas": ["24 horas", "tvn"],
    "mega": ["mega", "meganoticias"],
    "meganoticias": ["meganoticias", "mega"],
    "radio bio bio": ["bio bio", "biobio"],
    "radio biobio": ["bio bio", "biobio"],
    "radio adn": ["adn"],
    "cnn chile": ["cnn", "cnn chile"],
    "radio 13c": ["13c", "radio 13c"],
    "radio t13c": ["13c", "t13c", "radio 13c"],
    "lun": ["lun", "las ultimas noticias"],
}

STOP = {
    "de","del","la","las","el","los","y","en","un","una","unos","unas",
    "por","para","con","a","al","que","se","es","su","sus","sobre","tras",
    "como","mas","más","menos","chile","santiago"
}

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"https?://\S+", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def toks(s: str) -> set[str]:
    return {t for t in norm(s).split() if len(t) > 2 and t not in STOP}

def title_score(a: str, b: str) -> float:
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return 0.0
    seq = SequenceMatcher(None, na, nb).ratio()
    ta, tb = toks(a), toks(b)
    jac = len(ta & tb) / max(1, len(ta | tb))
    containment = len(ta & tb) / max(1, min(len(ta), len(tb)))
    return max(seq, 0.58 * jac + 0.42 * containment)

def media_bonus(media: str, video_text: str) -> float:
    nm = norm(media)
    aliases = MEDIA_ALIASES.get(nm, [nm])
    nv = norm(video_text)
    return 0.08 if any(a and norm(a) in nv for a in aliases) else 0.0

def run_ytdlp() -> list[dict]:
    cmd = [
        "yt-dlp", "--ignore-errors", "--flat-playlist", "--no-warnings",
        "--dump-json", PLAYLIST_URL
    ]
    p = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if p.returncode not in (0, 1):
        print(p.stderr, file=sys.stderr)
        raise SystemExit(p.returncode)
    entries = []
    for line in p.stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            j = json.loads(line)
        except json.JSONDecodeError:
            continue
        vid = j.get("id")
        if not vid:
            continue
        entries.append({
            "video_id": vid,
            "title": j.get("title") or "",
            "upload_date": j.get("upload_date") or "",
            "channel": j.get("channel") or j.get("uploader") or "",
            "description": "",
            "url": f"https://www.youtube.com/watch?v={vid}",
        })
    return entries

def main() -> int:
    videos = run_ytdlp()
    if not videos:
        raise SystemExit("No se pudieron enumerar videos de la playlist.")

    with PRESS.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fields = reader.fieldnames or []
        rows = list(reader)

    matches = []
    candidates = []
    used_rows = set()

    for v in videos:
        ranked = []
        vtext = f"{v['title']} {v['description']}"
        for i, r in enumerate(rows):
            s = title_score(v["title"], r["titulo"])
            s += media_bonus(r["medio"], vtext)
            # pequeñas pistas textuales por fecha/año sólo si aparecen en título/descripcion
            if r["anio"] and r["anio"] in vtext:
                s += 0.02
            ranked.append((min(s, 1.0), i, r))
        ranked.sort(key=lambda x: x[0], reverse=True)
        best = ranked[0]
        second = ranked[1] if len(ranked) > 1 else (0.0, -1, {})
        score, idx, row = best
        gap = score - second[0]

        rec = {
            **v,
            "best_score": f"{score:.3f}",
            "gap": f"{gap:.3f}",
            "press_fecha": row.get("fecha", ""),
            "press_medio": row.get("medio", ""),
            "press_titulo": row.get("titulo", ""),
            "press_has_link": "yes" if row.get("enlace") else "no",
        }

        # Auto-enlace sólo con evidencia muy fuerte, fila aún sin URL y match único.
        if score >= 0.91 and gap >= 0.055 and not row.get("enlace") and idx not in used_rows:
            row["enlace"] = v["url"]
            base_note = (row.get("nota") or "").strip()
            extra = "Video recuperado desde la playlist de prensa del canal de Ariel López en YouTube."
            row["nota"] = (base_note + (" " if base_note else "") + extra).strip()
            used_rows.add(idx)
            rec["decision"] = "auto_linked"
            matches.append(rec)
        elif score >= 0.70:
            rec["decision"] = "review"
            candidates.append(rec)
        else:
            rec["decision"] = "unmatched"
            candidates.append(rec)

    with PRESS.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)

    playlist_fields = [
        "video_id","title","upload_date","channel","url",
        "best_score","gap","press_fecha","press_medio","press_titulo","press_has_link","decision"
    ]
    allrecs = matches + candidates
    with PLAYLIST_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=playlist_fields, extrasaction="ignore", quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(allrecs)

    linked = [x for x in allrecs if x["decision"] == "auto_linked"]
    review = [x for x in allrecs if x["decision"] == "review"]
    unmatched = [x for x in allrecs if x["decision"] == "unmatched"]
    channel_counts = Counter(v["channel"] for v in videos)

    def rowmd(x):
        return (
            f"| [{x['title']}]({x['url']}) | {x['upload_date'] or '—'} | "
            f"{x['press_fecha'] or '—'} | {x['press_medio'] or '—'} | "
            f"{x['press_titulo'] or '—'} | {x['best_score']} |"
        )

    md = [
        "# Cruce de playlist de prensa en YouTube",
        "",
        f"Playlist: {PLAYLIST_URL}",
        "",
        f"- Videos enumerados: **{len(videos)}**",
        f"- Enlaces incorporados automáticamente a prensa.csv: **{len(linked)}**",
        f"- Coincidencias para revisión: **{len(review)}**",
        f"- Videos sin coincidencia suficiente: **{len(unmatched)}**",
        "",
        "La actualización automática es conservadora: sólo se enlazan filas sin URL cuando la similitud es >= 0,91 y existe separación suficiente respecto del segundo candidato.",
        "",
        "## Coincidencias incorporadas",
        "",
        "| Video | Fecha YouTube | Fecha prensa | Medio | Registro | Score |",
        "|---|---|---|---|---|---:|",
    ]
    md += [rowmd(x) for x in linked] or ["| — | — | — | — | Sin enlaces automáticos nuevos | — |"]
    md += [
        "",
        "## Candidatos para revisión",
        "",
        "| Video | Fecha YouTube | Fecha prensa | Medio | Registro | Score |",
        "|---|---|---|---|---|---:|",
    ]
    md += [rowmd(x) for x in review] or ["| — | — | — | — | Sin candidatos | — |"]
    md += [
        "",
        "## Videos sin correspondencia suficiente",
        "",
        "| Video | Fecha YouTube | Mejor fecha | Mejor medio | Mejor registro | Score |",
        "|---|---|---|---|---|---:|",
    ]
    md += [rowmd(x) for x in unmatched] or ["| — | — | — | — | Ninguno | — |"]
    md += [
        "",
        "## Canales/uploader reportados por YouTube",
        "",
    ]
    md += [f"- {k or '(sin dato)'}: {n}" for k,n in channel_counts.most_common()]
    md += [
        "",
        "## Política",
        "",
        "El inventario de YouTube complementa, pero no reemplaza, la fuente del medio. La prioridad sigue siendo: URL original del medio → video de la playlist propia → otro video exacto → copia institucional verificable.",
        "",
    ]
    REPORT.write_text("\n".join(md), encoding="utf-8")

    print(json.dumps({
        "videos": len(videos),
        "auto_linked": len(linked),
        "review": len(review),
        "unmatched": len(unmatched),
    }, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
