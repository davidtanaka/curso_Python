"""
Retorno das funções (return)
"""


def soma(x, y):
     if x > 10:
          return 10
     print(x + y)
     return x + y


soma1 = soma(2, 3)
soma2 = soma(11, 9)
soma(soma1, soma2)