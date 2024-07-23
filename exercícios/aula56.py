
"""
split - divide uma frase em determinado caracter
join - une uma string 

"""
frase = 'Olha só que, coisa interessante'

lista_palavras_cruas = frase.split(',') #Parametro aonde quer quebrar a frase(Caso deixar em branco, quebrara nos espacos em brancos)

lista_palavras = []

for i, frase in enumerate(lista_palavras_cruas):
   lista_palavras.append(lista_palavras_cruas[i].strip())

print(lista_palavras_cruas)
print(lista_palavras)

frases_Unidas = ' - '.join(lista_palavras)

print(frases_Unidas)