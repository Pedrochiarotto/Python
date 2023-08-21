"""
Repetições
- while(enquanto)
Executa uma ação enquanto por verdadeira
loop infinito -> enquanto um while não tem fim 
break -> quebra o while
"""
condicao = True
while condicao: 
    nome = input("Qual o seu nome? ")
    print(f"Seu nome é: {nome}")

    if nome == "sair":
        break

print("123")
