"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como os proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from abc import ABC, abstractmethod
from time import sleep

# Interface do usuário que define os métodos obrigatórios
class IUser(ABC):
    # Atributos firstname e lastname que devem ser implementados pelas classes concretas
    firstname: str
    lastname: str

    # Método abstrato para obter endereços, deve retornar uma lista de dicionários
    @abstractmethod
    def get_addresses(self) -> list[dict]: ...

    # Método abstrato para obter todos os dados do usuário, deve retornar um dicionário
    @abstractmethod
    def get_all_user_data(self) -> dict: ...

# Classe RealUser que representa o objeto real e implementa a interface IUser
class RealUser(IUser):
    # Construtor que recebe o nome e sobrenome e os armazena nos atributos
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    # Implementação do método get_addresses, com uma simulação de atraso (2 segundos)
    def get_addresses(self) -> list[dict]: 
        sleep(2)  # Simula uma operação demorada
        return [{'Rua': 'Av. Brasil', 'numero': 500}]

    # Implementação do método get_all_user_data, com uma simulação de atraso (2 segundos)
    def get_all_user_data(self) -> dict: 
        sleep(2)  # Simula uma operação demorada
        return {'cpf': '123.456.678-91', 'rg': 'AB122434'}

# Classe UserProxy que representa o proxy para RealUser e também implementa a interface IUser
class UserProxy(IUser):
    # Construtor que inicializa o proxy com o nome e sobrenome
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
         
        # Inicialmente, o objeto RealUser e os dados em cache não existem
        self._real_user: RealUser
        self._cached_addresses: list[dict]
        self._all_user_data: dict

    # Método para instanciar RealUser apenas quando necessário
    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    # Método para obter endereços; usa o cache se já tiver os dados
    def get_addresses(self) -> list[dict]:
        # Garante que o objeto RealUser seja instanciado
        self.get_real_user()

        # Carrega o cache se ainda não tiver os endereços
        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()
        
        # Retorna o endereço do cache
        return self._cached_addresses

    # Método para obter todos os dados do usuário; usa o cache se já tiver os dados
    def get_all_user_data(self) -> dict:
        # Garante que o objeto RealUser seja instanciado
        self.get_real_user()

        # Carrega o cache se ainda não tiver todos os dados do usuário
        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()
        
        # Retorna todos os dados do cache
        return self._all_user_data
    

# Bloco de execução principal
if __name__ == "__main__":
    # Cria um proxy para o usuário 'Davi Tanaka'
    davi = UserProxy('Davi', 'Tanaka')

    # Acessa o primeiro nome e sobrenome rapidamente (sem interação com o RealUser)
    print(davi.firstname)
    print(davi.lastname)

    # Acessa dados que precisam de 2 segundos para serem carregados (simulando operações caras)
    print(davi.get_all_user_data())
    print(davi.get_addresses())

    # Acessa o cache repetidamente (agora é rápido pois já foi carregado uma vez)
    print('CACHED DATA:')
    for i in range(50):
        print(davi.get_addresses())
