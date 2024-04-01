# Atríbutos de classe
class Pessoa:
     ano_atual = 2024

     def __init__(self, nome, idade):
          self.nome = nome
          self.idade = idade
          self.ano_atual = 2000

     def get_ano_nascimento(self):
          return Pessoa.ano_atual - self.idade
     

p1 = Pessoa('Davi', 16)
p2 = Pessoa('Mauro', 58)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())