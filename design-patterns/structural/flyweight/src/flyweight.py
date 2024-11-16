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

# A classe `Client` representa o contexto em que o padrão Flyweight será usado.
# Ela mantém os dados extrínsecos, como o número e os detalhes do endereço,
# e utiliza instâncias de `Address` para o estado intrínseco.
class Client(ABC):
    def __init__(self, name) -> None:
        # Nome do cliente
        self.name = name
        # Lista para armazenar os endereços associados ao cliente
        self._addresses: list = []

        # Dados extrínsecos do endereço que variam para cada cliente
        self.address_number: str = ""
        self.address_details: str = ""

    # Método para adicionar um endereço à lista do cliente
    def add_address(self, address: 'Address') -> None:
        self._addresses.append(address)

    # Lista os endereços do cliente, incluindo os dados extrínsecos
    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


# A classe `Address` é o Flyweight. 
# Ela contém o estado intrínseco (rua, bairro, CEP), que é imutável e pode ser compartilhado.
class Address:
    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        # Atributos que compõem o estado intrínseco do endereço
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    # Método para exibir o endereço completo, incluindo os dados extrínsecos
    def show_address(self, address_number: str, address_details: str):
        print(
            f"{self._street}, {address_number}, {self._neighborhood}, "
            f"{address_details}, {self._zip_code}"
        )


# A classe `AddressFactory` é a responsável por gerenciar as instâncias Flyweight.
# Ela garante que endereços com o mesmo estado intrínseco sejam reutilizados.
class AddressFactory:
    # Dicionário para armazenar os objetos Flyweight já criados
    _addresses: dict = {}

    # Método para gerar uma chave única para cada combinação de estado intrínseco
    def _get_key(self, **kwargs) -> str:
        # Combina os valores fornecidos em uma string padronizada (minúsculas e sem espaços extras)
        return ''.join(value.strip().lower() for value in kwargs.values())

    # Método principal para obter ou criar um objeto Flyweight
    def get_address(self, **kwargs) -> Address:
        # Gera uma chave única com base nos argumentos
        key = self._get_key(**kwargs)

        # Se a chave já existe, reutiliza o objeto Flyweight correspondente
        if key in self._addresses:
            print('Usando objeto já criado')
            return self._addresses[key]

        # Caso contrário, cria um novo objeto Flyweight, armazena e retorna
        print('Criando novo objeto')
        address_flyweight = Address(**kwargs)
        self._addresses[key] = address_flyweight
        return address_flyweight


# Código principal para demonstrar o funcionamento do padrão Flyweight
if __name__ == "__main__":
    # Criação da fábrica de endereços
    address_factory = AddressFactory()

    # Criação ou recuperação de objetos Flyweight
    a1 = address_factory.get_address(
        street='Av Brasil',
        neighborhood='Centro',
        zip_code='000000-000'
    )

    a2 = address_factory.get_address(
        street='Av Brasil ',  # Nota: espaço extra será removido
        neighborhood='Centro',
        zip_code='000000-000'
    )

    # Criação do cliente Luiz e adição de endereço
    luiz = Client('Luiz')
    luiz.address_number = '50'
    luiz.address_details = 'Casa'
    luiz.add_address(a1)
    luiz.list_addresses()  # Exibe o endereço completo de Luiz

    # Criação da cliente Joana e adição de endereço
    joana = Client('Joana')
    joana.address_number = '250A'
    joana.address_details = 'AP 555'
    joana.add_address(a2)
    joana.list_addresses()  # Exibe o endereço completo de Joana

    # Comparação dos objetos Flyweight
    # Retornará True, pois `a1` e `a2` compartilham o mesmo estado intrínseco
    print(a1 == a2)
