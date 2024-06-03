frase = 'aaaooo'

i = 0
qntd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
letra_mais_vezes = ''
while i < len(frase): 
     letra_atual = frase[i]

     if letra_atual == ' ':
          i += 1
          continue

     qntd_atual = frase.count(letra_atual)
     
     if qntd_apareceu_mais_vezes < qntd_atual:
          qntd_apareceu_mais_vezes = qntd_atual
          letra_apareceu_mais_vezes = letra_atual
      
     i += 1
     
print(f'A letra quue aparecweu mais vezes foi a letra {letra_apareceu_mais_vezes.upper()} que apareceu {qntd_apareceu_mais_vezes} vezes')
