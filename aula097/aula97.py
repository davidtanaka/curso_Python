"""
Entendendo os seus proprios ódulos python
O primeiro módulo executado se chama __main__
Você pode importar outro módulo inteiro ou parte do módulo 
O python conhece a pasta onde o __main__ está e as pastas
abaixo dele.
Ele não reconhece as pastas e módulos acima do __main__ por
padrão
O python conhece todos os módulos e pacotes presentes nos caminhos
de sys.path
"""
import aula97_m
from aula97_m import soma_ilimitada
print('Este módulo se chama', __name__)

aula97_m.soma_ilimitada(4, 4, 4, 8, 9, 6, 455)
soma_ilimitada(1, 2, 4, 6)

