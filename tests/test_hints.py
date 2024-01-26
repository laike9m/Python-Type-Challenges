import re
from pathlib import Path


def test_link(hint_file: Path):
    # Verify if python docs url link to English documentation
    matches = re.findall(
        r"https://docs.python.org/[a-zA-Z]+-?[a-zA-Z]+",
        hint_file.read_text(encoding="utf-8"),
    )
    assert len(matches) == 0
