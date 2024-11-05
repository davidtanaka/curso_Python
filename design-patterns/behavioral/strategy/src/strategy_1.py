"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algorítmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: 'DiscountStrategy') -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: ...

class CustomDiscount(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)

class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)

class NoDiscount(DiscountStrategy):
    def calculate(self, value: float | int) -> float | int:
        return value

if __name__ == '__main__':
    twent_porcent = TwentyPercent()
    order = Order(100, twent_porcent)
    
    fifty_porcent = FiftyPercent()
    order2 = Order(100, fifty_porcent)

    no_discount = NoDiscount()
    order3 = Order(100, no_discount)

    custom_discount = CustomDiscount(60)
    order4 = Order(500, custom_discount)

    print(order.total, order.total_with_discount)
    print(order2.total, order2.total_with_discount)
    print(order3.total, order3.total_with_discount)
    print(order4.total, order4.total_with_discount)