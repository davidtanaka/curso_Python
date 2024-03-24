# reduce - faz a redução de um iterável em um valor 
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]


"""def funcao_do_reduce(acumulador, produto):
     print('ACUMULADDOR', acumulador)
     print('PRODUTO', produto)
     print()
     return acumulador + produto['preco']

"""

total = reduce(
     lambda ac, p: ac + p['preco'],
     produtos,
     0
)

print('TOTAL', total)