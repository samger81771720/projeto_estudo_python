"""

Operadores de atribuição:

=  

+= 

-= 

*= 

/= 

//= 

**= (Potenciação)

%= (Resto da Divisão)


"""

contador = 10
contador += 2
print(f'Aqui o operador gera uma soma: {contador}')


contador_str = '10'
contador_str += '2'
print(f'Aqui o operador gera uma concatenação: {contador_str}')


contador = 10
contador *= '2'
print(f'Aqui o operador multiplica a qtde de "2" por 10: {contador}')


contador = 10
contador %= 3
print(f'Aqui acha o resto da divisão: {contador}')


contador = 10
contador **= 2
print(f'Aqui faz a potenciação: {contador}')


