"""
GoF - Memento é um padrão de projeto comportamental
que tem a intenção de permitir que você salve e restaure
um estado anterior de um objeto (Originator) sem revelar os
detalhes da sua implementação e sem violar o encapsulamento.

Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usado para armazenar mementos.
Caretaker também é usado com o Padrão Command.
"""
from copy import deepcopy

# Classe Memento para armazenar o estado do Originator
class Memento:
    def __init__(self, state: dict) -> None:
        # Armazena o estado como um dicionário imutável
        self._state: dict
        super().__setattr__('_state', state)

    def get_state(self) -> dict:
        # Retorna o estado armazenado no memento
        return self._state
    
    def __setattr__(self, name, value):
        # Impede qualquer modificação no estado após a criação do memento
        raise AttributeError("Sorry, I'm imuttable")
    
# Classe Originator que representa o editor de imagem
class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        # Define as propriedades do editor de imagem (estado do objeto)
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        # Salva o estado atual em um novo Memento e retorna
        return Memento(deepcopy(self.__dict__))
    
    def restore(self, memento: Memento) -> None:
        # Restaura o estado a partir de um Memento
        self.__dict__ = memento.get_state()

    def __str__(self):
        # Representação em string do estado atual do objeto
        return f'{self.__class__.__name__}({self.__dict__})'
    
# Classe Caretaker que gerencia o histórico de mementos do Originator
class Caretaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator       # Objeto originator a ser monitorado
        self._mementos: list[Memento] = []  # Lista para armazenar os mementos (histórico de estados)
        
    def backup(self) -> None:
        # Cria um backup do estado atual do originator
        self._mementos.append(self._originator.save_state())
    
    def restore(self) -> None:
        # Restaura o último estado salvo, se disponível
        if not self._mementos:
            return
        self._originator.restore(self._mementos.pop())


# Código principal para testar o padrão Memento
if __name__ == "__main__":
    # Cria um editor de imagem com estado inicial
    img = ImageEditor('FOTO_1.jpg', 111, 111)
    caretaker = Caretaker(img)  # Define o caretaker para monitorar o editor
    caretaker.backup()          # Salva o estado inicial

    # Modifica o estado do editor e salva o novo estado
    img.name = 'FOTO_2.jpg'
    img.width = 222
    img.height = 222
    caretaker.backup()

    # Modifica o estado do editor novamente e salva o novo estado
    img.name = 'FOTO_3.jpg'
    img.width = 333
    img.height = 333
    caretaker.backup()

    # Altera o estado do editor mais uma vez, mas sem salvar o estado
    img.name = 'FOTO_4.jpg'
    img.width = 444
    img.height = 444

    # Restaura o estado anterior duas vezes
    caretaker.restore()
    caretaker.restore()

    print(img)  # Exibe o estado atual do editor após restaurações
