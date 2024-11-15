# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar_argumentos(*args):
    total_multiplicacao = 1
    for valor in args:
        total_multiplicacao *= valor
    return total_multiplicacao
print(multiplicar_argumentos(5,3,2,1,4))


# Crie uma função que define se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_impar(numero):
    numero_verificado = 0
    try:
        numero_verificado = int(numero)
    except ValueError:
        return 'Vc não digitou um valor númerico.'
    multiplo_de_dois = numero_verificado % 2 == 0
    if multiplo_de_dois:
        return f'O número {numero_verificado} é par.'
    return f'O número {numero_verificado} é ímpar.'
print(par_impar(100))
print(par_impar('y'))