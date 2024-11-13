def soma(*args):
    print(args)
    total = 0
    for numero in args:
        total += numero
    return total

numeros = 1,2,3
outra_soma = soma(numeros)
print(outra_soma)