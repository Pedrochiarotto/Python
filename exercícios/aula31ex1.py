"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("Insira um número inteiro: ")

if numero.isdigit():
    numero_int = int(numero)

    if numero_int % 2 == 0:
        print("Este número é par")
    else:
        print("Este número é ímpar")
else:
    print("Você não digitou um número inteiro.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""



hora = input("Que horas são? ")
hora_int = float(hora)

if hora_int >= 0 and hora_int < 12: 
    print("Bom dia!")
elif hora_int >= 12 and hora_int <18:
    print("Boa tarde!")
else:
    print("Boa noite!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu primeiro nome: ")
nomeQnt = len(nome) #função para medir quantidade de caracteres

if nomeQnt > 1:
    if  nomeQnt <= 4:
        print("Seu nome é curto.")
    elif nomeQnt > 4 and nomeQnt <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")   
else:
    print("Digite seu nome por favor.")



    
