#!/usr/bin/env python3
"""Generate github-data/vocabulary.json from the easy-to-edit CSV file."""
import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "github-data" / "vocabulary.csv"
target = ROOT / "github-data" / "vocabulary.json"
items = []
with source.open("r", encoding="utf-8-sig", newline="") as f:
    for row_num, row in enumerate(csv.DictReader(f), start=2):
        korean = (row.get("korean") or "").strip()
        meaning = (row.get("meaning") or "").strip()
        if not korean and not meaning:
            continue
        if not korean or not meaning:
            raise SystemExit(f"Baris {row_num}: kolom korean dan meaning wajib diisi.")
        try:
            item_id = int(row.get("id") or len(items) + 1)
            source_number = int(row.get("sourceNumber") or item_id)
        except ValueError:
            raise SystemExit(f"Baris {row_num}: id dan sourceNumber harus angka.")
        items.append({"id": item_id, "sourceNumber": source_number, "korean": korean, "meaning": meaning})
if not items:
    raise SystemExit("CSV tidak berisi kosakata. JSON tidak diubah.")
target.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Berhasil membuat {target.name}: {len(items)} kosakata")
