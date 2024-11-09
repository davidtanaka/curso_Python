"""
Chain of Responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""
from abc import ABC, abstractmethod
import string

# Classe abstrata que define a interface para os handlers
class Handler(ABC):
    def __init__(self) -> None:
        self.successor: "Handler"  # Sucessor é o próximo handler na cadeia

    # Método abstrato que deve ser implementado pelos handlers concretos
    @abstractmethod
    def handle(self, letter: str) -> str: 
        pass

# Handler para as letras A, B, C
class HandlerABC(Handler):
    def __init__(self, successor: Handler) -> None:
        self.letters: list[str] = ['A', 'B', 'C']  # Letras tratadas por esse handler
        self.successor: Handler = successor  # Sucessor que será chamado caso essa letra não seja tratada
        
    # Implementação do método handle que verifica se a letra pode ser tratada por esse handler
    def handle(self, letter: str) -> str | None:
        if letter.upper() in self.letters:
            return f'HandlerABC: conseguiu tratar o valor {letter.upper()}'
        # Se não for tratada, passa para o próximo handler
        return self.successor.handle(letter)

# Handler para as letras D, E, F
class HandlerDEF(Handler):
    def __init__(self, successor: Handler) -> None:
        self.letters: list[str] = ['D', 'E', 'F']  # Letras tratadas por esse handler
        self.successor: Handler = successor  # Sucessor que será chamado caso essa letra não seja tratada
        
    # Implementação do método handle que verifica se a letra pode ser tratada por esse handler
    def handle(self, letter: str) -> str:
        if letter.upper() in self.letters:
            return f'HandlerDEF: conseguiu tratar o valor {letter.upper()}'
        # Se não for tratada, passa para o próximo handler
        return self.successor.handle(letter)

# Handler para os casos não resolvidos
class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        # Caso a letra não seja tratada por nenhum handler, retorna uma mensagem informando isso
        return f'HandlerUnsolved: não tratou {letter.upper()}'

# Código principal que configura a cadeia de responsabilidade e testa o processamento das letras
if __name__ == '__main__':
    # Configura os handlers em uma cadeia: ABC -> DEF -> Unsolved
    handler_unsolved: Handler = HandlerUnsolved()
    handler_def: Handler = HandlerDEF(handler_unsolved)
    handler_abc: Handler = HandlerABC(handler_def)

    # Testa o processamento de uma letra que será tratada pelo primeiro handler
    print(handler_abc.handle('a'))  # Esperado: HandlerABC que trata 'a'

    print()

    # Testa o processamento de todas as letras do alfabeto a partir de 'a'
    full_alphabet: list[str] = list(string.ascii_lowercase[string.ascii_lowercase.index('a'):])
    for letter in full_alphabet:
        print(handler_abc.handle(letter))  # Esperado: cadeia de handlers tentando tratar cada letra
