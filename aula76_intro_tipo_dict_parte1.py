'''
    Um dict (ou dicionário) é uma coleção de pares 
    chave-valor, onde cada chave é única. É extremamente 
    útil para armazenar dados de forma organizada e 
    permitir acesso rápido aos valores associados às chaves.'''


# Dicionários em Python (tipo dict)

# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".

# Em um dicionário, a chave não representa um índice 
# como em uma lista, mas sim um identificador único 
# associado a um valor. Em uma lista, os elementos são 
# acessados por índices numéricos que começam em 0. 
# Em um dicionário, os elementos são acessados por 
# suas chaves, que podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc. Se trata de
# outra denominação de índice(chave) só que agora é 
# utilizado para acessar um determinado valor 
# "num dicionário".

# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.

# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.

# Mutável: dict, list

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }

# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')



# FORMA MAIS USADA PARA CRIAR UM DICIONÁRIO:
pessoa1 = {
    'nome': 'André',
    'sobrenome': 'Sampaio',
    'idade': 46,
    'altura': 1.76,
    'enderecos':[
        {'logradouro':'Estr. da Programação', 'número': 100},
        {'logradouro':'Rua do Programador', 'número':200},
    ],
}

# FORMA MENOS USADA PARA CRIAR UM DICIONÁRIO:
pessoa2 = dict(nome = 'João', sobrenome = 'Santos')

endereco = dict(
    logradouro = 'Estr. da Comemoração',
    número = 10,
    bairro = 'Catumbi',
)

print('\n',pessoa1)
print('\n',pessoa2)
print('\n',endereco)

