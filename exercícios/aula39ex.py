"""Calculadora com while"""


while True:
    num1 = input("Qual o primeiro digito? ")
    num2 = input("Qual o segundo digito? ")
    operador = input("Qual operação você deseja efetuar? [Escolha entre os operadores lógicos + - * /]")


    numero_valido = None
    numero1 = 0
    numero2 = 0
        

    try:
        numero1 = float(num1)
        numero2 = float(num2)
        numero_valido = True
      
    except: 
        numero_valido = None

    if numero_valido is None:
        print("Um ou ambos os números digitados não são válidos")
        continue

    operadorperm = "+ - * /"

    if operador not in operadorperm:
        print("Digite apenas os operadores permitidos!")
        continue

    if len(operador) > 1:
        print("Digite apenas 1 operador!")
        continue

    ###
    if operador == "+":
        conta = numero1 + numero2
        print(conta)
    elif operador == "-":
        conta = numero1 - numero2
        print(conta)
               

    elif operador == "*":
        conta = numero1 * numero2
        print(conta)
            

    else:
        conta = numero1 / numero2
        print(f'{conta}')

    sair = input ("Desejar sair? ").lower().startswith('s')
    if sair is True:
        break

    
    




    



