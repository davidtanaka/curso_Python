from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
     try:
          print('abrindo arquivo')
          arquivo = open(caminho_arquivo, modo, encoding='utf8')
          yield arquivo
     except Exception as e:
          print('Ocorreu erro', e)
     finally:
          print('Fechando arquivo')
          arquivo.close()

with my_open('aula150\\aula150.txt', 'w') as arquivo:
     arquivo.write('Linha 1\n')
     arquivo.write('Linha 2\n')
     arquivo.write('Linha 3\n')
     print('WITH', arquivo)