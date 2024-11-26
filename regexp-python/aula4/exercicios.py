# 1. Contar Vogais em uma String
# Escreva uma função que conte o número de vogais em uma string fornecida.
import re

string = "Olá, como vai você?"
vocals = 'aeiouáéíóúâêîôûãõ'

# Expressão regular que busca por todas as vogais com ou sem acento, incluindo os acentos circunflexos e til.
pattern = re.findall(fr'[{vocals.lower()}]', string.lower())

# Contando o número de vogais encontradas
vocals_in_string = len(pattern)

print(vocals_in_string)


# 2. Substituir Caracteres Específicos
# Escreva uma função que substitua todos os espaços em branco (' ') 
# em uma string por um caractere específico fornecido.
string = "Eu gosto de programação"
substitute = "_"

pattern = re.sub(r' +', substitute, string)
print(pattern)