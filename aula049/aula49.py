"""
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Davi', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()
#lista_b = lista_a 

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

"""
for in com listas

lista = ['Davi', 'Claudia', 'Mauro']

for nome in lista:
     print(nome, type(nome))
"""
