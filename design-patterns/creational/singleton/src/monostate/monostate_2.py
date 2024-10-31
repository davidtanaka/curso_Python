"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""
class StringReprMixin:
    def __str__(self, *args, **kwargs) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'
    
    def __repr__(self) -> str:
        return self.__str__()

class MonoState:
    _state: dict = {
        'x': 20,
        'y': 10,
    }

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome: None | str = None, sobrenome: None | str = None) -> None:
        if nome is not None:
            self.nome = nome
        if sobrenome is not None:
            self.sobrenome = sobrenome

class A(MonoState):
    pass

if __name__ == '__main__':
    m1 = MonoState(nome='Davi')
    m2 = A(sobrenome='Tanaka')
    print(m1.__dict__)
    print(m2.__dict__)