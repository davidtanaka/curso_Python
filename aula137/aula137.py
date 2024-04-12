# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

# Solução professor
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)



# Minha solução
"""class Carro:
     def __init__(self, modelo_carro):
          self.modelo_carro = modelo_carro

     def carro(modelo_carro):
          return f'O seu carro é {modelo_carro}'


     class Motor:
          def __init__(self, modelo_motor):
               self.modelo_motor = modelo_motor

          def motor(modelo_motor):
               return f'O motor é {modelo_motor}'
          
          class Fabricante:
               def __init__(self, modelo_carro, modelo_motor, _fabricante):
                    self.modelo_motor = modelo_motor
                    self.modelo_carro = modelo_carro
                    self._fabricante = _fabricante

               def fabricante(modelo_carro, modelo_motor, _fabricante):
                    return f'{modelo_carro} tem motor {modelo_motor} e é da fabricante {_fabricante}'

     
c1 = Carro.Motor.Fabricante.fabricante('celta', 'V10', 'Chevrolet')
print(c1)
# c2 = Carro.carro('celta')
# print(c2)
# c3 = Carro.Motor.motor('Vhc')
# print(c3)

"""