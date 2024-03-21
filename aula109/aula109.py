# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def p(parametro):
     print(*list(parametro), sep ='\n')

pessoas = [
     'joão', 'Davi', 'Claudia', 'Mauro'
]


camisetas = [
     ['preta', 'branca'],
     ['p', 'm', 'g'],
     ['masculino', 'Feminino', 'Unisex'],
     ['Algodão', 'Poliéster'],
]

p(combinations(pessoas, 2))
p(permutations(pessoas, 2))
p(product(*camisetas))