"""
Flyweight é um padrão de projeto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades
de objetos de forma granular.

Só use o Flyweight quanto TODAS as condições
a seguir forem verdadeiras:

- uma aplicação utiliza uma grande quantidade de
objetos;
- os custos de armazenamento são altos por causa
da grande quantidade de objetos;
- a maioria dos estados de objetos podem se tornar
extrínsecos;
- muitos objetos podem ser substituídos por poucos
objetos compartilhados;
- a aplicação não depende da identidade dos objetos.

Importante:
- Estado intrínseco é o estado do objeto que não muda,
esse estado deve estar dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda,
esse estado pode ser movido para fora do objeto
flyweight;

Dicionário:
Intrínseco - que faz parte de ou que constitui a
essência, a natureza de algo; que é próprio de
algo; inerente.
Extrínseco - que não pertence à essência de algo;
que é exterior.
"""

from abc import ABC, abstractmethod

class Client(ABC):
    # Context
    def __init__(self, name) -> None:
        self.name = name
        self._addresses: list = []

        # Estrinsic address data
        self.address_number: str = ""
        self.address_details: str = ""

    def add_address(self, address: 'Address') -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    # Flyweight
    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str):
        print(
            f"{self._street}, {address_number}, {self._neighborhood}, "
            f"{address_details}, {self._zip_code}"
        )


class AddressFactory:
    _addresses: dict = {}

    def _get_key(self, **kwargs) -> str:
        # Padronizando valores para evitar inconsistências nas chaves
        return ''.join(value.strip().lower() for value in kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        if key in self._addresses:
            print('Usando objeto já criado')
            return self._addresses[key]

        print('Criando novo objeto')
        address_flyweight = Address(**kwargs)
        self._addresses[key] = address_flyweight
        return address_flyweight


if __name__ == "__main__":
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='Av Brasil',
        neighborhood='Centro',
        zip_code='000000-000'
    )

    a2 = address_factory.get_address(
        street='Av Brasil ',
        neighborhood='Centro',
        zip_code='000000-000'
    )

    luiz = Client('Luiz')
    luiz.address_number = '50'
    luiz.address_details = 'Casa'
    luiz.add_address(a1)
    luiz.list_addresses()

    joana = Client('Joana')
    joana.address_number = '250A'
    joana.address_details = 'AP 555'
    joana.add_address(a2)
    joana.list_addresses()

    print(a1 == a2)  # True, pois o Flyweight reutiliza o mesmo objeto
