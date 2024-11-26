# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação


from re import findall

cpf = '147.85sAd2.963-12'
print(findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(findall(r'[^a-z|A-Z]+', cpf))
print(findall(r'[^0-9]+', cpf))
