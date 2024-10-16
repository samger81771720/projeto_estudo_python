"""
Exercício

Exiba os índices da lista

"""

lista = ['Carlos','André', 'João', 100, 100.23, False]
qtde_indices_da_lista = len(lista)
indices = range(qtde_indices_da_lista)

for indice in indices:
     print(f'Índice: {indice} --> {lista[indice]} / Tipo: {type(lista[indice])}')  



     
