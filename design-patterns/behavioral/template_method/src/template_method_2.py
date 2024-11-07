from abc import ABC, abstractmethod

class Pizza(ABC):
    # Classe abstrata
    def prepare(self) -> str:
        """
        Método template que define a sequência de operações para preparar a pizza.
        Chamadas para hooks, métodos abstratos e concretos, como: adicionar ingredientes, cozinhar, cortar e servir.
        """
        hook_before = self.hook_before_add_ingredients()  # Hook antes de adicionar ingredientes
        _ingredients = self.add_ingredients()  # Adiciona ingredientes (método abstrato)
        hook_after = self.hook_after_add_ingredients()  # Hook depois de adicionar ingredientes
        _cook = self.cook()  # Cozinha (método abstrato)
        _cut = self.cut()  # Método concreto para cortar
        _serve = self.serve()  # Método concreto para servir

        # Usando match/case em vez de if para decidir o formato de retorno
        match (hook_before, hook_after):
            case (None, None):
                return f"{_ingredients}\n{_cook}\n{_cut}\n{_serve}\n"
            case (None, _):
                return f"\n{_ingredients}\n{hook_after}\n{_cook}\n{_cut}\n{_serve}\n"
            case (_, None):
                return f"{hook_before}\n{_ingredients}\n{_cook}\n{_cut}\n{_serve}\n"
            case (_, _):
                return f"{hook_before}\n{_ingredients}\n{hook_after}\n{_cook}\n{_cut}\n{_serve}\n"
    
    def hook_before_add_ingredients(self) -> str | None:
        """Método hook opcional que pode ser sobrescrito pelas subclasses."""
        pass

    def hook_after_add_ingredients(self) -> str | None:
        """Método hook opcional que pode ser sobrescrito pelas subclasses."""
        pass
    
    def cut(self) -> str:
        """Método concreto para cortar a pizza."""
        return f'{self.__class__.__name__}: Cortando a pizza'
    
    def serve(self) -> str:
        """Método concreto para servir a pizza."""
        return f'{self.__class__.__name__}: Servindo a pizza'
    
    @abstractmethod
    def add_ingredients(self) -> str:
        """Método abstrato para adicionar os ingredientes, a ser implementado pelas subclasses."""
        pass
    
    @abstractmethod
    def cook(self) -> str:
        """Método abstrato para cozinhar a pizza, a ser implementado pelas subclasses."""
        pass

class AModa(Pizza):
    def hook_before_add_ingredients(self) -> str:
        return f'Adicionando molho na massa da pizza'

    def add_ingredients(self) -> str:
        return f'{self.__class__.__name__} Ingredientes: Cebola, Calabresa, '\
               f'Mussarela, Orégano, Ovos cozidos, Azeitona e mix de pimenta'
    
    def hook_after_add_ingredients(self) -> str:
        return f'Adicionando Queijo ralado na pizza'
    
    def cook(self) -> str:
        return f'{self.__class__.__name__}: Cozinha por 40min no forno a Lenha'

class Veg(Pizza):
    def hook_before_add_ingredients(self) -> str:
        return f'Verificando se não há nada que não seja vegano (caso tenha, retirar)'
    
    def add_ingredients(self) -> str:
        return f'{self.__class__.__name__} Ingredientes VEGANOS'
    
    def cook(self) -> str:
        return f'{self.__class__.__name__}: Cozinha por 30min no forno a Lenha'


if __name__ == '__main__':
    a_moda = AModa()
    print(a_moda.prepare())  # Exibe a preparação da pizza AModa

    veg = Veg()
    print(veg.prepare())  # Exibe a preparação da pizza Veg
