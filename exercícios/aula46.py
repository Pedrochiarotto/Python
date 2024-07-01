#Listas em python!!
#Tipo list - mutável
#Suporta diversos valores de qualquer tipo 

"""
Métodos: append, insert, pop, del, clear, extend, +
"""

string = 'abcde' #5 caracter (len)
# lista = list()
lista = [123,True, 'Luiz', 4.56]
print(lista)
# print(bool(lista))
# print (lista, type(lista))

#Consultar um elemento da lista\/, por exemplo o elemento 2 entre []
print (lista[2], type(lista[2]))

#Alterar valor de um elemento na lista
lista[2] = 'Pedro'
print(lista[2])