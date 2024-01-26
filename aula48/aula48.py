"""
|Listas em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

"""
#        0   1   2   3   4
lista = [10, 20, 30, 40]
lista.append('Davi')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])"""

"""lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
ultimo_valor = lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, 'Removido', ultimo_valor)
"""
"""#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
#print(bool([]))  # falsy
#print(lista, type(lista))

#        0    1      2              3    4
#       -0   -1     -2             -3   -4
lista = [123, True, 'Davi tanaka', 1.2, []]
lista[-3] = 'David'
print(lista)
print(lista[2], type(lista[2]))"""
