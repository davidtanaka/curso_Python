# uma_string: str = 'Um valor'
# um_inteiro: int = 123
# um_float: float = 22.5
# um_booleano: bool = True
# um_set: set = {1, 2, 3} # Mais sobre a seguir
# uma_lista: list = [] # Mais sobre a seguir
# uma_tuple: tuple = () # Mais sobre a seguir
# um_dicionario: dict = {} # Mais sobre a seguir

# def soma(x: int, y: int, z: float) -> float:
#     return x + y + z

# lista_inteiros: list[int] = [1, 2, 3, 4]
# lista_string: list[str] = ["A", "B", "c"]
# lista_tuplas: list[tuple] = [("A", 1, 2), (3, 4)]
# lista_listas_int: list[list[int]] = [[1], [2], [ 3, 4]]

# um_dict: dict[str, int] = {
#     "A": 2,
#     "2": 2,
#     "B": 4,
# }

# um_dict_de_listas: dict[str, list[int]] = {
#     "A": [ 2, 6, 5, 3, 1],
#     "2": [2, 3, 4],
#     "B": [4, 1234],
# }

# um_set_de_inteiros: set[int] = {1, 2, 3}

# ListaInteiros = list[int]
# DictListaInteiros = dict[str, ListaInteiros]

# um_dict: DictListaInteiros = {
#     "A": [ 2, 6, 5, 3, 1],
#     "2": [2, 3, 4],
#     "B": [4, 1234],
# }

# string_e_inteiros: str | int = 1 # Union
# string_e_inteiros = "A" # Sem erros
# string_e_inteiros = 2 # Sem erros
# lista: list[int | str] = [1, 2, 3, 'Str']

# def soma(x: int, y: float | None = None) -> float:
#     if isinstance(y, float | int):
#         return x + y
#     return x + x

# from collections.abc import Callable

# SomaInteiros = Callable[[int, int], int]

# def executa(func: SomaInteiros, a: int, b: int) -> int:
#     return func(a, b)

# def soma(a: int, b: int) -> int:
#     return a + b

# executa(soma, 1, 2)

# from typing import TypeVar

# T = TypeVar('T')

# def get_item(list: list[T], index: int) -> T:
#     return list[index]

# list_int = get_item([1, 2, 3], 1) # int
# list_str = get_item(['a', 'b', 'c'], 1)

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return self.firstname + ' ' + self.lastname
    
def say_my_name(person: Person) -> str:
    return person.full_name

print(say_my_name(Person('Davi', 'Tanaka')))
