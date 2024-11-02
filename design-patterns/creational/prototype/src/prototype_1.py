"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""
from copy import deepcopy


class StringReprMixin:
    def __str__(self, *args, **kwargs) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'
    
    def __repr__(self) -> str:
        return self.__str__()

class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: list = []

    def add_address(self, address: 'Address') -> None:
        self.addresses.append(address)

    def clone(self) -> 'Person':
        return deepcopy(self)

class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number

if __name__ == '__main__':

    davi = Person('Davi', 'Tanaka')
    endereco_davi = Address('Av. Brasil', '260B')
    davi.add_address(endereco_davi)

    esposa_davi = davi.clone()
    esposa_davi.firstname = '  '

    print(davi)
    print(esposa_davi)