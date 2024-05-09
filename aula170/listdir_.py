# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('C:\\Users', 'davit', 'exemplo')

for item in os.listdir(caminho):
    if not os.path.isdir(caminho):
        continue

    for imagem in os.listdir(caminho):
        print(imagem)