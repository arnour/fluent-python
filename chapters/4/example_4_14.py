# function to remove all combining marks

import unicodedata
import string

def shave_marks(txt):
    # Decompose all characters into base characters and combining marks
    norm_txt = unicodedata.normalize('NFD', txt)
    # Filter out all combining marks.
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    # Recompose all characters
    return unicodedata.normalize('NFC', shaved)

def shave_marks_latin(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    preserve = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
        preserve.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(preserve)
    return unicodedata.normalize('NFC', shaved)


order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'

# Only the letters “è”, “ç”, and “í” were replaced
assert shave_marks(order) == '“Herr Voß: • ½ cup of Œtker™ caffe latte • bowl of acai.”'

Greek = 'Ζέφυρος, Zéfiro'

# Both “έ” and “é” were replaced
assert shave_marks(Greek) == 'Ζεφυρος, Zefiro' 

assert shave_marks_latin('ˆßéCafé') == 'ˆßeCafe'
