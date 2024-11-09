"""
Chain of Responsibility (COR) é um padrão comportamental que tem a intenção 
de evitar o acoplamento do remetente de uma solicitação ao seu receptor, 
ao dar a mais de um objeto a oportunidade de tratar a solicitação.
"""

import string
from typing import Optional, Callable

# Tipo para uma função handler que recebe uma letra e retorna uma string
HandlerFunction = Callable[[str], str]

# Handler para letras A, B e C
def handler_ABC(letter: str) -> str:
    """
    Trata letras A, B e C.
    
    Args:
    letter (str): Letra a ser tratada.
    
    Returns:
    str: Mensagem de tratamento bem-sucedido ou resultado do próximo handler.
    """
    letters = ['A', 'B', 'C']
    if letter.upper() in letters:
        return f'handler_ABC: conseguiu tratar o valor {letter}'
    return handler_DEF(letter)  # Passa para o próximo handler

# Handler para letras D, E e F
def handler_DEF(letter: str) -> str:
    """
    Trata letras D, E e F.
    
    Args:
    letter (str): Letra a ser tratada.
    
    Returns:
    str: Mensagem de tratamento bem-sucedido ou resultado do próximo handler.
    """
    letters = ['D', 'E', 'F']
    if letter.upper() in letters:
        return f'handler_DEF: conseguiu tratar o valor {letter}'
    return handler_GHI(letter)  # Passa para o próximo handler

# Handler para letras G, H e I
def handler_GHI(letter: str) -> str:
    """
    Trata letras G, H e I.
    
    Args:
    letter (str): Letra a ser tratada.
    
    Returns:
    str: Mensagem de tratamento bem-sucedido ou resultado do próximo handler.
    """
    letters = ['G', 'H', 'I']
    if letter.upper() in letters:
        return f'handler_GHI: conseguiu tratar o valor {letter}'
    return handler_all_others(letter)  # Passa para o próximo handler

# Handler para todas as letras restantes do alfabeto
def handler_all_others(letter: str) -> str:
    """
    Trata todas as letras restantes do alfabeto.
    
    Args:
    letter (str): Letra a ser tratada.
    
    Returns:
    str: Mensagem de tratamento bem-sucedido ou resultado do próximo handler.
    """
    letters = list(string.ascii_lowercase[string.ascii_lowercase.index('i'):])
    if letter.lower() in letters:
        return f'handler_all_others: conseguiu tratar o valor {letter}'
    return handler_unsolved(letter)  # Passa para o próximo handler

# Handler final para letras não tratadas
def handler_unsolved(letter: str) -> str:
    """
    Trata letras não tratadas pelos handlers anteriores.
    
    Args:
    letter (str): Letra a ser tratada.
    
    Returns:
    str: Mensagem de tratamento não bem-sucedido.
    """
    return f'handler_unsolved: não sei tratar {letter}'

if __name__ == '__main__':
    print(handler_ABC('4'))  # Testa o handler com uma letra não tratada
    
    # Testa o handler com todas as letras do alfabeto
    full_alphabet = list(string.ascii_lowercase[string.ascii_lowercase.index('a'):])
    for letter in full_alphabet:
        print(handler_ABC(letter))