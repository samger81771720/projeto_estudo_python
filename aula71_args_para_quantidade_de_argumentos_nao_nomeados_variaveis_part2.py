def soma(*args):
    total = 0
    for numero in args:
        total += numero
    #Usando return para retornar o total da soma:    
    return total

# EMPACOTANDO:
soma_um_a_nove = soma(1,2,3,4,5,6,7,8,9)

print(soma_um_a_nove)
# Ou:
print(soma(1,2,3,4,5,6,7,8,9))

# Curiosidade: a função sum() é uma função que 
# realiza um somatório de valores, mas desde
# que esses valores sejam "iteráveis":
print(sum((1,2,3,4,5,6,7,8,9)))

numeros = 1,2,3
# DESEMPACOTANDO PARA GERAR ARGUMENTOS NÃO NOMEADOS(args)

# Observe que foi preciso desempacotar a 
# tupla "numeros" dessa forma: " *numeros "
# para que pudessem ser gerados os argumentos 
# não nomeados e assim pudessem ser utilizados 
# no parâmetro da função soma:
outra_soma = soma(*numeros)
print(outra_soma)

