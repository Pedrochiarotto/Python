"""
Interpolação básica de strings 
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = "Pedro"
preco = 15.60
variavel = "%s, o preço é R$: %.2f" % (nome, preco)

print(variavel)