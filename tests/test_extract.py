from pathlib import Path
from extract.extract_data import extract_main

def test_extract_creates_file():
    extract_main()
    path = Path("data/raw/sample.txt")
    assert path.exists()
    assert "extract" in path.read_text()
