"""
Exercício: Usando re.findall, re.search, re.sub
-----------------------------------------------------------
1. Crie uma string que contenha várias palavras repetidas e algumas palavras únicas.

2. Use expressões regulares para:
   a) Encontrar todas as ocorrências de uma palavra específica usando `findall`.
   b) Verificar se uma palavra específica aparece na string usando `search`.
   c) Substituir uma palavra específica por outra usando `sub`.

3. Mostre os resultados de cada operação.

Exemplo de entrada:
string = "Python é ótimo! Python é poderoso. Eu gosto de Python."

Saída esperada:
- Resultado de `search`: <Match object; span=(0, 6), match='Python'>
- Resultado de `findall`: ['Python', 'Python', 'Python']
- Resultado de `sub`: "C++ é ótimo! C++ é poderoso. Eu gosto de C++."
"""
import re

# Sua string de exemplo
string = "Eu estudo python e gosto de python."

# Encontrar todas as ocorrências de 'python'
test_findall = re.findall('python', string)

# Verificar se 'python' aparece na string
test_search = re.search('python', string)

# Substituir 'gosto' por 'AMO'
test_sub = re.sub(r'\bgosto\b', 'AMO', string)  # O \b garante que só 'gosto' inteiro será substituído

print("Resultado de findall:", test_findall)
print("Resultado de search:", test_search.group() if test_search else None)
print("Resultado de sub:", test_sub)
