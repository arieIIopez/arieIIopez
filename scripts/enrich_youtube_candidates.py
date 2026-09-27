#!/usr/bin/env python3
"""
Enriquece los videos sin correspondencia suficiente del cruce de prensa con
metadata individual de YouTube. No modifica prensa.csv.
"""
from __future__ import annotations
import csv, json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"archivo"/"prensa"/"youtube_playlist.csv"
OUT=ROOT/"archivo"/"prensa"/"youtube_unmatched_enriched.csv"

def main():
    with SRC.open(newline="",encoding="utf-8") as fh:
        rows=list(csv.DictReader(fh))
    pending=[r for r in rows if r.get("decision")=="unmatched" and r.get("video_id")]
    urls=[f"https://www.youtube.com/watch?v={r['video_id']}" for r in pending]
    if not urls:
        print("No unmatched videos")
        return 0
    cmd=["yt-dlp","--ignore-errors","--skip-download","--no-warnings","--dump-json",*urls]
    p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True,timeout=900)
    meta={}
    for line in p.stdout.splitlines():
        line=line.strip()
        if not line.startswith("{"): continue
        try: j=json.loads(line)
        except json.JSONDecodeError: continue
        vid=j.get("id")
        if vid: meta[vid]=j

    fields=[
      "video_id","title_playlist","channel_playlist","url",
      "upload_date","timestamp","channel","uploader","duration",
      "title_youtube","description",
      "best_score","press_fecha","press_medio","press_titulo"
    ]
    out=[]
    for r in pending:
        j=meta.get(r["video_id"],{})
        out.append({
          "video_id":r["video_id"],
          "title_playlist":r.get("title",""),
          "channel_playlist":r.get("channel",""),
          "url":r.get("url",""),
          "upload_date":j.get("upload_date") or "",
          "timestamp":j.get("timestamp") or "",
          "channel":j.get("channel") or "",
          "uploader":j.get("uploader") or "",
          "duration":j.get("duration") or "",
          "title_youtube":j.get("title") or "",
          "description":(j.get("description") or "").replace("\r"," ").replace("\n"," ").strip(),
          "best_score":r.get("best_score",""),
          "press_fecha":r.get("press_fecha",""),
          "press_medio":r.get("press_medio",""),
          "press_titulo":r.get("press_titulo",""),
        })
    with OUT.open("w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=fields,quoting=csv.QUOTE_ALL)
        w.writeheader(); w.writerows(out)
    print(json.dumps({"pending":len(pending),"metadata_recovered":len(meta),"output":str(OUT.relative_to(ROOT))},ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
