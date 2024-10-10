#               "Exemplo de como o "For" trabalha por debaixo dos panos"


# Objeto iterável
iterable = 'André'

# Objeto iterador sendo criado por meio da função iter()
iterator = iter(iterable)



# Estrutura "for" por debaixo dos panos
while True:
    try:
        next_iterator_object = next(iterator)
        print(next_iterator_object)
    except StopIteration:
        break



# Estrutura "for" 
for iterator in iterable:
    print(iterator)