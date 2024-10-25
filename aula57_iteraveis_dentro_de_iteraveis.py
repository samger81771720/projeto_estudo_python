salas = [
    ['Maria', 'Helena',],
    ['Elaine',],
    ['Luiz', 'João', 'Eduarda', (9,5,56,83,48)],
]
print('LISTA COMPLETA "salas" que é composta por três listas:')
print(salas)

print('\nAcessando o ÍNDICE 1 de "salas" que é composto por uma lista:')
print(salas[1])

print('\nAcessando o ÍNDICE 0 da lista que o ÍNDICE 1 de "Salas" possui:')
print(salas[1][0])

print('\nAcessando o ÍNDICE 2 da lista que o ÍNDICE 2 de "Salas" possui:')
print(salas[2][2])

print('\nAcessando o ÍNDICE 1 da lista que o ÍNDICE 0 de "Salas" possui:')
print(salas[0][1])

print('\nAcessando o ÍNDICE 2 da tupla:')
print(salas[2][3][2])