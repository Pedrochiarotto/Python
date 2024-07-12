"""
Introdução ao empacotamento e desempacotamento
"""

nomes = ['Pedro', 'Joao', 'Maria']

# nome1, nome2, nome3 = nomes -> Desempacotamento de todos os nomes

_, nome2, *resto = nomes  #Para pegar somente um valor, é necessario criar uma variavel para pegar o resto da lista, criando uma outra lista. a variavel _ também é uma variavel auxiliar
print(nome2)