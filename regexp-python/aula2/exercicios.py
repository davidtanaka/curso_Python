# Exercício 1: Encontrar palavras que começam com letras maiúsculas
# Use uma expressão regular para encontrar todas as palavras no texto
# que começam com uma letra maiúscula.

import re

text = """
O sol brilhou forte naquela manhã. Carlos, com sua bicicleta velha, 
pedalava em direção ao parque. Lá, encontrou Ana, que estava lendo 
um livro sobre aventuras. 

“Bom dia, Ana!”, disse ele com um sorriso. Ela respondeu: 
“Bom dia, Carlos! Pronto para mais uma corrida?” 

E assim começaram a competir pelas trilhas, entre risadas e brincadeiras.
"""

# Corrigido para incluir suporte a caracteres acentuados
result = re.findall(r'\b[A-ZÀ-Ú][a-zà-ú]*', text)
print(result)
print()


# Exercício 2: Encontrar palavras que terminam com "ão"
# Use uma expressão regular para encontrar todas as palavras no texto 
# que terminam com "ão". Considere que as palavras podem ser separadas 
# por espaços ou sinais de pontuação como "." ou ",".
# 
# Dica: Lembre-se de usar o metacaractere de fronteira de palavra (\b) 
# para garantir que a busca seja precisa.

text = """
João decidiu ir ao mercado para comprar pão e feijão. 
No caminho, encontrou um amigo que falou sobre a decisão de mudar para o Japão.
A conversa foi tão boa que eles nem perceberam o tempo passar.
"""

# Corrigindo a expressão regular
result = re.findall(r'\b\w*ão\b', text, flags=re.I)
print(result)
