"""
Repetições
whille (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um codigo não tem fim
"""
contador = 0

while contador <= 100:
     contador += 1
     print(contador)

     if contador == 6:
          print('não vou mostrar o 6')

     if contador == 89:
          break

print('Acabou')
