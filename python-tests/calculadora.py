def soma(x, y):
    """ Soma x e y
    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x + y

def subtrai(x, y):
    """ Subtrai x e y

    >>> subtrai(10, 5)
    5

    >>> subtrai(10, 4)
    6
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x - y

def dividir(x, y):
    """ Dividi x e y

    >>> dividir(10, 2)
    5.0

    >>> dividir(12, 2)
    6.0
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x / y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
