"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 60 # Velocidade atual do carro
localizacao_carro_km = 99 # Local onde o carro está parado na estrada

LIMITE_VELOCIDADE_RADAR_1 = 60 # Velocidade máxima do radar 1 
LOCALIZACAO_KM_RADAR_1 = 100 # Local onde o radar 1 está
DISTANCIA_DE_MARGEM = 1 

RANGE_ANTERIOR = LOCALIZACAO_KM_RADAR_1 - DISTANCIA_DE_MARGEM
RANGE_POSTERIOR = LOCALIZACAO_KM_RADAR_1 + DISTANCIA_DE_MARGEM

passou_pelo_range_anterior = (localizacao_carro_km == RANGE_ANTERIOR)
passou_centro_radar = (localizacao_carro_km == LOCALIZACAO_KM_RADAR_1)
passou_pelo_range_posterior = (localizacao_carro_km == RANGE_POSTERIOR)
ultrapassou_limite_velocidade_radar =(velocidade > LIMITE_VELOCIDADE_RADAR_1)

carro_multado = (
    (
        passou_pelo_range_anterior or 
        passou_pelo_range_posterior or 
        passou_centro_radar
    ) and ultrapassou_limite_velocidade_radar
)

                
'''
RANGE:
Representa a distância que fica um pouco antes e um 
pouco depois de onde o radar pega.
''' 

if carro_multado:
    print('Multado!')
else:
    print('Passou pelo radar dentro do limite de velocidade.')