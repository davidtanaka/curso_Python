""" 
1 - Receber um número inteiro 
2 - Saber se o número é multiplo de 3 e 5:
    Bacon com ovos
3 - Saber  se um número NÃO e multiplo de 3 e 5:
    Passa fome
4 - Saber se o número é multiplo somente de 3:
    Bacon
5 - Sabe se o número é multiplo de 5:
    ovos
"""
def bacon_com_ovos(n):
    assert isinstance(n, int), 'n Deve ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'.strip() # Apenas garantindo qua não tenha espaços indesejados 
    
    if n % 3 == 0:
        return 'Bacon'.strip()
    
    if n % 5 == 0:
        return 'Ovos'.strip()
   
    return 'Passar fome'.strip() # Apenas garantindo qua não tenha espaços indesejados 
