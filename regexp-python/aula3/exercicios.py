"""
Exercícios utilizando meta caracteres em expressões regulares:
^ $ ( )
* 0 ou mais
+ 1 ou mais {1,}
? 0 ou 1
{n} Exatamente n repetições
{min, max} Entre min e max repetições
{10,} 10 ou mais repetições
{,10} Entre 0 e 10 repetições
{10} Exatamente 10 repetições
{5,10} Entre 5 e 10 repetições
()+ Agrupamento
[a-zA-Z0-9]+ Correspondência de letras e/ou números.

Exercício 1: Encontre números
Encontre todos os números no texto.
"""
import re

# Texto para o primeiro exercício
text_numbers = '''
João trouxe flores para sua amada namorada em 10 de janeiro de 1970.
Teve 5 filhos, todos adultos atualmente. Em 2024, a família comemora 50 anos.
'''

# Expressão regular para capturar números
numbers_found = re.findall(r'\d+', text_numbers)
print("Exercício 1 - Números encontrados:", numbers_found)

"""
Exercício 2: Repetição de caracteres
Encontre todas as palavras onde a letra "o" aparece 2 ou mais vezes consecutivas.
"""
# Texto para o segundo exercício
text_repetition = '''
Jooooão comprou ovos e colocou no forno. Depois disse: "Oooooops!"
'''

# Expressão regular para capturar palavras com 'o' repetido 2 ou mais vezes
repeated_o_words = re.findall(r'\b\w*o{2,}\w*\b', text_repetition, flags=re.I)
print("Exercício 2 - Palavras com 'o' repetido:", repeated_o_words)

"""
Exercício 3: Substituição
Substitua todas as palavras que começam com "Jo" (como João, Jonas, Joana) por "Ana".
"""
# Texto para o terceiro exercício
text_substitution = '''
João e Jonas são amigos. Joana não gosta de jogar cartas com eles.
'''

# Expressão regular para substituir palavras que começam com 'Jo' por 'Ana'
substituted_text = re.sub(r'\bJo[a-zA-Z]+\b', 'Ana', text_substitution)
print("Exercício 3 - Texto com substituições:", substituted_text)

