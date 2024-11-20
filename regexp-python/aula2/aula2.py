# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

text = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'João|Maria|adult..', text)) # O (.) significa qualuquer coisa(caracter)
print(re.findall(r'[Jj]oão|[Mm]aria', text))
print(re.findall(r'[a-zA-Z]oão|[a-zA-Z]aria', text)) # Qualquer letra de A a Z, desse modelo, maiúscula ou minúscula
print(re.findall(r'[a-zA-Z0-9_.]aria|[a-zA-Z0-9]oão', text)) # Qualquer número de 0 a 9

# Esta configuração flag ignora se as letras são maiúsculas ou não.
print(re.findall(r'JoÃo|MaRIa', text, flags=re.IGNORECASE)) 