# Exercício 2: Tipagem com Tipos Opcionais
# Escreva uma função chamada saudacao que aceite um parâmetro nome 
# do tipo str, e um parâmetro opcional idade do tipo int. A função 
# deve retornar uma string com uma saudação, e se a idade for 
# fornecida, inclua-a na mensagem. Use tipagem para especificar 
# que idade é opcional.
def saudacao(nome: str, idade: int | None = None) -> str:
    if idade is not None:
        return f'Saudações, {nome}. Você tem {idade} anos de idade.'
    return f'Saudações, {nome}.'

# Exemplos de uso da função saudacao
print(saudacao('Davi'))          # Saída: "Saudações, Davi."
print(saudacao('Davi', 16))      # Saída: "Saudações, Davi. Você tem 16 anos de idade."
