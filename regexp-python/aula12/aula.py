import re
from pprint import pprint

# https://regex101.com/r/DfXYXM/1/
# Minhas soluções (queria pegar todos os números dentro do texto para treinar)
# regexp = re.compile(r'^\([1-9]{2}\)\s?|[0-9]\s|\s+|\S[0-9]\s[0-9]{3}|\s[0-9]{4}|[0-9]{4}-[0-9]{4}$', flags=re.M)
# regexp = re.compile(r'\(?[1-9]{2}\)?\s*-?\s*(\d{4,5})\s*-?\s*(\d{4})|(\d{4}-\d{4}|\d{4}\s\d{4})', flags=re.M)

# Solução professor (Apenas os números válidos)
regexp = re.compile(r'^(?:\(\d{2}\)\s)(?:9\s)(?:\d{4}-\d{4})$', flags=re.M)

text = '''
(21) 9 8852-5214
(11)9955-1231
(11)            9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''
pprint(regexp.findall(text))

for phone_number in regexp.findall(text):
    print(phone_number)
