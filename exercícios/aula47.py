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

lista = [10,20,30,40]

lista[2] = 300
print(lista[2])
del lista[2] # del é usado para remover qualquer item da lista(Não recomendado usar em lista grandes por conta da grande quantia de processamento que seria utilizado)
print(lista)
print(lista[2])

lista.append(50) #Append é utilizado para adicionar itens no final da lista
print(lista)
lista.pop() #Pop Remove o ultimo item da lista 
print(lista)

lista.insert(0, 5) #Inser para inserir elementos em qualquer item da lista(Nao recomendado usar em listas grandes por conta da grande quantia de processamento que seria utilizado) Argumentos: (Indice, valor)

lista.clear() #Clear para limpar a lista
print(lista)