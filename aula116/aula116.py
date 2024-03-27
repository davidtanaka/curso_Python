import os

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho = 'D:\\Cursos\\cursoPython\\aula116\\arquivo_aula116.txt'

# arquivo = open(caminho, 'w)
# #
# arquivo.close()
with open(caminho,'w') as arquivo:
     arquivo.write('Atenção\r')
     arquivo.write('linha 1\r')
     arquivo.write('linha 2\r')
     arquivo.writelines(
          ('linha 3\r', 'linha 4\r')
     )
    # arquivo.seek(0, 0)
     
with open(caminho,'r') as arquivo:
     print(arquivo.read())
     

# os.remove(caminho)
# os .rename(caminho, 'aula116-2.txt')