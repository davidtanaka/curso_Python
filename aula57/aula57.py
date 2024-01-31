"""
Lista de lista e seus índices
"""
salas = [
     #  0        1
     ['Maria', 'Davi'], # 0
     #   0
     ['Eliane'], # 1
     #   0       1        2
     ['Luiz', 'João', 'Otávio', (0, 1, 2, 3, 4)] # 2
]

#print(salas[2][2])
#print(salas[2][3][2])

for sala in salas:
     for aluno in sala:
          print(aluno)
