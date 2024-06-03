primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')
if primeiro_valor > segundo_valor:
     print(f'O primeiro numero = {primeiro_valor} é maior que o segundo valor ={segundo_valor}')
elif segundo_valor > primeiro_valor:
     print(f'O segundo numero = {segundo_valor} é maior que o primeiro valor ={primeiro_valor}')
else:
     print(f'Os numeros são iguais primeiro numero = {primeiro_valor}, e o segundo numero = {segundo_valor}')
print('Fim....')