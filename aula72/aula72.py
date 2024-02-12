# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiplication(*args):
     final_result = 1 
     for number in args:
          final_result *= number
     return final_result
     
#print(multiplication(2, 2, 2))

def even_or_odd():
     user_number = input('Type a number: ')
     user_number_without_pontuation = user_number.replace('.', '').replace(',', '')
     user_number_without_pontuation_int = int(user_number_without_pontuation)
     if user_number_without_pontuation_int % 2 == 0:
          return print(f'Your number {user_number} is EVEN')
     else:
          print('YOU ARRIVED IN THE END, THANK YOU')
          return print(f'Your number {user_number} is ODD')

even_or_odd()
