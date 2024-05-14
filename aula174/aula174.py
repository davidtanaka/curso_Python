# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename 
import os
import shutil

HOME = os.path.expanduser('~')
DUCUMENTS = os.path.join(HOME, 'Documents')
PASTA_ORIGINAL = os.path.join(DUCUMENTS, 'EXEMPLO')
NOVA_PASTA = os.path.join(DUCUMENTS, 'NOVA_PASTA')

shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')

os.makedirs(NOVA_PASTA, exist_ok=True)


# for root, dirs, files in os.walk(PASTA_ORIGINAL):
    # for dir_ in dirs:
    #     novo_caminho_diretorio = os.path.join(
    #     root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
    #     )
#         os.makedirs(novo_caminho_diretorio, exist_ok=True)


#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         novo_caminho_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#         )
#         shutil.copy(caminho_arquivo, novo_caminho_arquivo)
