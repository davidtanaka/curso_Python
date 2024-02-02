"""
Argumentos nomeados e não nomeados em funções python
Argumentos nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
     # definição
     print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

# argumentos não nomeados
soma(1, 2, 3)

# argumentos nomeados
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')
