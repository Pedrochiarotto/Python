"""
for + range
range -> range(start, stop, step)
"""

numeros = range(10) #range(stop) de 0 a 10
numeros = range(2,10) #range(start e stop)inicia no '2' e termina no 10
numeros = range(2,10,2) #range(start,stop e step) inicia no '2', termina no 10 e pula de 2 em 2

for numero in numeros: 
    print(numero)