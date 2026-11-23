#!/usr/bin/env python3
from pathlib import Path
import re, sys

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("../index.html")
if not target.is_absolute():
    target = (Path(__file__).resolve().parent / target).resolve()
html = target.read_text(encoding="utf-8")
scripts = re.findall(r"<script\\b[^>]*>(.*?)</script\\s*>", html, re.I | re.S)
ids = re.findall(r'\\bid=["\\']([^"\\']+)["\\']', html, re.I)
dupes = sorted({x for x in ids if ids.count(x) > 1})
print(f"File: {target}")
print(f"Script blocks: {len(scripts)}")
print(f"Duplicate IDs: {dupes or 'none'}")
print("HTML file read: OK")
