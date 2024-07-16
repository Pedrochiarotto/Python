"""
enumerate - enumera iteráveis (índices)
"""

nomes = ['Pedro', 'Joao', 'Maria']
nomes.append("Cleber")

#Lista_enumerada = enumerate(nomes)

for indice, nome in enumerate(nomes):
    print(indice ,nome)
