'''
    "INTRODUÇÃO AO DESEMPACOTAMENTO"

    --->  Desempacotando listas []
'''

lista_estados = ['Rio de Janeiro','Santa Catarina','São Paulo']

# "Desempacotar" - Extrair cada valor, criando variáveis 
# independentes para armazená-las:
estado1, estado2, estado3 = lista_estados

# Observe que para cada índice 
# foi criada uma respctiva variável
# a qual armazenou de acordo com a 
# ordem de cada índice presente na lista "[]"
print(estado1)
print(estado2)
print(estado3)
print('\n')

# Outra forma de desempacotar, porém essa 
# forma somente pode ser usada na impressão:
print(*lista_estados)

# Pode ser feito tbm dessa forma suprimindo os colchetes[]:
cidade1, cidade2, cidade3 = 'Curitiba', 'Porto Alegre', 'João Pessoa'
print('Primeiro exemplo de desempacotamento de cidades:\n')
print(cidade1)
print(cidade2)
print(cidade3)
print('\n')
# ou
print('\nSegundo exemplo de desempacotamento de cidades:\n')
print(cidade1,cidade2,cidade3)

# Criando uma variável de resto "resto_jogadores"
# para "empacotar" apenas um valor para a variável
# "jogador1":
jogador1, *resto_jogadores = ['Pelé', 'Garrincha','Maradona']
# Essa "variável de resto" irá armazenar uma "outra lista", composta
# pelos valores restantes, ou seja, será uma outra variável a ser
# criada para armazenar uma outra lista.

print('\n')
print(jogador1)
print(resto_jogadores)
print('\n')


# Por conveção quando a variável de resto não
# vier a ser usada, utiliza-se então o símbolo
# de "_" para evidenciar isso no código:
cerveja1, *_ = ['Brahma', 'Antartica','Skol']
print(cerveja1)
# Aqui foi impresso, mas não havia necessidade, devido a declaração "_"
print(_)
print('\n')


# Utilizando o símbolo "_" para pular índices
_, _, cantor_segundo_indice, *_ = [
    'Reginaldo Rossi',
    'Fábio Junior',
    'Ronnie Von',
    'Roberto Carlos',
    'Tom Jobim',
    'Caetano Veloso'
]
print(cantor_segundo_indice)
print('\n')
# Observe que aqui os outros restanrtes
# não foram impressos, devido cada declaração "_"

# Pegando o primeiro e o último índice
primeiro_indice, *_, ultimo_indice  = [
    'Reginaldo Rossi',
    'Fábio Junior',
    'Ronnie Von',
    'Roberto Carlos',
    'Tom Jobim',
    'Caetano Veloso'
]
print(ultimo_indice)
print('\n')
# Observe como o uso do '*_' é versátil 
# e pode ser usado de diversar maneiras


# Variável de resto vazia pois não há mais índices 
# a serem acessados:
_, _, frutas, *_ = ['maçã', 'banana', 'morango']
print(frutas)
print(_)
print('\n')

