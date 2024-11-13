"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalhem em conjunto
através de um "adaptador".
"""
from abc import ABC, abstractmethod


# Interface IControl define métodos para movimentos em diferentes direções
class IControl(ABC):
    @abstractmethod
    def top(self) -> None: ...

    @abstractmethod
    def right(self) -> None: ...

    @abstractmethod
    def down(self) -> None: ...

    @abstractmethod
    def left(self) -> None: ...


# Classe Control implementa IControl, seguindo a interface padrão de controle
class Control(IControl):
    def top(self) -> None:
        print('Movendo para cima...')

    def right(self) -> None:
        print('Movendo para direita...')

    def down(self) -> None:
        print('Movendo para baixo...')

    def left(self) -> None:
        print('Movendo para esquerda...')


# Classe NewControl possui métodos com uma interface diferente de IControl
class NewControl:
    def move_top(self) -> None:
        print('New Control - Movendo para cima...')

    def move_right(self) -> None:
        print('New Control - Movendo para direita...')

    def move_down(self) -> None:
        print('New Control - Movendo para baixo...')

    def move_left(self) -> None:
        print('New Control - Movendo para esquerda...')


# Classe ControlAdapter atua como adaptador entre NewControl e IControl
class ControlAdapter(IControl):
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        # Adapta o método top() para usar o método move_top() de NewControl
        self.new_control.move_top()

    def right(self) -> None:
        # Adapta o método right() para usar o método move_right() de NewControl
        self.new_control.move_right()

    def down(self) -> None:
        # Adapta o método down() para usar o método move_down() de NewControl
        self.new_control.move_down()

    def left(self) -> None:
        # Adapta o método left() para usar o método move_left() de NewControl
        self.new_control.move_left()


# Classe ControlAdapter2 herda de Control e NewControl
# e implementa IControl usando métodos de NewControl
class ControlAdapter2(Control, NewControl):
    def top(self) -> None:
        self.move_top()  # Usa o método move_top() de NewControl

    def right(self) -> None:
        self.move_right()  # Usa o método move_right() de NewControl

    def down(self) -> None:
        self.move_down()  # Usa o método move_down() de NewControl

    def left(self) -> None:
        self.move_left()  # Usa o método move_left() de NewControl


# Testa a funcionalidade das classes e do adaptador
if __name__ == '__main__':
    # Usando Control, que implementa IControl diretamente
    control_object: IControl = Control()
    control_object.top()
    control_object.down()
    control_object.left()
    control_object.right()

    print()
    
    # Usando NewControl através do adaptador ControlAdapter
    new_control_object = NewControl()
    control_object2: IControl = ControlAdapter(new_control_object)
    control_object2.top()
    control_object2.down()
    control_object2.left()
    control_object2.right()

    print()
    
    # Usando ControlAdapter2 que combina Control e NewControl
    control_class: IControl = ControlAdapter2()
    control_class.top()
    control_class.down()
    control_class.left()
    control_class.right()
