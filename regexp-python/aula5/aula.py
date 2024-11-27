# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3
from re import findall, sub
from pprint import pprint

text = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''
cpf = '132.758.138-84'

# pprint(findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))


tags = findall(r'(<([pdiv]{1,3})>(.+?)<\/\2>)', text)
# tags = findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', text)
pprint(tags)

print(sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', text))

# for tag in tags:
#     um, dois, tres = tag
#     pprint(tres)
