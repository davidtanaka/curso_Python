# sys.argv - Executando arquivos com argumentos no sistema
import sys

argumentos = sys.argv
qnt_argumentos = len(argumentos)

if qnt_argumentos <= 1:
    print('Você não passou argumentos')
else:
    print(f'Você passou os argumentos {argumentos}')