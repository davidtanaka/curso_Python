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

class MonoStateSimple:
    _state: dict = {
        'x': 20,
        'y': 10,
    }

    def __init__(self, nome: None | str = None, sobrenome: None | str = None) -> None:
        self.x = 1 # Apenas para o Linter não ficar dando erro
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome
        if sobrenome is not None:
            self.sobrenome = sobrenome

if __name__ == '__main__':
    m1 = MonoStateSimple(nome='Davi')
    m1.x = 200
    m2 = MonoStateSimple(sobrenome='Tanaka')
    print(m1.__dict__)
    print(m2.__dict__)