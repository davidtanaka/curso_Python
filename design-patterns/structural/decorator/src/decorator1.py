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


from __future__ import annotations  # Permite o uso de anotações de tipo no estilo futuro.
from dataclasses import dataclass  # Facilita a criação de classes imutáveis com atributos definidos.
from typing import List  # Para especificar listas tipadas.
from copy import deepcopy  # Faz cópias profundas de objetos, útil para listas de objetos complexos.

# INGREDIENTS
@dataclass
class Ingredient:
    # Classe base para representar um ingrediente com um preço.
    price: float


@dataclass
class Bread(Ingredient):
    # Classe para o ingrediente pão, com um preço fixo.
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    # Classe para o ingrediente salsicha, com um preço fixo.
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    # Classe para o ingrediente bacon, com um preço fixo.
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    # Classe para o ingrediente ovo, com um preço fixo.
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    # Classe para o ingrediente queijo, com um preço fixo.
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    # Classe para o ingrediente purê de batatas, com um preço fixo.
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    # Classe para o ingrediente batata palha, com um preço fixo.
    price: float = 0.99

# Hotdogs
class Hotdog:
    # Classe base para representar um hotdog.

    _name: str  # Nome do hotdog.
    _ingredients: List[Ingredient]  # Lista de ingredientes do hotdog.

    @property
    def price(self) -> float:
        # Calcula o preço total do hotdog somando o preço de todos os ingredientes.
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        # Retorna o nome do hotdog.
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        # Retorna a lista de ingredientes do hotdog.
        return self._ingredients

    def __repr__(self) -> str:
        # Retorna uma representação amigável do hotdog.
        return f'{self.name}({self.price}) -> {self.ingredients})'


class SimpleHotdog(Hotdog):
    # Hotdog simples com pão, salsicha e batata palha.

    def __init__(self) -> None:
        self._name: str = 'SimpleHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


class SpecialHotdog(Hotdog):
    # Hotdog especial com vários ingredientes adicionais.

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

# Decorators
class HotdogDecorator(Hotdog):
    # Decorator base para adicionar novos comportamentos a um hotdog.

    def __init__(self, hotdog: Hotdog) -> None:
        self.hotdog = hotdog  # Hotdog que está sendo decorado.

    @property
    def price(self) -> float:
        # Retorna o preço do hotdog decorado.
        return self.hotdog.price

    @property
    def name(self) -> str:
        # Retorna o nome do hotdog decorado.
        return self.hotdog.name

    @property
    def ingredients(self) -> List[Ingredient]:
        # Retorna os ingredientes do hotdog decorado.
        return self.hotdog.ingredients


class BaconDecorator(HotdogDecorator):
    # Decorator que adiciona bacon a um hotdog.

    def __init__(self, hotdog: Hotdog) -> None:
        super().__init__(hotdog)  # Chama o construtor da classe base.
        self._ingredient = Bacon()  # Define o ingrediente bacon.

        # Copia os ingredientes do hotdog original e adiciona bacon.
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        # Calcula o preço total do hotdog com bacon.
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        # Atualiza o nome do hotdog para incluir bacon.
        return f'{self.hotdog.name} +{self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> List[Ingredient]:
        # Retorna os ingredientes do hotdog com bacon.
        return self._ingredients


if __name__ == "__main__":
    # Cria um hotdog simples.
    simple_hotdog = SimpleHotdog()

    # Decora o hotdog simples sem adicionar ingredientes.
    decorated_simple_hotdog = HotdogDecorator(simple_hotdog)

    # Adiciona bacon ao hotdog simples.
    bacon_simple_hotdog = BaconDecorator(simple_hotdog)

    # Adiciona bacon novamente ao hotdog com bacon.
    bacon_simple_hotdog = BaconDecorator(bacon_simple_hotdog)

    # Mostra os hotdogs criados e decorados.
    print(simple_hotdog)
    print(decorated_simple_hotdog)
    print(bacon_simple_hotdog)
