"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que
encapsula a forma como um conjunto de objetos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objetos se refiram uns aos
outros explicitamente e permite variar suas
interações independentemente.
"""
from abc import ABC, abstractmethod

# Classe abstrata Colleague, que representa um participante na comunicação mediada
class Colleague(ABC):
    def __init__(self) -> None:
        self.name: str  # Nome do participante, que será definido nas classes derivadas

    @abstractmethod
    def broadcast(self, msg: str) -> None: ...
    # Método abstrato para enviar uma mensagem a todos

    @abstractmethod
    def direct(self, msg: str) -> None: ...
    # Método abstrato para receber uma mensagem direta

# Implementação de um participante específico (Person) que herda de Colleague
class Person(Colleague):
    def __init__(self, name: str, mediator: 'Mediator') -> None:
        self.name = name            # Define o nome do participante
        self.mediator = mediator    # Define o mediador para a comunicação

    def broadcast(self, msg: str) -> None:
        # Envia uma mensagem para todos os participantes através do mediador
        self.mediator.show(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        # Envia uma mensagem direta a um participante específico via mediador
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None:
        # Recebe e exibe uma mensagem direta
        print(msg)

# Classe abstrata Mediator, que define as interações entre os participantes
class Mediator(ABC):
    @abstractmethod
    def show(self, person: Colleague, msg: str) -> None: ...
    # Método abstrato para enviar uma mensagem a todos os participantes

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None: ...
    # Método abstrato para enviar uma mensagem direta de um participante para outro


# Implementação do Mediator para uma sala de bate-papo (Chatroom)
class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: list[Colleague] = []  # Lista de participantes na sala

    def is_colleague(self, colleague: Colleague) -> bool:
        # Verifica se um participante já está na sala
        return colleague in self.colleagues
    
    def add(self, colleague: Colleague) -> None:
        # Adiciona um participante à sala se ele ainda não estiver presente
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        # Remove um participante da sala se ele estiver presente
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def show(self, colleague: Colleague, msg: str) -> None: 
        # Exibe uma mensagem para todos os participantes da sala
        if not self.is_colleague(colleague):  # Ignora se o participante não estiver na sala
            return
        print(f'{colleague.name} Escreveu {msg}')

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        # Envia uma mensagem direta de um participante para outro
        if not self.is_colleague(sender):  # Ignora se o remetente não estiver na sala
            return

        # Encontra o destinatário na lista de participantes
        receiver_obj: list[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        if not receiver_obj:  # Ignora se o destinatário não foi encontrado
            return

        # Envia a mensagem direta ao primeiro destinatário encontrado
        receiver_obj[0].direct(f'{sender.name} para {receiver_obj[0].name}: {msg}')


# Código principal para testar o comportamento do Mediator e Colleagues
if __name__ == '__main__':
    chat = Chatroom()  # Instancia a sala de bate-papo

    # Cria participantes e os adiciona à sala
    joao = Person('João', chat)
    maria = Person('Maria', chat)
    elis = Person('Elis', chat)
    jose = Person('José', chat)

    chat.add(joao)
    chat.add(maria)
    chat.add(elis)
    chat.add(jose)

    # João e Maria enviam mensagens para todos na sala
    joao.broadcast('Olá pessoas')
    maria.broadcast('Fala, beleza?')
    
    # José tenta enviar uma mensagem sem ter sido adicionado à sala (sem efeito)
    jose.broadcast('Eu não fui adicionado ao chat...')

    print()

    # Mensagens diretas entre João e Maria
    joao.send_direct('Maria', 'Oi Maria, tudo bem?')
    maria.send_direct('João', 'Bem e você?')
