"""

Flag (Bandeira) - Marcar um local

None = Não valor

is e is not = é ou não é (tipo, valor, identidade)

id = Identidade

"""

'''

Quando uma variável é criada na verdade 
é reservado na memória um espaço(com nome) 
para guardar um valor. Essa variável passa 
a ter uma identidade. É possível visualizar 
essa identidade na memória utilizando a função
"id()"

'''





v1 = 'a'
v2 = 'a'

print(id(v1))
print(id(v2))

'''
Como as duas variáveis("v1" e v2") possuem 
o mesmo valor o interpretador direciona a 
identificação da variável "v2" para ser a 
mesma identificação da variável "v1", pois 
ambas possuem o mesmo valor em comum, ou seja,
elas apontam para o mesmo valor na memória.
'''


v3 = 'b'
print(id(v3))
'''
Observe que ao criar uma outra variável("v3") 
com um outro valor diferente do valor das 
variáveis "v1 e "v2", é criada uma nova 
identificação para essa nova variável.
'''



condicao = True

# "passou_no_if" é uma marcação de um local no código,
#  ou seja uma "flag"
passou_no_if = None

if condicao:
    passou_no_if = True
    print('\nFaça algo')
else:
    print('\nNão faça algo')


if passou_no_if is not None:
    print('\nPassou dentro do bloco if\n')
    print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('\nNão passou dentro do bloco if\n')
    print(passou_no_if, passou_no_if is None)

print('\n')
    
