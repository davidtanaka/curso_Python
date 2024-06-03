('Este módulo se chama', __name__)

def soma_ilimitada(*args):
     soma = 0
     for numero in args:
          soma = soma + numero
     return print(soma)
