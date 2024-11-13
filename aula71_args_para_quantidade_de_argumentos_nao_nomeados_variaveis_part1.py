'''

"args" - Argumentos não nomeados(É possível 
passar uma qtde "ilimitada" de argumentos para 
a função)

* - *args (empacotamento e  desempacotamento)

'''

# Forma mais usual de desempacotar, já vista antes:
x, y, *resto = 1,2,3,4
print(x,y,resto)

# termo "args" é um termo convencionado 
# para "argumentos não nomeados" para a função:
def soma(*args):
    # Observe que o que existe em "args" é uma "tupla"
    print(args, type(args))
    # também é possível fazer conversão para uma lista:
    lista_args = list(args)
    print(lista_args)
# iterando sobre a tupla:
    for numero in args:
        print(numero)


# EMPACOTANDO ARGUMENTOS NÃO NOMEADOS(args):
soma(1,2,3,4,5,6,7,8,9)