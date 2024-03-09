import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
     # o importlib.reload serve basicamente para reccarregar a importação.
     importlib.reload(aula98_m)
     print(i)

print('FIM')