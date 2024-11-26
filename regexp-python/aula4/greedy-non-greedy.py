"""
Meta caracteres: ^ $ ( )
* 0 ou n
+ 1 ou n
? 0 ou 1.

Em expressões regulares:
Greedy (guloso): Tenta capturar o máximo possível. Exemplos:

.* pega tudo que puder.
Ex.: Em "<tag>content</tag>", .* captura "<tag>content</tag>".
Non-greedy (não guloso): Tenta capturar o mínimo possível, usando ?.

Exemplo: .*? captura o mínimo para casar.
Em "<tag>content</tag>", .*? captura "<tag>".
Use ? para evitar capturas excessivas!
"""

import re

text = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', text))
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', text))
