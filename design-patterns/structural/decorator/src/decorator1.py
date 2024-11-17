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

from abc import ABC  # Fornece suporte para criar classes abstratas.
from dataclasses import dataclass  # Facilita a criação de classes imutáveis com atributos definidos.
from copy import deepcopy  # Faz cópias profundas de objetos, útil para listas de objetos complexos.

# Ingredients
@dataclass
class Ingredient:
    # Classe base para representar um ingrediente com um preço.
    price: float

@dataclass
class Bread(Ingredient):
    # Classe para o ingrediente pão, com um preço fixo.
    price: float = 1.5

@dataclass
class Sausage(Ingredient):
    # Classe para o ingrediente salsicha, com um preço fixo.
    price: float = 3.9

@dataclass
class Bacon(Ingredient):
    # Classe para o ingrediente bacon, com um preço fixo.
    price: float = 7.99

@dataclass
class Egg(Ingredient):
    # Classe para o ingrediente ovo, com um preço fixo.
    price: float = 3.5

@dataclass
class Cheese(Ingredient):
    # Classe para o ingrediente queijo, com um preço fixo.
    price: float = 6.45

@dataclass
class MashedPotatoes(Ingredient):
    # Classe para o ingrediente purê de batatas, com um preço fixo.
    price: float = 6.2

@dataclass
class PotatoSticks(Ingredient):
    # Classe para o ingrediente batata palha, com um preço fixo.
    price: float = 0.99


# Hotdogs
class Hotdog(ABC):
    # Classe abstrata para um hotdog, que pode ter vários ingredientes.

    _name: str
    _ingredients: list[Ingredient]

    @property
    def price(self) -> float:
        # Calcula o preço total do hotdog somando o preço de todos os ingredientes.
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        # Retorna o nome do hotdog. Deve ser implementado pelas subclasses.
        ...

    @property
    def ingredients(self) -> list[Ingredient]:
        # Retorna a lista de ingredientes do hotdog.
        return self._ingredients

    def __repr__(self) -> str:
        # Retorna uma representação amigável do hotdog.
        return f'{self.__class__.__name__}({self.price} -> {self.ingredients})'


class SimpleHotdog(Hotdog):
    # Hotdog simples com pão, salsicha e batata palha.

    def __init__(self) -> None:
        self._name: str = 'SimpleHotdog'
        self._ingredients: list[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


class SpecialHotdog(Hotdog):
    # Hotdog especial com vários ingredientes adicionais.

    def __init__(self) -> None:
        self._name: str = 'SpecialHotdog'
        self._ingredients: list[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            PotatoSticks()
        ]


class HotdogDecorator(Hotdog):
    # Decorator para adicionar novos ingredientes a um hotdog existente.

    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        self.hotdog = hotdog
        self._ingredient = ingredient

        # Copia os ingredientes do hotdog original e adiciona o novo ingrediente.
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        # Atualiza o nome do hotdog incluindo o novo ingrediente.
        return f'{self.hotdog.name} +{self._ingredient.__class__.__name__}'


if __name__ == "__main__":
    # Cria um hotdog simples
    simple_hotdog = SimpleHotdog()
    print(simple_hotdog)

    # Adiciona bacon ao hotdog simples
    bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())

    # Adiciona ovo ao hotdog com bacon
    egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog, Egg())

    # Adiciona purê de batata ao hotdog com ovo e bacon
    mashed_potato_egg_bacon_simple_hotdog = HotdogDecorator(
        egg_bacon_simple_hotdog,
        MashedPotatoes()
    )

    # Mostra o hotdog final com todos os ingredientes adicionados
    print(mashed_potato_egg_bacon_simple_hotdog)
