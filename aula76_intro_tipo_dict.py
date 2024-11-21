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
# num dicionário.

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

# Acessando valores por suas chaves:
print('\n',pessoa1["sobrenome"])

# Adicionando um novo par de chave-valor:
pessoa1["telefone"] = "99999-9999"
print('\n',pessoa1)

# Atualizando um dado existente:
pessoa1["altura"] = 1.8
print('\n',pessoa1)

# removendo um par chave-valor:
del(pessoa1["sobrenome"])
print('\n',pessoa1)

print('\n')
# iterando sobre as chaves do dicionário:
for chave in pessoa1:
    print(chave,':')
    print(pessoa1[chave])


print("\n")

# Gerando tuplas para cada par:
print("\n")
for chave_valor in pessoa1.items():
    print(f"{chave_valor}")
print("\n")
# Como num dicionário cada item é um par chave-valor
# O método "items()" de um dicionário retorna
# esses pares como tuplas e o loop for
# precisa desembrulhar cada tupla.


# Desempacotando e iterando sobre as chaves e valores:
print("\n")
for chave,valor in pessoa1.items():
    print(f"{chave}:{valor}")
