# "\t" Usado para tabular

lista = ['A', 'B', 'C']

iterador = enumerate(lista)


for iterator1 in enumerate(lista):
    print('\tFor da tupla:')
    for iterator2 in iterator1:
        print('\t',iterator2)

