# Exercício 2: Análise de Tuplas
# Crie uma função chamada `analisar_coordenadas` que use `match` para receber uma tupla representando 
# coordenadas 2D (x, y) ou 3D (x, y, z). A função deve retornar uma mensagem indicando se as coordenadas 
# são 2D ou 3D e listar os valores.
# Se a tupla tiver um formato diferente, retorne "Formato de coordenadas não reconhecido".

# Exemplo de uso esperado:
# print(analisar_coordenadas((3, 4)))      # Saída esperada: "Coordenadas 2D: x=3, y=4"
# print(analisar_coordenadas((3, 4, 5)))   # Saída esperada: "Coordenadas 3D: x=3, y=4, z=5"
# print(analisar_coordenadas((3, 4, 5, 6))) # Saída esperada: "Formato de coordenadas não reconhecido"

def analisar_coordenadas(tupla: tuple):
    tamanho_tupla = len(tupla)
    match tamanho_tupla:
        case 2:
            return f'Você enviou coordenadas em 2D (x={tupla[0]}, y={tupla[1]})'
        case 3:
            return f'Você enviou coordenadas 3D (x={tupla[0]}, y={tupla[1]}, z={tupla[2]})'
        case _:
            return f'Formato de coordenadas não reconhecidos'

print(analisar_coordenadas((3, 4)))      # Saída esperada: "Coordenadas 2D: x=3, y=4"
print(analisar_coordenadas((3, 4, 5)))   # Saída esperada: "Coordenadas 3D: x=3, y=4, z=5"
print(analisar_coordenadas((3, 4, 5, 6))) # Saída esperada: "Formato de coordenadas não reconhecido"
