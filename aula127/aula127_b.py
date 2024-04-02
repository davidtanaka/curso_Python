import json

from aula127 import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
     pessoas = json.load(arquivo)
     p1 = Pessoa(**pessoas[0])
     p2 = Pessoa(**pessoas[2])
     p3 = Pessoa(**pessoas[3])
     p4 = Pessoa(**pessoas[4])
     p5 = Pessoa(**pessoas[5])
     p6 = Pessoa(**pessoas[6])
     
     print(p1.nome, p1.idade)
     print(p2.nome, p2.idade)
     print(p3.nome, p3.idade)
     print(p4.nome, p4.idade)
     print(p5.nome, p5.idade)
     print(p6.nome, p6.idade)
     