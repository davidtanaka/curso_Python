from typing import List

# Exercício 3: Listas e Dicionários Tipados
# Crie uma função chamada calcular_media que receba uma lista de números 
# (do tipo float) e retorne a média dos valores. Use tipagem para 
# especificar que a lista é composta por float e que o retorno 
# também é um float.
def calcular_media(numeros: List[float]) -> float:
    if numeros:  # Verifica se a lista não está vazia
        return sum(numeros) / len(numeros)  # Calcula a média
    return 0.0  # Retorna 0.0 se a lista estiver vazia

# Exemplo de uso da função calcular_media
print(calcular_media([10.0, 10.0, 10.0]))  # Saída: 10.0