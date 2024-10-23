from typing import List, Union, Tuple, Dict


# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False | True
string: str = str('Ola mundo')

# dicionários e conjuntos
pessoa: dict[str, str] = {'nome:': 'Davi', 'sobrenome:': 'Tanaka',}
pessoa_str_int: dict[str, str | int] = {'nome:': 'Davi', 'sobrenome:': 'Tanaka', 'idade:': 16}

# Criando meu tipo
user_id: str | None = None
user_id = 'Eu não sei o que falar'
# print(user_id)

# Sequências
# Maneiras mais recomendadas & modernas
lista: list[int] = [1, 2, 3]
lista_str_int: list[int | str] = [1, 2, 3, 'Davi']
tupla: tuple[int, str, int] = (1, 'Davi', 3)

# Funções
def ola_mundo(msg: str):
    return msg

# print(ola_mundo('Hello World'))

def soma(x: int | float, y: int | float):
    return x + y

# print(soma(21, 11.4))

# Classes 
class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int | float = idade

    def fala(self):
        return (f'Olá {self.nome} {self.sobrenome} Esse é seu nome '
            f'E você tem {self.idade} anos.')

pessoa_1 = Pessoa('davi', 'Tanaka', 16)
pessoa_1.fala()

# Maneiras mais antigas para quando a variável pode ter valores diferentes,
# Recomendados apenas para versões 3.8 e anteriores
lista_antiga: List[Union[int, str]] = [1, 2, 3, 'Davi']
tupla_antiga: Tuple[int, str, int] = (1, 'Davi', 3)
dict_pessoa_antiga: Dict[str, Union[str, int]] = {'nome:': 'Davi', 'sobrenome:': 'Tanaka', 'idade:': 16}
