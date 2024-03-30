# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pelas classes podem usar seus dados 
# internos para realizar várias ações.
# por convenção, usamos pascalCase para nomes de 
# classes 
class pessoa:
     def  __init__(self, nome, sobrenome):
          self.nome = nome
          self.sobrenome = sobrenome

p1 = pessoa('Davi', 'Tanaka')
# p1.nome = 'Davi'
# p1.sobrenome = 'Tanaka'

p2 = pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)