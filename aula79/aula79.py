# Exemplo de uso de sets
letras = set()
while True:
     letra= input('Digite: ')
     letras.add(letra.upper())

     print(letras)
     if 'd' in letras:
          print('Parabéns')
          break

