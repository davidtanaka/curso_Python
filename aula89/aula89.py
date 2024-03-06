#dir, hasattr e getattr em python
string = 'Davi'
metodo = 'strip'
if hasattr(string, metodo):
     print(f'Existe', metodo, 'em ', end='')
     print(getattr(string, metodo)())
else:
     print('Não existe o método', metodo)