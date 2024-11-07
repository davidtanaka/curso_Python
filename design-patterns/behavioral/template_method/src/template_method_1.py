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


class Abstract(ABC):
    def template_method(self):
        _hook = self.hook()
        result1 = self.operation1()
        result2 = self.operation2()
        class_base = self.base_class_method()
        return f"{result1}\n{result2}\n{class_base}\n{_hook}"
    
    def hook(self): ...

    def base_class_method(self):
        return f'SOU DA CLASSE ABSTRATA E SEREI EXECUTADO TAMBÉM'

    @abstractmethod
    def operation1(self): ...

    @abstractmethod
    def operation2(self): ...

class ConcreteClass1(Abstract):
    def hook(self):
        return f'Utilizando hook (ConcretClass1)'

    def operation1(self) -> str: 
        return f'Operação 1 concluída'

    def operation2(self) -> str: 
        return f'Operação 2 concluída'
    

class ConcreteClass2(Abstract):
    def hook(self):
        return f'Utilizando hook (ConcretClass2)'

    def operation1(self) -> str: 
        return f'Operação 1 concluída (De maneira diferente, "ConcretClass2")'

    def operation2(self) -> str: 
        return f'Operação 2 concluída  (De maneira diferente, "ConcretClass2")'
    
if __name__ == '__main__':
    c1 = ConcreteClass1()
    c2 = ConcreteClass2()
    print(c1.template_method())
    print(c2.template_method())
