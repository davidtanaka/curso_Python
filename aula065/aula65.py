"""
Introdução às funções (def) em python
Funções são trechos de código usado para
replicar determinada ação ao longo do código
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico
por padrão, funções python retornam None (nada)
"""
#def imprimir(a, b, c):
#     print(a, b, c)

#imprimir(6, 3, 8)

def hello(name):
     print(f'Hi {name}')

hello(name = input('Type your name: '))
