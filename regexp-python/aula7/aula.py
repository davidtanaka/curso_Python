# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\n\t]
# \b -> borda
# \B -> não borda
from re import findall, I, A

text = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de João. Teve_ALGO 5 filhos, todos adultos atualmente.
Maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# Exemplos de expressões regulares com explicação:

# Encontra todas as palavras compostas por letras minúsculas, ignorando maiúsculas por conta da flag I.
# print(findall(r'[a-z]+', text, flags=I))

# Encontra todas as palavras compostas apenas por letras (minúsculas ou maiúsculas).
# print(findall(r'[a-zA-Z]+', text))

# Encontra todas as palavras compostas por letras e números.
# print(findall(r'[a-zA-Z0-9]+', text))

# Essa linha faz a mesma coisa que a anterior, mas inclui caracteres acentuados (como "ó", "ê").
# print(findall(r'[a-zA-Z0-9À-ú]+', text))

# Alternativa mais simples: \w encontra qualquer caractere alfanumérico (inclui letras, números e "_").
# print(findall(r'\w+', text))

# A flag A (ASCII) limita a busca a caracteres não acentuados.
# print(findall(r'\w+', text, flags=A))

# (\d) Encontra todos os números no texto.
# print(findall(r'\d+', text))  # Exemplo: ['10', '1970', '5']

# (\D) Encontra tudo que NÃO é número.
# print(findall(r'\D+', text))  # Exemplo: ['João trouxe    flores para sua amada namorada em ', ...]

# (\s) Encontra espaços em branco, incluindo tabulações e quebras de linha.
# print(findall(r'\s+', text))  # Exemplo: [' ', '    ', ' ', ' ', ...]

# (\S) Encontra tudo que NÃO é espaço em branco.
# print(findall(r'\S+', text))  # Exemplo: ['João', 'trouxe', 'flores', ...]

# (\b) Representa a "borda" de uma palavra. Usado para encontrar palavras que começam ou terminam de forma específica.
# Encontra palavras que começam com "fl".
# print(findall(r'\bfl\w+', text))  # Exemplo: ['flores']

# Encontra palavras que terminam com "e".
# print(findall(r'\w+e\b', text))  # Exemplo: ['flores', 'nome', 'mineira', ...]

# (\B) Representa "não-borda", ou seja, onde NÃO há início ou fim de palavra.
# Exemplos:
# print(findall(r'\Boo', text))  # Encontra "oo" que NÃO está no início ou fim da palavra (como em "Jooooooão").
# print(findall(r'\Bne\b', text))  # Encontra "ne" no meio das palavras, como em "também né!".
