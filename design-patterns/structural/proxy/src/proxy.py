"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
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

class IUser(ABC):
    # Subject Interface

    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> list[dict]: ...

    @abstractmethod
    def get_all_user_data(self) -> dict: ...

class RealUser(IUser):
    # Real Subject
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> list[dict]: 
        sleep(2) 
        return [{'Rua': 'Av. Brasil', 'numero': 500}]

    def get_all_user_data(self) -> dict: 
        sleep(2) 
        return {'cpf': '123.456.678-91', 'rg': 'AB122434'}
    

class UserProxy(IUser):
    # Proxy

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
         
        # Esses objetos ainda não exitem nesse ponto do código
        self._real_user: RealUser
        self._cached_addresses: list[dict]
        self._all_user_data: dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> list[dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()
        
        return self._cached_addresses

    def get_all_user_data(self) -> dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()
        
        return self._all_user_data
    

if __name__ == "__main__":
    davi = UserProxy('Davi', 'Tanaka')

    # Responde instantaneamente
    print(davi.firstname)
    print(davi.lastname)

    # Responde em 6 segundos porque vem do real subject
    print(davi.get_all_user_data())
    print(davi.get_addresses())

    # Responde instantaneamente (porque está em cache)
    print('CACHED DATA:')
    for i in range(50):
        print(davi.get_addresses())