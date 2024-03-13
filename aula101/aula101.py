# Exercício - Adiando execução de funções

def soma(x, y):
     return print('O resultado da soma é de: ',x + y)


def multiplica(x, y):
     return print('O resultado da soma é de: ',x * y)


def executa(funcao, *args):
     return funcao(*args)

# Solução professor
def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))


# Minha solução
"""
# Pausando primeira função     
try:
     soma_com_cinco = executa(soma, 5, 1)
except:
     print('Você não digitou o segundo parâmetro para soma.')
     tente_novamente_soma = int(input('Digite o valor de y: '))
     soma_com_cinco = executa(soma, 5, tente_novamente_soma)

# Pausando segunda função 
try:
     multiplica_por_dez = executa(multiplica, 10)
except:
     print('Você não digitou o segundo parâmetro, porfavor tente novamente.')
     tente_novamente_multiplica = int(input('Digite o segundo parametro para ser multiplicado por 10: '))
     multiplica_por_dez = executa(multiplica, 10, tente_novamente_multiplica)"""