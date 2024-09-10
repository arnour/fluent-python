# Demo of partial applied to the function tag


def tag(name, *content, class_=None, **attrs):
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs["class"] = class_
    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = "".join(attr_pairs)
    if content:
        elements = (f"<{name}{attr_str}>{c}</{name}>" for c in content)
        return "\n".join(elements)
    else:
        return f"<{name}{attr_str}/>"


import functools

picture = functools.partial(tag, "img", class_="pic-frame")

assert picture(src="wumpus.jpeg") == '<img class="pic-frame" src="wumpus.jpeg"/>'

assert picture.func == tag
assert picture.args == ("img",)
assert picture.keywords == {"class_": "pic-frame"}
