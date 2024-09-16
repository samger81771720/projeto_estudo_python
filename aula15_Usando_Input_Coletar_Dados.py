                        #  A função input "retorna uma string" 



nome = input('\nQual é o seu nome? ')

print(f'\nO nome da pessoa é {nome}.\n')

#Dessa outra forma é possível imprimir o nome da variável e o respectivo valor.
print(f'O nome da pessoa é {nome = }.\n')





'''
Como a função input retorna apenas strings, todas as variáveis que forem igualadas
a essa função, como no exemplo: numero_1 = input('Digite um número qualquer: ') ,
serão automaticamente identificadas pelo interpretador como "strings". Passe o mouse
sobre a variável que foi igualada para comprovar.

'''
numero_1 = input('Digite um número qualquer: ' )

numero_2 = input('Digite um outro número qualquer: ')

print(f'A soma dos números não é {numero_1 + numero_2}. O que ocorreu aqui foi uma concatenação, pois se tratam de strings.\n')


''''''
int_numero_1 = int(numero_1)

int_numero_2 = int(numero_2)


print(f'Aqui a soma dos números {int_numero_1} e {int_numero_2} de fato é {int_numero_1 + int_numero_2}, pois nesse caso foi feito o type casting.\n')





