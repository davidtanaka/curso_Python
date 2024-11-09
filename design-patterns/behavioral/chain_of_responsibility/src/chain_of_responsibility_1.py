"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""

# Implementando com fuções (Apenas lógica)
import string

def handler_ABC(letter: str) -> str:
    letters = ['A', 'B', 'C']

    if letter.upper() in letters:
        return f'handler_ABC: conseguio tratar o valor {letter}'
    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = ['D', 'E', 'F']

    if letter.upper() in letters:
        return f'handler_DEF: conseguio tratar o valor {letter}'
    return handler_GHI(letter)


def handler_GHI(letter: str) -> str:
    letters = ['G', 'H', 'I']

    if letter.upper() in letters:
        return f'handler_GHI: conseguio tratar o valor {letter}'
    return handler_all_others(letter)


def handler_all_others(letter: str) -> str:
    letters = list(string.ascii_lowercase[string.ascii_lowercase.index('i'):])

    if letter.lower() in letters:
        return f'handler_all_others: conseguio tratar o valor {letter}'
    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
    return f'handler_unsolved: não sei tratar {letter}'


if __name__ == '__main__':
    print(handler_ABC('4'))
    full_alphabet = list(string.ascii_lowercase[string.ascii_lowercase.index('a'):])
    
    for letter in full_alphabet:
        print(handler_ABC(letter))

