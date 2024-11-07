"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""

from abc import ABC, abstractmethod

class Pizza(ABC):
    # Classe abstrata
    def prepare(self):
        # Template method
        hook_before = self.hook_before_add_ingredients() # Hook
        _ingredients = self.add_ingredients() # Abstract
        hook_after = self.hook_after_add_ingredients() # Hook
        _cook = self.cook() # Abstract
        _cut = self.cut() # Concreto
        _serve = self.serve() # Concreto
        if hook_before is not None and hook_after is not None:
            return f"{hook_before}\n{_ingredients}\n{hook_after}\n{_cook}\n"\
            f"{_cut}\n{_serve}\n"
        
        if hook_before is not None:
            return f"{hook_before}\n{_ingredients}\n{_cook}\n{_cut}\n{_serve}\n"
        
        if hook_after is not None:
            return f"\n{_ingredients}\n{hook_after}\n{_cook}\n{_cut}\n{_serve}\n"
        return f"{_ingredients}\n{_cook}\n{_cut}\n{_serve}\n"
    
    def hook_before_add_ingredients(self): ...
    def hook_after_add_ingredients(self): ...
    
    def cut(self):
        return f'{self.__class__.__name__}: Cortando a pizza'
    
    def serve(self):
        return f'{self.__class__.__name__}: Servindo a pizza'
    
    @abstractmethod
    def add_ingredients(self): ...
    
    @abstractmethod
    def cook(self): ...

class AModa(Pizza):
    def hook_before_add_ingredients(self):
        return f'Adicionando molho na massa da pizza'

    def add_ingredients(self):
        return f'{self.__class__.__name__} Ingredientes: Cebola, Calabresa, '\
            f'Mussarela, Orégano, Ovos cozidos, Azeitona e mix de pimenta'
    
    def hook_after_add_ingredients(self):
        return f'Adicionando Queijo ralado na pizza'
    
    def cook(self):
        return f'{self.__class__.__name__}: Cozinha por 40min no forno a Lenha'

class Veg(Pizza):
    def hook_before_add_ingredients(self):
        return f'Verificando se não a nada que não seja vegano(caso tenha retirar)'
    
    def add_ingredients(self):
        return f'{self.__class__.__name__} Ingredientes VEGANOS'
    
    def cook(self):
        return f'{self.__class__.__name__}: Cozinha por 30min no forno a Lenha'


if __name__ == '__main__':
    a_moda = AModa()
    print(a_moda.prepare())

    veg = Veg()
    print(veg.prepare())
