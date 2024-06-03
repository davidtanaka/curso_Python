# Manipulando chaves e valores em dicionarios
pessoa = {}

chave = 'nome'

pessoa[chave] = 'Davi'
pessoa['sobrenome'] = 'Tanaka'

print(pessoa[chave])

pessoa[chave] = 'Maria'


del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome))
if pessoa.get('sobrenome') is None:
     print('Não existe')
else:
     print(pessoa['sobrenome'])

# print('ISSo não vai)
