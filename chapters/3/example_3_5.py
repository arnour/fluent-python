# Inserting or Updating Mutable Values
import re

WORD_RE = re.compile(r'\w+')

text = """Sou composta por urgências:
minhas alegrias são intensas;
minhas tristezas, absolutas.
Entupo-me de ausências,
Esvazio-me de excessos.
Eu não caibo no estreito,
eu só vivo nos extremos.
Pouco não me serve,
médio não me satisfaz,
metades nunca foram meu forte!
Todos os grandes e pequenos momentos,
feitos com amor e com carinho,
são pra mim recordações eternas.
Palavras até me conquistam temporariamente…
Mas atitudes me perdem ou me ganham para sempre.
Suponho que me entender
não é uma questão de inteligência
e sim de sentir,
de entrar em contato…
Ou toca, ou não toca"""

# Build an index mapping word -> list of occurrences
index = {}

for line_no, line in enumerate(text.split("\n")):
    for match in WORD_RE.finditer(line):
        word = match.group()
        column_no = match.start() + 1
        location = (line_no, column_no)
        index.setdefault(word, []).append(location)

for word in sorted(index, key= str.upper):
    print(word, index[word])