# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com 

pessoa = {
    'nome': 'André',
    'sobrenome': 'Sampaio',
    'idade': 46,
    'altura': 1.76,
}

print('\n0 -->')
print(pessoa)

# Acessando um índice com o método "get".
# Por padrão retorna None caso o índice 
# não exista:
print('\n1 -->')
if pessoa.get('conta bancaria'):
    print(pessoa['conta bancaria'])
else:
    print(pessoa.get('conta bancaria'))

# Também é possível passar um outro 
# valor padrão, caso não exista o índice:
print('\n2 -->')
if pessoa.get('conta bancaria'):
    print(pessoa['conta bancaria'])
else:
    print(pessoa.get('conta bancaria', 'Índice "conta bancaria" não existe.'))

# Forma mais usual de tratar a condicional acima:
print('\n3 -->')
if pessoa.get('conta bancaria') is None:
    print(pessoa.get('conta bancaria', 'Primeira opção: "Índice "conta bancaria" não existe".'))
    # Ou:
    print('Segunda opção: "A chave "conta bancaria" não existe".')
else:
    print(pessoa['conta bancaria'])


# Apagando uma chave e retornando o valor
# da chave a qual foi excluída do dicionário
# com o método "pop":
print('\n4 -->')
valor_da_chave_excluida = pessoa.pop('sobrenome')
print(valor_da_chave_excluida)
print(pessoa)


# Apagando a última chave do dicionário
# e retornando uma tupla contendo a chave
# e o respectivo valor com o método "popitem":
print('\n5 -->')
valor_da_ultima_chave = pessoa.popitem()
print(valor_da_ultima_chave)
print(pessoa)

print('\n6 -->')
# Método "update" usando chaves contendo
# com pares de chave e valor em formato
# string:
pessoa.update({
    # Atualiza o valor de chave(s) existente(s):
    'nome': 'João',
    # Cria nova(s) chave(s):
    'sexo': 'Masculino',
})
print(pessoa)


print('\n7 -->')
# Método "update" usando argumentos nomeados:
pessoa.update(
    nome = 'Alberto',
    idade = 50,
    endereco = 'Rua dos lagos, nº 101.',
)
print(pessoa)


print('\n8 -->')
# Método "update" para inserir
# ou atualizar "iteráveis".

# Dentro da tupla o campo a esquerda
# representa a chave e o da direita
# representa o valor:
tupla1 = ('estado_civil', 'Casado'),
pessoa.update(tupla1)
print(pessoa)
# OU:
tupla2 = ('tipo_sanguineo', 'B-'),('local_nascimento','Rio de Janeiro')
pessoa.update(tupla2)
print('\n',pessoa)
# OU:
tupla3 = (('tipo_sanguineo', 'B+'),('escolaridade','Superior'))
pessoa.update(tupla3)
print('\n',pessoa)
# OU:
pessoa.update((('tipo_sanguineo', 'a+'),('escolaridade','Pós-Graduação')))
print('\n',pessoa)


# Incluindo e atualizando listas seguindo
# a mesma lógica anterior das tuplas:
print('\n9 -->')
lista_com_listas = [['tipo_sanguineo', 'ab'],['idade',30],['pais_origem','Brasil']]
#['tipo_sanguineo', 'ab'],['escolaridade','Mestrado']
pessoa.update(lista_com_listas)
print(pessoa)


# Tentando acessar um valor de uma chave 
# que não existe por meio dos colchetes,
# surge um erro de chave(KeyError):
print('\nÚltimo -->')
print(pessoa['profissao'])
