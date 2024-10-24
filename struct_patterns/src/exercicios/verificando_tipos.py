# Exercício 1: Verificação de Tipos
# Crie uma função chamada `verificar_tipo` que receba um valor e use `match` para retornar uma mensagem 
# que indique se o valor é um `int`, `float`, `str` ou `bool`. 
# Se o valor não for nenhum desses tipos, retorne "Tipo desconhecido".

# Exemplo de uso esperado:
# print(verificar_tipo(42))         # Saída esperada: "É um inteiro"
# print(verificar_tipo(3.14))       # Saída esperada: "É um float"
# print(verificar_tipo("Olá"))      # Saída esperada: "É uma string"
# print(verificar_tipo(True))       # Saída esperada: "É um booleano"
# print(verificar_tipo([1, 2, 3]))  # Saída esperada: "Tipo desconhecido"

# Minha solução
from pickletools import int4


valores_aceitos = int | float | str | bool 
def verificar_tipo(valor: valores_aceitos) -> str:
    match valor:
        case int(): 
            return f'{valor} é um inteiro'
        case float():
            return f'{valor} é um float' 
        case str():
            return f'{valor} é uma string'
        case bool():
            return f'{valor} é um booleano'
        case _:
            return 'Comando inválido'

print(verificar_tipo(42))         # Saída esperada: "42 é um inteiro"
print(verificar_tipo(3.14))       # Saída esperada: "3.14 é um float"
print(verificar_tipo("Olá"))      # Saída esperada: "Olá é uma string"
print(verificar_tipo(True))       # Saída esperada: "True é um booleano"
