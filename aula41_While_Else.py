'''
Nessa configuração onde o "while" e o "else" estão trabalhando juntos,
o bloco "else" somente será executado quando a condição "while" for 
False.

Obs importante: Nessa configuração mencionada anteriormente, caso o "break" 
seja inserido dentro do while a cláusula "else" não será executada.

'''

string = 'Valor qualquer'
extensao_da_string = len(string)

i = 0

'''
# EXEMPLO SEM O USO DO "BREAK" NO CONTEXTO
while i < extensao_da_string:
    letra = string[i]
    print(letra)
    i += 1
else:
    print('EXEMPLO 1: Essa impressão foi dentro do bloco do "else".')

print('EXEMPLO 1: Essa impressão foi fora do "while" e do "else".\n')
'''

# EXEMPLO COM O USO DO "BREAK" NO CONTEXTO
while i < extensao_da_string:
    letra = string[i]
    if letra == ' ':
        print('Foi encontrado um "espaço" e o laço foi interrompido.')
        break
    print(letra)
    i += 1
else:
    print('EXEMPLO 2: Essa impressão foi dentro do bloco do "else".')

print('EXEMPLO 2: Essa impressão foi fora do "while" e do "else".')

