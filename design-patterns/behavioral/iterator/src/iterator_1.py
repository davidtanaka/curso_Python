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
from gc import collect
from typing import Any, List


class MyIterator(Iterator):
    def __init__(self, collection) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index+=1
            return item
        except:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, collection) -> None:
        self._collection = collection
        self._index = -2

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index-=1
            return item
        except:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self):
        return MyIterator(self._items)
    
    def reverse_iterator(self):
        return ReverseIterator(self._items)

    def __str__(self):
        return f'{self.__class__.__name__}({self._items})'

if __name__ == '__main__':
    mylist = MyList()
    mylist.add('Davi')
    mylist.add('Mauro')
    mylist.add('Paulo')
    
    # print(mylist)

    for item in mylist:
        print(item)

    print()

    for value in mylist.reverse_iterator():
        print(value)
