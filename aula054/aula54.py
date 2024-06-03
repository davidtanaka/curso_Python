"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
"""
from time import sleep

lista_de_compras = ['Banana', 'Uva', 'Maça', 'Arroz', 'Feijão', 'Abacate', 'Bolacha', 'Óleo', 'Vinagre', 'Azeite', 'Whey', 'Café', 'Água']

continuar = True
while continuar:
     continuar = input('Você deseja continuar/começar [S] ou [N] ').upper()
     if continuar == 'N':
          break


     for indice, nome in enumerate(lista_de_compras):
          sleep(0.3)
          print(indice , nome)

     if continuar == 'S': 
          indice_alterar_produto = int(input('Digite o indice do produto que você deseja alterar: '))
          
          int_indice_alterar_produto = int(indice_alterar_produto)
          alterando_produto = input(f'Qual produto voce deseja colocar no lugar de {lista_de_compras[indice_alterar_produto ]}: ')

          lista_de_compras[int_indice_alterar_produto] = alterando_produto 
          print('Veja como ficou a lista: ')
          sleep(1)
          for indice, nome in enumerate(lista_de_compras):
               sleep(0.5)
               print(indice , nome)


print('OBRIGADO, fim de programa')
