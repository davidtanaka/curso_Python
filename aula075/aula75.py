"""
Exercicios
Crie funções que duplicam, triplicam e quadripliquem
o numero enviado como parâmetro
"""

# My solution
def multiplication():
     number = float(input('Digite um numero: '))
     return number * 2
#print(multiplication())

def tripled():
     number = float(input('Digite um numero: '))
     return number * 3
#print(tripled())

def quadruple():
     number = float(input('Digite um numero: '))
     return number * 4
print(quadruple())


# Teacher solution
def creater_multiplication(multiplication):
     def multiply(number):
          return number * multiplication
     return multiply

duplicar = creater_multiplication(2)
triple = creater_multiplication(3)
quadrupl = creater_multiplication(4)

print(duplicar)
print(triple)
print(quadrupl)