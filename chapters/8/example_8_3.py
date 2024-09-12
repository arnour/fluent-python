def show_count(count: int, singular: str, plural: str = "") -> str:
    if count == 1:
        return f"1 {singular}"
    count_str = str(count) if count else "no"
    if not plural:
        plural = singular + "s"
    return f"{count_str} {plural}"


def test_irregular() -> None:
    got = show_count(2, "child", "children")
    assert got == "2 children"
