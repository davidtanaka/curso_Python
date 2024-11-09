"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""
from abc import ABC, abstractmethod
import string

class Handler(ABC):
    def __init__(self) -> None:
        self.successor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: ...

class HandlerABC(Handler):
    def __init__(self, successor) -> None:
        self.letters = ['A', 'B', 'C']
        self.successor = successor
        
    def handle(self, letter: str) -> str | None:
        if letter.upper() in self.letters:
            return f'HandlerABC: conseguio tratar o valor {letter.upper()}'
        return self.successor.handle(letter)
    
class HandlerDEF(Handler):
    def __init__(self, successor) -> None:
        self.letters: list[str] = ['D', 'E', 'F']
        self.successor = successor
        
    def handle(self, letter: str) -> str:
        if letter.upper() in self.letters:
            return f'HandlerDEF: conseguio tratar o valor {letter.upper()}'
        return self.successor.handle(letter)
    
class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'HandlerUnsolved: não tratou {letter.upper()}'

if __name__ == '__main__':
    handler_unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)
    print(handler_abc.handle('a'))

    print()

    full_alphabet = list(string.ascii_lowercase[string.ascii_lowercase.index('a'):])
    for letter in full_alphabet:
        print(handler_abc.handle(letter))

