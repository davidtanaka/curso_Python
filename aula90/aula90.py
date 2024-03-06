import sys
# Generator expression, Iterables e Iterators em Python
iterable = ['eu', 'tenho', '__iter__']
iterator = iter(iterable) # tem__iter__ e __next__
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
lista = [n for n in range(10000000)]
generator = (n for n in range(1000000))

print(sys.getsysof(lista))
print(sys.getsysof(generator))

print(generator)

# for n in generator:
#    print(n)