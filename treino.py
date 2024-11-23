pessoa1 = {}

pessoa1['nome'] = 'Carlos'
pessoa1['sobrenome'] = 'Alvarenga'

print(pessoa1)

del pessoa1['nome']
print(pessoa1)

print(pessoa1.get('sobrenome'))
