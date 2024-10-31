# from typing import Any

# class Meta(type):
#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         print('CALL é executado')
#         return super().__call__(*args, **kwds)

# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('NEW é executado')
#         return super().__new__(cls)

#     def __init__(self, nome):
#         print('INIT é executado')
#         self.nome = nome

#     def __call__(self, x, y):
#         return f'O call foi chamado {self.nome} {x+y}'
    
# p1 = Pessoa('Davi')
# print(p1(2, 2))
# print(p1.nome)
from typing import Any


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]

class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'Escuro'
        self.font = '20px'

if __name__ == '__main__':
    appsettins1 = AppSettings()
    appsettins1.tema = 'Claro'
    print(appsettins1.tema)

    appsettins2 = AppSettings()
    print(appsettins2.tema)
