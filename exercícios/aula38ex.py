"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

nome = input("Digite seu nome ")

indice = 0
novoNome = ""

while indice < len(nome):
    letra = nome[indice]
    novoNome += (f"*{letra}")
  
    indice += 1

print (novoNome)