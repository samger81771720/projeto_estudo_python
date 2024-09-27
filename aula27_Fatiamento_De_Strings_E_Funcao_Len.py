"""
                                Fatiamento de strings
 
 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p] [::]

função "len": retorna a qtd de caracteres da str

"""

variavel = 'Olá mundo'



print(variavel[4])
# Apenas acessando o índice 4



print(variavel[4:])
''' 
    Usando os ":" para realizar o fatiamento.

    "Exibindo do índice 4 em diante. Ou seja, o início é lido, mas como
    o final não foi declarado, então é lido do índice 4 até o final da 
    string."
'''


print(variavel[4:7])
''' 
    Exibindo do índice 4 até o índice "6", pois a leitura é feita 
    deduzindo um a menos. Ou seja, são declarados início e fim 
    mas do final é deduzido 1 da contagem. Será preciso acrescetar 
    1 a mais para chegar ao índice desejado, ou seja, no exemplo acima
    deveria ser "print(variavel[4:8])".
'''



print(variavel[:5])
''' 
    Exibindo do índice "4" para "trás"(invertendo a ordem). 
    Seguirá partindo do índice 4 até o início da string.
'''


print(variavel[-5:])
print(variavel[-5:-1])
print(variavel[:-1])
'''
    Exemplos usando índices com números negativos.
'''



print(len(variavel))
print(variavel[0:len(variavel)])
'''
    A função "len" é usada para determinar a qtde de caracteres.
'''




print(variavel[0:len(variavel):2])
'''
    O último argumento é o "passo"
    (De quantos em quantos caracteres irá pular.)
'''

print(variavel[::-1])
'''
    No exemplo acima como o início e o fim não foram 
    declarados com números, então o interpretador 
    entenderá que a iteração deverá ocorrer do início 
    ao fim e o "passo" seguirá uma "ordem inversa", pois 
    o número correspondente está "negativo".
'''

print('\n')
