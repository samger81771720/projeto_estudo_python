# Métodos úteis dos dicionários em Python:

# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe



'''Em Python, dunder é um termo informal usado para se 
referir a "double underscore". Esse termo 
é originado da combinação de "double underscore" em 
inglês, e é frequentemente usado para se referir a 
nomes de métodos e atributos especiais que começam 
e terminam com dois underscores (__).'''

carro = {
    'cor': 'prata',
    'ano': '2019',
    'modelo': 'Ônix',
    # Observe abaixo que há uma série de repetições 
    # de um mesmo nome de chave. Por isso,
    # o interpretador irá apenas "atualizando" 
    # o valor da mesma chave até que a última 
    # atualização é que será de fato considerada:
    'marca': 'Chevrolet1',
    'marca': 'Chevrolet2',
    'marca': 'Chevrolet3',
    'marca': 'Chevrolet4',
}
print('1 --> ',carro)


# Exemplo de método dunder: __len__()
qtde_chaves_dict = carro.__len__()
print('\n2 --> ',qtde_chaves_dict)

# Python usando a função len() para 
# retornar esse método de dentro
# do dicionário:
print('\n3 --> ',len(carro))



# Método "keys()" retorna uma
# visualização das chaves
#  em um dicionário:
print('\n4 --> ',carro.keys())
# iterando sobre a lista de chaves:
chaves = carro.keys()
print('\n5 --> ')
for chave in chaves:
    print(f'{chave}: {carro[chave]}')



# Método "values()" retorna uma
# visualização dos valores das 
# chaves de um dicionário:
print('\n6 --> ',carro.values())

# iterando sobre a lista de valores:
valores = carro.values()
print('\n7 --> ')
for valor in valores:
    print(valor)



# O método "items" tbm retorna uma "lista"
#  que contém "tuplas" dos pares
#  chave-valor em um dicionário:
pares = carro.items()
print('\n 8 --> ',pares)

# iterando sobre a lista com 
# tuplas do método "items()":
print('\n 9 --> ')
for par in pares:
    print(par)

# ou desempacotando:
print('\n 10 --> ')
for chave, valor in pares:
    print(f'{chave}: {valor}')


# O método "setdefault()"" é utilizado 
# para obter o valor de uma chave 
# em um dicionário. Se a chave não
# estiver presente, ele insere a 
# chave com um valor padrão que
# pode ser especificado e retorna esse valor:
carro.setdefault('numero_chassi', '999888777666555')
print('\n11 --> ',carro)

# O novo par a ser associado tbm 
# pode ser armazenado numa variável:
preco = carro.setdefault('preco', '60000')
print('\n12 --> ',preco)
print('\n13 --> ',carro)

# Se a chave já existir no dicionário 
# o valor não será substituído por 
# nenhum outro valor padrão declarado
#  no método:
print(carro.setdefault('cor','azul'))
print('\n14 --> ', carro)



# É possível também fazer coerções
#  de um dicionário em outros tipos:
print('\n --> ')
print(tuple(carro))
print(list(carro))
# ou:
print('\n --> ')
print(tuple(carro.keys()))
print(tuple(carro.values()))
print(tuple(carro.items()))

print('\n')