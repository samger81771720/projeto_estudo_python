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
    print(f"{chave}: {valor}")


# utilizando uma chave "dinâmica":
chave = 'Estado Civil'
pessoa1[chave] = 'casado'
print('\n',pessoa1)
# ou:
print('\n',pessoa1[chave])