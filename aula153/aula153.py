# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instancia de uma 
# classe 'callable'
class CallMe:
     def __init__(self, phone):
          self.phone = phone

     def __call__(self, nome):
          print(nome, 'esta chamando', self.phone)
          return 2134
     

call1 = CallMe('326437264333')
retorno = call1('Davi Tanaka')
print(retorno)