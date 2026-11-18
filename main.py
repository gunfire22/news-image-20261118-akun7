#!/usr/bin/env python3
"""news-image-20261118 entry (akun 7): copy the pre-composed front page to
/output/entry.png, byte-identical. No network, deterministic.

The front page (image.jpg, 1024x1024, 254905 bytes) was composed from three
photorealistic panels (Manila summit lead, Kerch Bridge day 2, Cyclone Akvan)
with PIL-drawn masthead, date strip, headlines and footer.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.jpg")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    size = os.path.getsize(SRC)
    if size > 1048576:
        raise SystemExit(f"image too large: {size} bytes (limit 1 MiB)")
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
