# Count occurrences of needles in a haystack, both of type set

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

haystack = set(text.split())

needles = set(['e', 'com', 'vida', 'mais'])

found = len(needles & haystack)

assert found == 2

found = len(set(needles) & set(haystack))

assert found == 2

found = len(set(needles).intersection(haystack))

assert found == 2