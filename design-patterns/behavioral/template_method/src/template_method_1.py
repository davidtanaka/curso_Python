from abc import ABC, abstractmethod

class Abstract(ABC):
    def template_method(self) -> str:
        """
        Método template que define a estrutura do algoritmo.
        Este método chama operações específicas de subclasses (operation1, operation2),
        um método opcional (hook) e um método comum a todas as classes base (base_class_method).
        """
        _hook = self.hook()  # Chama o hook, que pode ser sobrescrito pelas subclasses
        result1 = self.operation1()  # Chama a operação 1, definida pelas subclasses
        result2 = self.operation2()  # Chama a operação 2, definida pelas subclasses
        class_base = self.base_class_method()  # Chama o método base, que é comum a todas as classes
        return f"{result1}\n{result2}\n{class_base}\n{_hook}"

    def hook(self) -> str:
        """
        Método opcional (hook) que pode ser sobrescrito pelas subclasses.
        Serve como um ponto de extensão no algoritmo.
        """
        return ""

    def base_class_method(self) -> str:
        """
        Método comum a todas as classes que herdam de Abstract.
        Este método pode ser chamado diretamente dentro do template method.
        """
        return 'SOU DA CLASSE ABSTRATA E SEREI EXECUTADO TAMBÉM'

    @abstractmethod
    def operation1(self) -> str:
        """
        Operação abstrata 1 que deve ser implementada nas subclasses.
        """
        pass

    @abstractmethod
    def operation2(self) -> str:
        """
        Operação abstrata 2 que deve ser implementada nas subclasses.
        """
        pass


class ConcreteClass1(Abstract):
    def hook(self) -> str:
        """
        Sobrescreve o hook opcional, caso a ConcreteClass1 precise dele.
        """
        return 'Utilizando hook (ConcretClass1)'

    def operation1(self) -> str:
        """
        Implementação específica da operação 1 para ConcreteClass1.
        """
        return 'Operação 1 concluída'

    def operation2(self) -> str:
        """
        Implementação específica da operação 2 para ConcreteClass1.
        """
        return 'Operação 2 concluída'


class ConcreteClass2(Abstract):
    def hook(self) -> str:
        """
        Sobrescreve o hook opcional, caso a ConcreteClass2 precise dele.
        """
        return 'Utilizando hook (ConcretClass2)'

    def operation1(self) -> str:
        """
        Implementação específica da operação 1 para ConcreteClass2.
        """
        return 'Operação 1 concluída (De maneira diferente, "ConcretClass2")'

    def operation2(self) -> str:
        """
        Implementação específica da operação 2 para ConcreteClass2.
        """
        return 'Operação 2 concluída  (De maneira diferente, "ConcretClass2")'


if __name__ == '__main__':
    c1 = ConcreteClass1()
    c2 = ConcreteClass2()
    print(c1.template_method())  # Executa o método template usando a ConcreteClass1
    print(c2.template_method())  # Executa o método template usando a ConcreteClass2
