# Excrcício - sistema de perguntas e respostas


resposta_certa = perguntas_totais = 0 
perguntas = [
     {
          'Pergunta': 'Quanto é 2+2?',
          'Opções': ['1', '3', '4', '5'],
          'Resposta': '4',
     },
     {
          'Pergunta': 'Quanto é 5*5?',
          'Opções': ['25', '55', '10', '51'],
          'Resposta': '25',
     },
     {
          'Pergunta': 'Quanto é 10/2?',
          'Opções': ['4', '5', '2', '1'],
          'Resposta': '5',
     },
]

# Primeira questão
print(perguntas[0]['Pergunta'] )
alternativas = (perguntas[0]['Opções'])
for alternativa in alternativas:
     print(alternativa)

resposta_sesao_1 = input('Digite uma das opções: ')
perguntas_totais += 1

if resposta_sesao_1 == perguntas[0]['Resposta']:
     resposta_certa += 1
     print('ACERTOUUUU')
     print()
else:
     print('Errou')
     print()

# Segunda questão
print(perguntas[1]['Pergunta'] )
alternativas = (perguntas[1]['Opções'])
for alternativa in alternativas:
     print(alternativa)

resposta_sesao_1 = input('Digite uma das opções: ')
perguntas_totais += 1

if resposta_sesao_1 == perguntas[1]['Resposta']:
     resposta_certa += 1
     print('ACERTOUUUU')
     print()
else:
     print('Errou')
     print()


# terceira questão
print(perguntas[2]['Pergunta'] )
alternativas = (perguntas[2]['Opções'])
for alternativa in alternativas:
     print(alternativa)

resposta_sesao_1 = input('Digite uma das opções: ')
perguntas_totais += 1

if resposta_sesao_1 == perguntas[2]['Resposta']:
     resposta_certa += 1
     print('ACERTOUUUU')
     print()
else:
     print('Errou')
     print()
     
print(f'Você acertou {resposta_certa} de {perguntas_totais}')