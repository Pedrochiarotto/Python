primeiroValor= input("Digite um valor: ")
segundoValor= input("Digite um segundo valor: ")

Primeiro_valor = int(primeiroValor)
Segundo_valor = int(segundoValor)

if Primeiro_valor > Segundo_valor:
    valormaior = Primeiro_valor
    valormenor = Segundo_valor

elif Segundo_valor > Primeiro_valor:
    valormaior = Segundo_valor
    valormenor = Primeiro_valor
else:
    print("Os dois números são iguais!")

if valormaior == Primeiro_valor:
    print(f'{Primeiro_valor= } é maior do que {Segundo_valor= }')
else:
    print(f'{Segundo_valor= } é maior do que {Primeiro_valor= }')



