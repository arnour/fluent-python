# From Positional to Keyword-Only Parameters
#  tag generates HTML elements; a keyword-only argument class_ is used
# to pass “class” attributes as a workaround because class is a keyword in Python


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


# A single positional argument produces an empty tag with that name
assert tag("br") == "<br/>"

# Any number of arguments after the first are captured by *content as a tuple
assert tag("p", "hello") == "<p>hello</p>"
assert (
    tag("p", "hello", "world")
    == """<p>hello</p>
<p>world</p>"""
)

# Keyword arguments not explicitly named in the tag signature are captured by **attrs as a dict.
assert tag("p", "hello", id=33) == '<p id="33">hello</p>'

# The class_ parameter can only be passed as a keyword argument
assert (
    tag("p", "hello", "world", class_="sidebar")
    == """<p class="sidebar">hello</p>
<p class="sidebar">world</p>"""
)

# The first positional argument can also be passed as a keyword (name)
assert tag(content="testing", name="img") == '<img content="testing"/>'

# Prefixing the my_tag dict with ** passes all its items as separate arguments,
# which are then bound to the named parameters, with the remaining caught by **attrs.
# In this case we can have a 'class' key in the arguments dict,
# because it is a string, and does not clash with the class reserved word.
my_tag = {
    "name": "img",
    "title": "Sunset Boulevard",
    "src": "sunset.jpg",
    "class": "framed",
}

assert (
    tag(**my_tag) == '<img class="framed" src="sunset.jpg" title="Sunset Boulevard"/>'
)


# To specify keyword-only arguments when defining a function,
# name them after the argument prefixed with *.
# If you don’t want to support variable positional arguments but still want keyword-only arguments,
# put a * by itself in the signature
def f(a, *, b):
    return a, b


assert f(1, b=2) == (1, 2)
try:
    f(1, 2)
    assert False, "It should have raised a TypeError"
except TypeError as err:
    assert str(err) == "f() takes 1 positional argument but 2 were given"


def divmod(a, b, /):
    return (a // b, a % b)


assert divmod(5, 4) == (1, 1)


def tag2(name, /, *content, class_=None, **attrs):
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


# If we want the name parameter to be positional only,
# we can add a / after it in the function signature
assert tag2("img", content="testing") == '<img content="testing"/>'
