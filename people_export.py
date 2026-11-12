"""Exports who Apple Photos has named in each photo, for the Boz family archive (Beehive 159b46e7).

Read-only: opens the Photos library through osxphotos and writes one JSON file. Nothing in Photos
changes. For each photo or video with at least one named person it records the capture time, the
names, and a perceptual hash (imagehash 4.3.2 phash, the same one the enrichment job uses) of a
preview Photos already keeps on disk, so purplebee-enc can match it to Flickr items and album
uploads by time and confirm by image.

Run it in the Terminal app (it needs Full Disk Access; the terminal built into other apps is refused).
Family members get it from github.com/AIRSHP/boz-family-photos (see the user guide there):

    osxphotos run people_export.py --person dustin --out ~/boz-people-dustin.json

The file holds family names. It goes only to purplebee-enc and the family B2 folder.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import socket
import sys
from pathlib import Path

import imagehash
import osxphotos
from PIL import Image, ImageOps

SCHEMA = "boz-family-people-export/1"
ALBUM = "Boz Family Archive Sync"
READABLE = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".gif", ".bmp", ".webp"}


def image_path(p) -> Path | None:
    """A file Pillow can open that shows the photo as Photos does: a derivative first, else the original."""
    candidates = [Path(x) for x in (p.path_derivatives or [])]
    if p.path:
        candidates.append(Path(p.path))
    for c in candidates:
        if c.suffix.lower() in READABLE and c.exists():
            return c
    return None


def phash_of(path: Path) -> str | None:
    try:
        with Image.open(path) as img:
            img = ImageOps.exif_transpose(img).convert("RGB")
            return str(imagehash.phash(img))
    except Exception:
        return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--person", required=True, help="whose library this is, e.g. dustin or evan")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    if not args.person.isalpha():
        sys.exit("--person must be a single word, e.g. dustin")

    db = osxphotos.PhotosDB()
    album_uuids = {p.uuid for a in db.album_info if a.title == ALBUM for p in a.photos}
    items, no_hash = [], 0
    for p in db.photos(intrash=False):
        names = sorted({n for n in p.persons if n and n != "_UNKNOWN_"})
        if not names or not p.date:
            continue
        path = image_path(p)
        h = phash_of(path) if path else None
        no_hash += h is None
        items.append({
            "uuid": p.uuid,
            "taken_local": p.date.replace(tzinfo=None).strftime("%Y-%m-%d %H:%M:%S"),
            "taken_utc": p.date.astimezone(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
            "kind": "video" if p.ismovie else "photo",
            "names": names,
            "phash": h,
            "in_archive_album": p.uuid in album_uuids,
            "original_filename": p.original_filename,
        })

    doc = {
        "schema": SCHEMA,
        "person": args.person.lower(),
        "source": f"{args.person.capitalize()}'s Apple Photos (names as Photos has them)",
        "made_by": {"tool": "tools/family_archive_enrich/people_export.py", "host": socket.gethostname().split(".")[0].lower(),
                    "osxphotos": osxphotos.__version__, "imagehash": imagehash.__version__},
        "made_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "items": items,
    }
    out = Path(args.out).expanduser()
    out.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    print(f"named items: {len(items)} | without an image hash: {no_hash} | in the archive album: {sum(i['in_archive_album'] for i in items)}")
    print(f"distinct names: {len({n for i in items for n in i['names']})} | written to {out}")


if __name__ == "__main__":
    main()
