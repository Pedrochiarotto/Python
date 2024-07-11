"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2 #Concatenação de listas
print (lista3)

lista1.extend(lista2) #Agrupamento de lista(Lista 1 está recebendo no seu proprio valor a lista2)
print(lista1)