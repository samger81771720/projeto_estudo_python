# Operador "in" significa "está entre"

# Operador "not in" significa "não está entre"

# Strings são iteráveis

# Índices "Positivos":    0  1  2  3  4
# Conteúdo:               A  N  D  R  É
# Índices "Negativos":   -5 -4 -3 -2 -1

nome = 'ANDRÉ'

# Acessando os índices
print('\n')
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print('\n')
print(nome[-1])
print(nome[-2])
print(nome[-3])
print(nome[-4])
print(nome[-5])
print('\n')


# Usando o operador lógico "in"
print('A' in nome)
print('\n')

print('a' in nome)
print('\n')

print('NDR' in nome)
print('\n')


# Usando o operador lógico "not in"
print('ANDRÉ' not in nome)
print('\n')

print('João' not in nome)
print('\n')


# Mini programa exemplificativo do uso desses operadores lógicos
nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar no nome: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}.')
else:
    print(f'{encontrar} não está em {nome}')
print('\n')
