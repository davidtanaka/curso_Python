# Operadores in e not in
# Strings são interaveis
#  0 1 2 3 4 5
#  T a n a k a
# -6-5-4-3-2-1
#nome = 'Tanaka'
#print(nome[2])
#print(nome[-4])

#print('k' in nome)
#print(10 * '-')
#print('k' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Qual letra você deseja encontrar em seu nome: ')

if encontrar in nome:
     print(f'Encontrei a letra "{encontrar}" em seu nome')
else:
     print(f'A letra "{encontrar}" não esta em seu nome')