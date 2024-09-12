from collections.abc import Iterable

# FromTo is a type alias
FromTo = tuple[str, str]


# changes needs to be an Iterable[FromTo];
def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text


l33t = [("a", "4"), ("e", "3"), ("i", "1"), ("o", "0")]
text = "mad skilled noob powned leet"

assert zip_replace(text, l33t) == "m4d sk1ll3d n00b p0wn3d l33t"
