# Problema dos parâmetros mutáveis em Python
def adiciona_clientes(nome, lista=None):
     if lista is None:
          lista = []
     lista.append(nome)
     return lista


cliente1 = adiciona_clientes('Davi')
adiciona_clientes('Tanaka', cliente1)
adiciona_clientes('Mauro', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)