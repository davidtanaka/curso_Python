nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

espacos = 0
if ' ' in nome:
     espacos = True

letras = len(nome) - espacos
ultima_letra = int((len(nome) - 1) + 1)
penultima_letra = int(len(nome) - 1)
if nome and idade != '':
     print(f'Seu nome é {nome}')
     print(f'Seu nome invertido é {nome[::-1]}')
     print(f'Seu nome contem {espacos} espaços')
     print(f'Seu nome tem {letras} letras')
     print(f'A primeira letra  do seu nome é {nome[0:1]}')
     print(f'A ultima letra do seu nome é {nome[penultima_letra:ultima_letra]}')
elif nome or idade == '': 
     print('NADA DIGITADO, PORFAVOR TENTE NOVAMENTE (DIGITE ALGO)')