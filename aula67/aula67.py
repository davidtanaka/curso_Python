"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja enviado
para o parâmetro, o valor não será usado.
Refatorar: editar o seu codigo
"""


def soma(x, y, z=None):
     if z is not None:
          print(x + y + z)
     else:
          print(y + x)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)