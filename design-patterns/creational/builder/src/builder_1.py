"""
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos
(method chaining).
"""

from abc import ABC, abstractmethod

class StringReprMixin:
    def __str__(self, *args, **kwargs) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'
    
    def __repr__(self) -> str:
        return self.__str__()

class User(StringReprMixin):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.addresses = []
        self.phonenumbers = []

class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): ...

    @abstractmethod
    def add_firstname(self, firstaname): ...

    @abstractmethod
    def add_lastname(self, lastaname): ...

    @abstractmethod
    def add_age(self, age): ...

    @abstractmethod
    def add_phone(self, phone): ...

    @abstractmethod
    def add_address(self, address): ...


class UserBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self): 
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname): 
        self._result.firstname = firstname

    def add_lastname(self, lastname):
        self._result.lastname = lastname

    def add_age(self, age):
        self._result.age = age

    def add_phone(self, phone):
        self._result.phonenumbers.append(phone)

    def add_address(self, address):
        self._result.addresses.append(address)

class UserDirector:
    def __init__(self, builder):
        self._builder = builder

    def with_age(self, firstname, lastname, age):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname) 
        self._builder.add_age(age) 
        return self._builder.result

    def with_address(self, firstname, lastname, age, address):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname) 
        self._builder.add_age(age) 
        self._builder.add_address(address) 
        return self._builder.result

    def with_phone_all(self, firstname, lastname, age, address, phone):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname) 
        self._builder.add_age(age) 
        self._builder.add_address(address)
        self._builder.add_phone(phone)
        return self._builder.result

if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Davi', 'Tanaka', 16)
    user2 = user_director.with_address('Davi', 'Tanaka', 16, 'Rua: eu Não sei 210')
    user3 = user_director.with_phone_all('Davi', 'Tanaka', 16, 'Rua: eu Não sei 210', 1198949873)
    print(user1)
    print(user2)
    print(user3)