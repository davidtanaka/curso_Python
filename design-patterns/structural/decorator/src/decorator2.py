"""
Decorator é um padrão de projeto estrutural que permite que você
adicione novos comportamentos em objetos ao colocá-los dentro de
um "wrapper" (decorador) de objetos.
Decoradores fornecem uma alternativa flexível ao uso de subclasses
para a extensão de funcionalidades.

Decorator (padrão de projeto) != Decorator em Python

Python decorator -> Um decorator é um callable que aceita outra
função como argumento (a função decorada). O decorator pode
realizar algum processamento com a função decorada e devolvê-la
ou substituí-la por outra função ou objeto invocável.
Do livro "Python Fluente", por Luciano Ramalho (pág. 223)
"""

from dataclasses import dataclass
from copy import deepcopy
from typing import List


# INGREDIENTES
@dataclass
class Ingredient:
    """Classe base para os ingredientes, com um atributo de preço."""
    price: float


@dataclass
class Bread(Ingredient):
    """Classe que representa o pão do hot dog."""
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    """Classe que representa a salsicha do hot dog."""
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    """Classe que representa o bacon como ingrediente adicional."""
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    """Classe que representa o ovo como ingrediente adicional."""
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    """Classe que representa o queijo como ingrediente adicional."""
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    """Classe que representa o purê de batatas como ingrediente adicional."""
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    """Classe que representa batata-palha como ingrediente adicional."""
    price: float = 0.99


# CLASSE BASE PARA HOTDOGS
class Hotdog:
    """Classe base para representar um hot dog."""
    _name: str  # Nome do hot dog
    _ingredients: List[Ingredient]  # Lista de ingredientes do hot dog

    @property
    def price(self) -> float:
        """
        Calcula o preço total do hot dog, somando o preço de todos os ingredientes.
        """
        return round(sum([ingredient.price for ingredient in self._ingredients]), 2)

    @property
    def name(self) -> str:
        """Retorna o nome do hot dog."""
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        """Retorna a lista de ingredientes do hot dog."""
        return self._ingredients

    def __repr__(self) -> str:
        """Representação em string do hot dog: nome, preço e ingredientes."""
        return f'{self.name}({self.price}) -> {self.ingredients})'


# HOTDOGS ESPECÍFICOS
class SimpleHotdog(Hotdog):
    """Classe que define um hot dog simples com ingredientes básicos."""
    def __init__(self) -> None:
        self._name: str = 'SimpleHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


class SpecialHotdog(Hotdog):
    """Classe que define um hot dog especial com vários ingredientes."""
    def __init__(self) -> None:
        self._name: str = 'SpecialHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes(),
            PotatoSticks()
        ]


# DECORADOR PARA HOTDOGS
class HotdogDecorator(Hotdog):
    """Decorator que adiciona um ingrediente extra a um hot dog."""
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        self.hotdog: Hotdog = hotdog  # O hot dog original que será decorado
        self._ingredient: Ingredient = ingredient  # O ingrediente extra

        # Copia os ingredientes do hot dog original e adiciona o novo ingrediente
        self._ingredients: List[Ingredient] = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        """Adiciona o nome do ingrediente extra ao nome do hot dog."""
        return f'{self.hotdog.name} +{self._ingredient.__class__.__name__}'


# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    # Criação de um hot dog simples
    simple_hotdog = SimpleHotdog()
    print(simple_hotdog)

    # Adicionando bacon ao hot dog simples
    bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())

    # Adicionando ovo ao hot dog com bacon
    egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog, Egg())

    # Adicionando purê de batatas ao hot dog com ovo e bacon
    mashed_potato_egg_bacon_simple_hotdog = HotdogDecorator(
        egg_bacon_simple_hotdog,
        MashedPotatoes()
    )

    # Exibindo o hot dog final
    print(mashed_potato_egg_bacon_simple_hotdog)
