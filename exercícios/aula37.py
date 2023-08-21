"""
Repetições
- while(enquanto)
Executa uma ação enquanto por verdadeira
loop infinito -> enquanto um while não tem fim 
break -> quebra o while
"""

qntlinhas = 5
qntColunas = 5

linha = 1
while linha < qntlinhas: 
    coluna = 1
    while coluna <= qntColunas:
        print(f"{linha=} {coluna=}")
        coluna += 1
    linha += 1

print("Acabou")

   