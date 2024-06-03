"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""cpf = str(input('Digite seu cpf: '))

# Deixando o cpf sem pontuação para calculos

cpf_limpo = cpf.replace('.', '').replace('-','')


# variavel com numeros em int
cpf_numerado = []

for a in cpf_limpo:
     a = int(a)
     cpf_numerado.append(a)


tamanho = True
valido_ou_invalido = True
if len(cpf_limpo) > 11 or len(cpf_limpo) < 11:
     tamanho = False
else:
     acumulador = 0
     resultado = 0
     controlador = 10
     for numeros in cpf_numerado[0:9]:
          resultado = numeros * controlador
          acumulador += resultado
          controlador = controlador - 1
     aumulador = acumulador *10 % 11
     if acumulador == 10:
          acumulador = 0
     if acumulador == cpf_numerado[9]:
          valido_ou_invalido = True
     else:
          valido_ou_invalido = False

     
tamanho = True
if len(cpf_limpo) > 11 or len(cpf_limpo) < 11:
     tamanho = False
else:
     acumulador2 = 0
     resultado2 = 0
     controlador2 = 11
     for numeros in cpf_numerado[0:10]:
          resultado2 = numeros * controlador2
          acumulador2 += resultado2
          controlador2 = controlador2 - 1
     aumulador = acumulador2 *10 % 11
     if acumulador2 == 10:
          acumulador2 = 0
     if acumulador2 == cpf_numerado[9]:
          valido_ou_invalido = True
     else:
          valido_ou_invalido = False
if valido_ou_invalido and tamanho:
     print('CPF válido')
else:
     print('CPF inválido')
"""