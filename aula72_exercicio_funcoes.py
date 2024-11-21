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



'''
Uma empresa precisa calcular o preço final 
de seus produtos após aplicar descontos 
diferentes para cada cliente. O sistema 
deve permitir configurar a porcentagem de 
desconto uma vez e usá-la para calcular o 
preço final de vários produtos sem precisar 
reconfigurar o desconto toda vez.

'''

def calcular_preco_produto(valor_do_produto):
    def calcular_total_com_desconto(percentual_desconto):
        return valor_do_produto * (1 - (percentual_desconto/100))
    return calcular_total_com_desconto

desconto_20_porcento = calcular_preco_produto(100)
print(f'{desconto_20_porcento(20):.2f}')
desconto_30_porcento = calcular_preco_produto(100)
print(f'{desconto_30_porcento(30):.2f}')