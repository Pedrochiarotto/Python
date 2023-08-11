"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input("Vou dobrar o número que você digitar: ")

try:
    numeroFloat = float(numero)
    print(f"O dobro de {numero} é {numeroFloat * 2}")
except:
    print("Você não digitou um número.")

    #Se o dado que receber no input, não for compativel com o código que está no try, altomaticamente ele irá para o execpt ao invés de dar "error" 

                    #OU 

    """if numero.isdigit():
    numeroFloat = float(numero)
    print(f" O dobro de {numero} é {numeroFloat * 2}")
else:
    ("Você não digitou um número.")"""