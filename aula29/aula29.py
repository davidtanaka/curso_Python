"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu um erro ao executar o programa
"""
numero_str = input('Vou dobrar o numero que você digitar: ')
numero_float = float(numero_str)
try:
     numero_float = float(numero_str)
     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
     print('Isso é um número')

#numero_float = float(numero_str)
#if numero_float.isdigit():
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
#else:
#    print('Isso é um número')