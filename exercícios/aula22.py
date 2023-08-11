# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 <- índice
#  O t á v i o
# -6-5-4-3-2-1 <- índice

nome = "Pedro"
print(nome[2])
print(nome[-2])

print("Pe" in nome)
print("zar" in nome)
print("Zar" not in nome)
print("Pe" not in nome)

Nome1 = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")
