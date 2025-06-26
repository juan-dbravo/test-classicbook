import logging
from pathlib import Path
import string

def transform_main():
    logging.info("🔹 Starting transformation...")
    in_path = Path("data/raw/sample.txt")
    out_path = Path("data/clean/cleaned.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    raw_text = in_path.read_text(encoding="utf-8")
    cleaned = raw_text.lower().translate(str.maketrans('', '', string.punctuation))
    out_path.write_text(cleaned, encoding="utf-8")

    logging.info(f"✅ Transformed text saved to {out_path}")
