# f-strings(formatação de texto)
#colocando o f antes do argumento da string, e colocando as variáveis em chaves, não é necessario usar virgulas. 
 

nome = "Pedro"
altura = 1.84
peso = 79
imc = peso / (altura * altura)

print(nome, "Tem", altura,"de altura, pesa", peso,"quilos e seu IMC é", imc)

linha = f"{nome} Tem {altura} de altura pesa {peso} quilos e seu IMC é {imc:.4f}"#podemos usar ":.xf" para escolher quantas casas decimais depois dos pontos.
 

print(linha)