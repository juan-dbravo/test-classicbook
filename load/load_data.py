import logging
from pathlib import Path
from collections import Counter

def load_main():
    logging.info("🔹 Starting loading...")
    in_path = Path("data/clean/cleaned.txt")
    out_path = Path("data/output/frequencies.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    words = in_path.read_text(encoding="utf-8").split()
    freqs = Counter(words)

    out_path.write_text("\n".join(f"{word}: {count}" for word, count in freqs.items()), encoding="utf-8")
    logging.info(f"✅ Word frequencies saved to {out_path}")
