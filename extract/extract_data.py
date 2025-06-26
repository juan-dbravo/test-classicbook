import logging
from pathlib import Path

def extract_main():
    logging.info("🔹 Starting extraction...")
    text = "Hello Juan! This is a simulated extract step. Extract step complete."
    out_path = Path("data/raw/sample.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    logging.info(f"✅ Extracted sample text to {out_path}")
