"""
CONSTANTE = 'VARRIAVEIS' que não podem mudar
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
"""
velocidade = 61 # Velocidadde atual do carro
local_carro = 99 # Local em que o carro esta na estrada

RADAR_1 = 60 # Velocidade maxima do radar 1
LOCAL_1 = 100 # local em que o radar se localiza na pista
RADAR_RANGE = 1 # A distancia em que o radar pega

valocidade_maior_radar1 = velocidade > RADAR_1

if valocidade_maior_radar1:
     print('O carro esta na velocida maior do que a permitida')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
       local_carro <= (LOCAL_1 + RADAR_RANGE) and \
          valocidade_maior_radar1:
     print('Carro mutado  no radar 1')