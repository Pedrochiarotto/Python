"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 67  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

#Ultilizar letras maiúsculas para indicar variáveis que não devem ser mudadas

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 90  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade <= RADAR_1:
    print("O carro passou dentro da velocidade limite do radar.")
else:
    print("O carro passou acima da velocidade permitida pelo radar.")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print("Carro multado")
