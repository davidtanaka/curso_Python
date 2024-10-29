"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_customer(self) -> object: ...

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
    def get_car(tipo: str) -> Vehicle: ...
    
    def get_customer(self) -> None:
        self.car.get_customer()

class VehicleNorthZonefactory(VehicleFactory):
    @staticmethod
    def get_car(tipo: str) -> Vehicle:
        match tipo.lower():
            case 'luxury car':
                return LuxuryCar()
            case 'common car':
                return CommonCar()
            case 'motorcycle':
                return Motorcycle()
            case 'luxury motorcycle':
                return LuxuryMotorcycle()
        raise ValueError('Esse veículo não existe')


class VehicleSouthZonefactory(VehicleFactory):
    @staticmethod
    def get_car(tipo: str) -> Vehicle:
        match tipo.lower():
            case 'common car':
                return CommonCar()
            case 'motorcycle':
                return Motorcycle()
        raise ValueError('Esse veículo não existe obs(no momento só temos carros comuns)')

if __name__ == '__main__':
    from random import choice
    vehicles_available_north_zone = ['luxury car', 'common car', 'motorcycle', 'luxury motorcycle']
    vehicles_available_south_zone = ['common car', 'motorcycle']

    for i in range(10):
        car = VehicleNorthZonefactory(choice(vehicles_available_north_zone))
        car.get_customer()

    print()

    for i in range(10):
        car_2 = VehicleSouthZonefactory(choice(vehicles_available_south_zone))
        car_2.get_customer()
