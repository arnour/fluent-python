# Sorting Unicode Text

import locale

my_locale = locale.setlocale(locale.LC_COLLATE, "pt_BR.UTF-8")

fruits = ["caju", "atemoia", "cajá", "açaí", "acerola"]

assert my_locale == "pt_BR.UTF-8"

assert sorted(fruits) == ["acerola", "atemoia", "açaí", "caju", "cajá"]

assert sorted(fruits, key=locale.strxfrm) == [
    "açaí",
    "acerola",
    "atemoia",
    "cajá",
    "caju",
]
