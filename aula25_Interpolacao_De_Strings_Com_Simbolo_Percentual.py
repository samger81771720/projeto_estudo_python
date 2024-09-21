"""

" Interpolação é o processo de inserir valores 
de variáveis dentro de uma string. Em Python, 
temos diferentes sintaxes para realizar essa tarefa,
cada uma com suas particularidades e melhor utilizada 
em diferentes contextos. O uso do "%" é um outro tipo
pelo qual é possível fazer a interpolação.


s - string

d e i - int

f - float

x e X - Hexadecimal (ABCDEF0123456789)
(HEXADECIMAL -->  Números e letras de "A à F" e de "0 à 9")


"""

nome = 'André'
preco = 1000.95897643
varivel = '%s, o preço é R$%.2f' % (nome, preco)


print(varivel)

print('\n')

# Sem acescentar zeros
print('O hexadecimal do número inteiro %d é %x' % (15, 15))

# Acrescentando zeros ("0" é o número desejado para aparecer e "4" é o números de vezes que o zero irá aparecer, mas subtraído pela qtde de casas decimais do número já existente.)
print('O hexadecimal do número inteiro %d é %04x' % (15, 15))

# Nesse exemplo está sendo mostrada a variáção de exibição de letra maiúscula para representar o número hexadecimal.)
print('O hexadecimal do número inteiro %d é %X' % (1500, 1500))

print('\n')