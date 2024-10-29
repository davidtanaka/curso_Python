"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.

Princípio: programe para interfaces, não para implementações
"""

from abc import ABC, abstractmethod
from typing import List

# Interface para veículos de luxo
class LuxuryVehicle(ABC):
    @abstractmethod
    def get_customer_luxury(self) -> None:
        """Método abstrato que deve ser implementado por veículos de luxo para buscar clientes."""
        pass

# Interface para veículos comuns
class CommonVehicle(ABC):
    @abstractmethod
    def get_customer_common(self) -> None:
        """Método abstrato que deve ser implementado por veículos comuns para buscar clientes."""
        pass

# Classe base para veículos, fornece um método para padronizar a saída de mensagens
class VehicleBase:
    def _print_message(self, vehicle_type: str, zone: str) -> None:
        """
        Exibe uma mensagem indicando que o veículo está buscando o cliente.
        
        Args:
            vehicle_type (str): Tipo de veículo (ex.: 'Carro de luxo').
            zone (str): Zona geográfica do veículo (ex.: 'NZ').
        """
        print(f"{vehicle_type} {zone} está buscando o cliente.")

# Implementações concretas de veículos para a zona norte (NZ)
class LuxuryCarNZ(LuxuryVehicle, VehicleBase):
    def get_customer_luxury(self) -> None:
        self._print_message("Carro de luxo", "NZ")

class CommonCarNZ(CommonVehicle, VehicleBase):
    def get_customer_common(self) -> None:
        self._print_message("Carro popular", "NZ")

class CommonMotorcycleNZ(CommonVehicle, VehicleBase):
    def get_customer_common(self) -> None:
        self._print_message("Moto", "NZ")

class LuxuryMotorcycleNZ(LuxuryVehicle, VehicleBase):
    def get_customer_luxury(self) -> None:
        self._print_message("Moto de luxo", "NZ")

# Implementações concretas de veículos para a zona sul (SZ)
class LuxuryCarSZ(LuxuryVehicle, VehicleBase):
    def get_customer_luxury(self) -> None:
        self._print_message("Carro de luxo", "SZ")

class CommonCarSZ(CommonVehicle, VehicleBase):
    def get_customer_common(self) -> None:
        self._print_message("Carro popular", "SZ")

class CommonMotorcycleSZ(CommonVehicle, VehicleBase):
    def get_customer_common(self) -> None:
        self._print_message("Moto", "SZ")

class LuxuryMotorcycleSZ(LuxuryVehicle, VehicleBase):
    def get_customer_luxury(self) -> None:
        self._print_message("Moto de luxo", "SZ")

# Fábrica abstrata que define métodos de criação para veículos
class VehicleFactory(ABC):
    @abstractmethod
    def get_luxury_car(self) -> LuxuryVehicle:
        """Retorna uma instância de um veículo de luxo (carro) específico."""
        pass

    @abstractmethod
    def get_common_car(self) -> CommonVehicle:
        """Retorna uma instância de um veículo comum (carro) específico."""
        pass

    @abstractmethod
    def get_luxury_motorcycle(self) -> LuxuryVehicle:
        """Retorna uma instância de uma motocicleta de luxo específica."""
        pass

    @abstractmethod
    def get_common_motorcycle(self) -> CommonVehicle:
        """Retorna uma instância de uma motocicleta comum específica."""
        pass

# Implementação concreta da fábrica para a zona norte (NZ)
class VehicleNorthZoneFactory(VehicleFactory):
    def get_luxury_car(self) -> LuxuryVehicle:
        return LuxuryCarNZ()

    def get_common_car(self) -> CommonVehicle:
        return CommonCarNZ()

    def get_luxury_motorcycle(self) -> LuxuryVehicle:
        return LuxuryMotorcycleNZ()

    def get_common_motorcycle(self) -> CommonVehicle:
        return CommonMotorcycleNZ()

# Implementação concreta da fábrica para a zona sul (SZ)
class VehicleSouthZoneFactory(VehicleFactory):
    def get_luxury_car(self) -> LuxuryVehicle:
        return LuxuryCarSZ()

    def get_common_car(self) -> CommonVehicle:
        return CommonCarSZ()

    def get_luxury_motorcycle(self) -> LuxuryVehicle:
        return LuxuryMotorcycleSZ()

    def get_common_motorcycle(self) -> CommonVehicle:
        return CommonMotorcycleSZ()

# Classe cliente que utiliza as fábricas para acessar os métodos de criação e obter veículos
class ClientVehicleRequestor:
    def __init__(self, factories: List[VehicleFactory]) -> None:
        """
        Inicializa o solicitante de veículos com uma lista de fábricas.

        Args:
            factories (List[VehicleFactory]): Lista de fábricas de veículos para diferentes zonas.
        """
        self.factories = factories

    def get_customers(self) -> None:
        """
        Itera pelas fábricas e solicita cada tipo de veículo para buscar clientes,
        exibindo as mensagens padronizadas.
        """
        for factory in self.factories:
            # Obter e chamar método de busca para cada tipo de veículo
            common_car = factory.get_common_car()
            common_car.get_customer_common()

            luxury_car = factory.get_luxury_car()
            luxury_car.get_customer_luxury()

            common_motorcycle = factory.get_common_motorcycle()
            common_motorcycle.get_customer_common()

            luxury_motorcycle = factory.get_luxury_motorcycle()
            luxury_motorcycle.get_customer_luxury()

# Código de execução principal
if __name__ == '__main__':
    # Inicializa as fábricas para zonas norte e sul
    factories = [VehicleNorthZoneFactory(), VehicleSouthZoneFactory()]
    
    # Cria um cliente solicitante de veículos com as fábricas disponíveis
    client = ClientVehicleRequestor(factories)
    
    # Solicita que cada veículo busque clientes e exiba as mensagens
    client.get_customers()
