class Pessoa:
     def __init__(self, nome: str, sobrenome: int) -> None:
          self.nome = nome
          self.sobrenome = sobrenome

     @property
     def nome(self):
          return self._nome
     
     @nome.setter 
     def nome(self, valor):
          self._nome = valor
          
     
     @property
     def sobrenome(self):
          return self._sobrenome
     
     @sobrenome.setter
     def sobrenome(self, idade: int):
          self._idade = idade
          
p1 = Pessoa.nome('Davi')
print(p1)