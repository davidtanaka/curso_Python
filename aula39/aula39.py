"""
Interand strigs com while
"""
#       012345678910
nome = 'Davi tanaka' # Iteraveis
tamanho_nome = len(nome)
indice = 0
novo_nome = ''
while indice < len(nome):
     letra = nome[indice]
     novo_nome += f'*{letra}'
     indice += 1

novo_nome += '*'
print(novo_nome)