"""
Iterator é um padrão comportamental que tem a
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objeto
agregado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna
- Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos
- Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais
tarefas para um objeto iterador.
"""

from collections.abc import Iterator, Iterable
from typing import Any, List

class MyIterator(Iterator):
    """Iterador para percorrer uma coleção do início ao fim."""
    
    def __init__(self, collection: List[Any]) -> None:
        """Inicializa o iterador com uma coleção e o índice inicial."""
        self._collection = collection
        self._index = 0

    def __next__(self) -> Any:
        """Retorna o próximo item da coleção; levanta StopIteration ao final."""
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:  # Erro específico de índice
            raise StopIteration

class ReverseIterator(Iterator):
    """Iterador para percorrer uma coleção do fim para o início."""
    
    def __init__(self, collection: List[Any]) -> None:
        """Inicializa o iterador com a coleção e o índice para percorrer em ordem inversa."""
        self._collection = collection
        self._index = -1  # Começa no último índice válido

    def __next__(self) -> Any:
        """Retorna o item da coleção na posição atual; levanta StopIteration ao final."""
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:  # Erro específico de índice
            raise StopIteration

class MyList(Iterable):
    """Coleção que permite adição de itens e pode ser percorrida com iteradores customizados."""
    
    def __init__(self) -> None:
        """Inicializa a lista de itens vazia."""
        self._items: List[Any] = []

    def add(self, value: Any) -> None:
        """Adiciona um novo item à coleção."""
        self._items.append(value)

    def __iter__(self) -> MyIterator:
        """Retorna um iterador padrão da coleção."""
        return MyIterator(self._items)
    
    def reverse_iterator(self) -> ReverseIterator:
        """Retorna um iterador que percorre a coleção em ordem inversa."""
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        """Retorna uma representação textual da coleção."""
        return f'{self.__class__.__name__}({self._items})'

if __name__ == '__main__':
    mylist = MyList()
    mylist.add('Davi')
    mylist.add('Mauro')
    mylist.add('Paulo')
    
    # Iteração padrão
    for item in mylist:
        print(item)

    print()

    # Iteração reversa
    for value in mylist.reverse_iterator():
        print(value)
