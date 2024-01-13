"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')
try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int:.0f} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Que horas são: ')
horario_convertido = float(horario)

if horario_convertido >= 0 and horario_convertido <= 11:
    print(f'Bom dia agora é {horario}')
   
if horario_convertido >= 11 and horario_convertido <= 17:
    print(f'Boa tarde agora é {horario}')
   
if horario_convertido >= 18 and horario_convertido <= 23:
    print(f'Boa noite agora é {horario}')
else:
    print('Não conheço essa hora')
   
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = str(input('Digite seu primeiro nome: '))
letras = len(nome)

if letras <= 4:
     print(f'Seu nome é curto tem apenas {letras} letras')
elif letras >= 5 and letras <= 6:
     print(f'Seu nome é normal tem {letras} letras')
elif letras > 6:
    print(f'Seu nome é muito grande, ele tem {letras}')
