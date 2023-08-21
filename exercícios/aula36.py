"""
Repetições
- while(enquanto)
Executa uma ação enquanto por verdadeira
loop infinito -> enquanto um while não tem fim 
break -> quebra o while
"""

contador = 0

while contador < 100: 
    contador += 1 

    if contador == 0:
        continue               # serve para "Pular" o código que vem após o continue
    print(contador)

    if contador == 50: 
        break

print("Acabou")