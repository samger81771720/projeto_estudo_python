# Desempacotamento em chamadas de métodos e funções

string = 'JLMNOPQ'

lista = ['Gol', 'Fusca', 'Passat']

tupla = 'André', 'Luiz', 'Geraldo', 'Sampaio' 

lista_variada = [
    ['Maria', 'Helena',],
    ['Elaine',],
    ['Luiz', 'João', 'Eduarda', (9,5,56,83,48)],
]


# Desempacotando uma lista:
print('Desempacotando uma lista por meio da estrutura "for in" usando o parâmetro "sep" da função print:')
for nome in lista:
    print(nome, end = ' ')


# O operador * na função print() é conhecido 
# como o operador de desempacotamento (ou "unpacking"). 
# Ele pega todos os elementos da lista e os passa como 
# argumentos individuais para a função 
print('\n\nDesempacotando uma lista com o operador de desempacotamento "*":')
print(*lista)   
# Por padrão, o print() adiciona um espaço entre 
# cada argumento quando eles são impressos, o que 
# explica o espaço entre "Gol", "Fusca" e "Passat".


# Outro exemplo, mas agora com uma string:
print('\n\nDesempacotando uma string com o operador de desempacotamento "*":\n')
print(*string)

# Outro exemplo, mas agora com uma tupla:
print('\n\nDesempacotando uma tupla com o operador de desempacotamento "*":\n')
print(*tupla)


print('\n\nDesempacotando várias listas com o operador de desempacotamento "*" \ne usando o parâmetro "sep" da função print para gerar quebras de linha:\n')
print(*lista_variada, sep = '\n')

print('\n')