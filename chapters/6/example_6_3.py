# Identity, Equality, and Aliases

charles = {"name": "Charles L. Dodgson", "born": 1932}

lewis = charles

# lewis is an alias for charles
assert lewis is charles

assert id(lewis) == id(charles)

# Adding an item to lewis is the same as adding an item to charles
lewis['balance'] = 950

assert charles['balance'] == 950