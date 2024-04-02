# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO =  'D:\\Cursos\\cursoPython\\aula127\\aula127.json'
class Pessoa:
     def __init__(self, nome, idade):
          self.nome = nome
          self.idade = idade 


p1 = Pessoa('Davi', 16)
p2 = Pessoa('Claudia', 43)
p3 = Pessoa('Mauro', 59)
p4 = Pessoa('Maria', 26)
p5 = Pessoa('Bruno', 19)
p6 = Pessoa('Joana', 66)
p7 = Pessoa('Ione', 86)
bd = [vars(p1), vars(p2), vars(p3), vars(p4), vars(p5), vars(p6), vars(p7)]

def fazer_dump():
     with open(CAMINHO_ARQUIVO, 'w') as arquivo:
          json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
     print('Ele é o __main__')
     fazer_dump()