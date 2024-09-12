# show_count from messages.py without type hints
# $ mypy chapters/8/example_8_1.py
# $ mypy --disallow-untyped-defs chapters/8/example_8_1.py
# $ mypy  --disallow-incomplete-defs chapters/8/example_8_1.py
# $ pytest chapters/8/example_8_1.py

from pytest import mark


def show_count(count: int, word: str) -> str:
    if count == 1:
        return f"1 {word}"
    count_str = str(count) if count else "no"
    return f"{count_str} {word}s"


@mark.parametrize("qty, expected", [(1, "1 part"), (2, "2 parts")])
def test_show_count(qty, expected):
    got = show_count(qty, "part")
    assert got == expected


def test_show_count_zero():
    got = show_count(0, "part")
    assert got == "no parts"
