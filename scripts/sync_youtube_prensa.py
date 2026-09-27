#!/usr/bin/env python3
"""
Cruza la playlist audiovisual de prensa de Ariel López con archivo/prensa/prensa.csv.

- Enumera la playlist con yt-dlp.
- Genera archivo/prensa/youtube_playlist.csv.
- Aplica un conjunto versionado de mapeos curados.
- Completa enlaces vacíos automáticamente sólo cuando la coincidencia es de alta confianza.
- Sincroniza los enlaces del índice humano archivo/prensa/index.md.
- Genera archivo/prensa/youtube_match_report.md con coincidencias y pendientes.
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
INDEX = ROOT / "archivo" / "prensa" / "index.md"
PLAYLIST_CSV = ROOT / "archivo" / "prensa" / "youtube_playlist.csv"
REPORT = ROOT / "archivo" / "prensa" / "youtube_match_report.md"
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLAzCbyGKyDPBSXrZb5NctMaQwpZPmpUMG"

# Mapeos revisados manualmente a partir del título del video, el medio y el registro
# anual ya documentado. Sólo se aplican si la fila de prensa aún no tiene enlace.
MANUAL_VIDEO_MAP = {
    ("2026-06-23","Experiencia Tech","El desafío de una movilidad inteligente"): "qiSEBsXfSZM",
    ("2026-06-03","Turno","¿Ha bajado la frecuencia de las micros?"): "ZaK4vA_PBaU",
    ("2026-05-31","Chilevisión","Evasiones: Contraloría aprueba duras sanciones"): "hVc75yWFvW8",
    ("2026-05-28","Chilevisión","Pasajeros de Buin y Talagante pasan 5 horas en el transporte público"): "P7KINSF0leM",
    ("2026-05-17","El Desconcierto","Experto revela recortes en micros y fallas ocultas en metro"): "KI6vFrEK8U0",
    ("2026-05-15","Radio La Metro","La accesibilidad no se mide en porcentajes de dispositivos dañados, porque un ascensor es parte de una trayectoria, un ascensor dañado corta el trayecto completo"): "rK62xVOsdHE",
    ("2026-05-06","Canal 13","Hay menos micros y el Metro está más lleno?"): "RJI_peC7eqI",
    ("2026-05-04","Radio ADN","Aumento de flujo de pasajeros en el transporte público tras el aumento del precio de los combustibles"): "2lUPQiq9jNE",
    ("2026-05-01","Canal 13","Gobierno ajusta sistema de transporte"): "RwBmZkIP4Lo",
    ("2026-04-29","Chilevisión","Mayor falla de escaleras mecánicas en un año"): "3pOlMiqAvdE",
    ("2026-04-22","Radio Bío Bío","¿Menor flujo de buses en Santiago?"): "fllMdTBe5Bo",
    ("2026-04-12","Meganoticias","¿Fin de los buses “oruga” por las noches?"): "z46NLS0mGhc",
    ("2026-03-23","Chilevisión","El transporte público es más barato que el automóvil"): "_2EMhZGeBgM",
    ("2026-03-23","Súbela Radio","¿Qué implican las reformas del MEPCO en nuestro bolsillo?"): "qXWV-oAsgg4",
    ("2026-03-22","TVN","Gobierno descarta reducción de buses operativos de flota Red"): "hp2iE6qCOek",
    ("2026-03-04","Canal 13","Asfaltaron la calle y taparon los desagües"): "iUWwHhZIM3Y",
    ("2026-02-04","Teletrece","Buscan a ciclista que huyó tras atropellar a mujer"): "tO7NVNrAp14",
    ("2026-01-28","Chilevisión","Usuarios en alerta por intenso calor en el Metro"): "oIzXFLzT1KE",
    ("2025-12-26","Meganoticias","¿Qué artículos se pueden subir a un tren? Guardias de EFE arrebatan regalo de navidad a una pasajera en el Biotren"): "lw-MUEorJZg",
    ("2025-11-05","Chilevisión","Señal de tránsito que permite pasar el semáforo con luz roja ilegalmente"): "8A1s-Z9nRXw",
    ("2025-07-31","Chilevisión","Tobalaba al límite: Acusan colapso en andén"): "xKTBmdeA4yA",
    ("2025-05-01","Chilevisión","Medidas de autocuidado peatonal para prevenir accidentes"): "wo7keUXeX8k",
    ("2025-04-19","Canal 13","Quedó atrapada y fue arrastrada por la micro"): "dIADb_pXgx0",
    ("2025-04-04","Chilevisión","Ascensores de Metro sin servicio hace un año"): "MaU_9CpTnP4",
    ("2025-03-12","Chilevisión","Tarifas de saturación en autopistas urbanas"): "shWGLIKIx9g",
    ("2025-02-11","Meganoticias","Alerta por accidentes en peajes"): "GyRzst7C2Fg",
    ("2025-01-09","Radio Bío Bío","Descarrilamiento en L2 del Metro de Santiago"): "WNm7xF17vWo",
    ("2024-09-08","Meganoticias","Tarifa de saturación en la mira"): "MDo4-dxOj_Q",
    ("2024-06-29","Mega","Continúan las filtraciones de agua en AVO por segundo año consecutivo"): "YkNxjkA2KPQ",
    ("2024-06-29","TVN","Continúan las filtraciones de agua en AVO por segundo año consecutivo"): "ZJ1JOduGubA",
    ("2024-06-29","Meganoticias","Continúan las filtraciones de agua en AVO por segundo año consecutivo"): "OHkdD9J4ylg",
    ("2024-03-17","Radio ADN","Buses de 2 pisos operan en Santiago hace más de una década"): "_Vx1l5C178M",
    ("2023-10-04","TVN","Las dudas que salpican a la concesionaria"): "zxLaFZoc9kQ",
    ("2023-09-28","Canal 13","Filtraciones en Autopista Vespucio Oriente"): "Ok277EqeA64",
    ("2023-09-13","Chilevisión","Por mal estado de las vías, motoristas en riesgo"): "57tCgT5581w",
    ("2023-09-11","Chilevisión","Mujer herida tras disparo a Metrotren Nos"): "x3vWbpOWQ18",
}

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

def sync_index(rows: list[dict]) -> None:
    if not INDEX.exists():
        return
    links = {
        (r.get("fecha",""), r.get("medio",""), r.get("titulo","")): r.get("enlace","")
        for r in rows if r.get("enlace")
    }
    out = []
    table_re = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$")
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        m = table_re.match(line)
        if not m:
            out.append(line)
            continue
        fecha, medio, titulo, current = m.groups()
        url = links.get((fecha, medio, titulo))
        if not url or not current.startswith("Sin URL"):
            out.append(line)
            continue
        label = "video" if "youtube.com/watch" in url or "youtu.be/" in url else "original"
        out.append(f"| {fecha} | {medio} | {titulo} | [{label}]({url}) |")
    INDEX.write_text("\n".join(out) + "\n", encoding="utf-8")

def main() -> int:
    videos = run_ytdlp()
    if not videos:
        raise SystemExit("No se pudieron enumerar videos de la playlist.")

    by_id = {v["video_id"]: v for v in videos}

    with PRESS.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fields = reader.fieldnames or []
        rows = list(reader)

    row_by_key = {(r["fecha"], r["medio"], r["titulo"]): r for r in rows}
    manual_records = []
    manual_video_ids = set()
    for key, vid in MANUAL_VIDEO_MAP.items():
        row = row_by_key.get(key)
        video = by_id.get(vid)
        if not row or not video:
            continue
        manual_video_ids.add(vid)
        if not row.get("enlace"):
            row["enlace"] = video["url"]
            base_note = (row.get("nota") or "").strip()
            extra = "Video curado desde la playlist de prensa del canal de Ariel López en YouTube."
            row["nota"] = (base_note + (" " if base_note else "") + extra).strip()
        manual_records.append({
            **video,
            "best_score": "curado",
            "gap": "—",
            "press_fecha": row["fecha"],
            "press_medio": row["medio"],
            "press_titulo": row["titulo"],
            "press_has_link": "yes",
            "decision": "manual_linked",
        })

    matches = []
    candidates = []
    used_rows = {i for i,r in enumerate(rows) if r.get("enlace") and "youtube.com/watch" in r.get("enlace","")}

    for v in videos:
        if v["video_id"] in manual_video_ids:
            continue
        ranked = []
        vtext = f"{v['title']} {v['description']}"
        for i, r in enumerate(rows):
            s = title_score(v["title"], r["titulo"])
            s += media_bonus(r["medio"], vtext)
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

        if score >= 0.91 and gap >= 0.055 and not row.get("enlace") and idx not in used_rows:
            row["enlace"] = v["url"]
            base_note = (row.get("nota") or "").strip()
            extra = "Video recuperado automáticamente desde la playlist de prensa del canal de Ariel López en YouTube."
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

    sync_index(rows)

    playlist_fields = [
        "video_id","title","upload_date","channel","url",
        "best_score","gap","press_fecha","press_medio","press_titulo","press_has_link","decision"
    ]
    allrecs = manual_records + matches + candidates
    with PLAYLIST_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=playlist_fields, extrasaction="ignore", quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(allrecs)

    manual = [x for x in allrecs if x["decision"] == "manual_linked"]
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
        f"- Mapeos curados versionados: **{len(manual)}**",
        f"- Enlaces incorporados automáticamente por similitud: **{len(linked)}**",
        f"- Coincidencias para revisión: **{len(review)}**",
        f"- Videos sin coincidencia suficiente: **{len(unmatched)}**",
        "",
        "El cruce combina mapeos curados y coincidencia conservadora. Los enlaces originales de medios nunca son reemplazados por YouTube.",
        "",
        "## Mapeos curados",
        "",
        "| Video | Fecha YouTube | Fecha prensa | Medio | Registro | Score |",
        "|---|---|---|---|---|---:|",
    ]
    md += [rowmd(x) for x in manual] or ["| — | — | — | — | Sin mapeos curados | — |"]
    md += [
        "",
        "## Coincidencias automáticas incorporadas",
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
        "manual_mapped": len(manual),
        "auto_linked": len(linked),
        "review": len(review),
        "unmatched": len(unmatched),
    }, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
