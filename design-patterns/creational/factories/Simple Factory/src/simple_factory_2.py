"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_customer(self) -> object: pass

class LuxuryCar(Vehicle):
    def get_customer(self) -> None:
        print('Carro de luxo está buscando o cliente.')

class CommonCar(Vehicle):
    def get_customer(self) -> None:
        print('Carro popular está buscando o cliente.')

class Motorcycle(Vehicle):
    def get_customer(self) -> None:
        print('Moto está buscando o cliente.')

class LuxuryMotorcycle(Vehicle):
    def get_customer(self) -> None:
        print('Moto de luxo está buscando o cliente.')

class VehicleFactory:
    def __init__(self, tipo):
        self.car = self.get_car(tipo)

    @staticmethod
    def get_car(tipo: str) -> Vehicle:
        match tipo.lower():
            case 'luxury':
                return LuxuryCar()
            case 'common':
                return CommonCar()
            case 'motorcycle':
                return Motorcycle()
            case 'luxury motorcycle':
                return LuxuryMotorcycle()
        raise ValueError('Esse veículo não existe')
    
    def get_customer(self) -> None:
        self.car.get_customer()


if __name__ == '__main__':
    from random import choice
    cars_available = ['luxury', 'common', 'motorcycle', 'luxury motorcycle']

    for i in range(10):
        car = VehicleFactory(choice(cars_available))
        car.get_customer()
