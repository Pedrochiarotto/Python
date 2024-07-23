""" 
Lista de listas e seus indices 
"""

salas = [
    ['maria', 'helena'],
    ['elaine'],
    ['Joao', 'Pedro', 'Jose', (0,2,3,4)]
]

print(salas[2] [2])
print(salas[2][3][2])

for sala in salas:
    print(sala)
    for item in sala:
        print(item)