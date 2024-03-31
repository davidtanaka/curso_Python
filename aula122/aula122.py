# Métodos em instâncias de classes Python
class Carro:
     def __init__(self, nome):
          self.nome = nome

     def acelerar(self):
          print(f'{self.nome} está acelerando')


fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)

# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome = 'Celta')
Carro.acelerar(celta)
# print(celta.nome)
# celta.acelerar()