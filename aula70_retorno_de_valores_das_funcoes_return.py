
"""

Retorno de valores das funções (return)

"""

def soma(x, y):
    # Emobora apareça a mensagem "oi" 
    # a função print() é usada para 
    # enviar a saída para a tela 
    # (ou outro dispositivo de saída padrão). 
    # Por padrão, "ela não retorna nenhum valor".
    # "O retorno de print() é sempre "None"
    print('oi')
    return x+y
soma1 = soma(1,2)
soma2 = soma(3,4)
print(soma1+soma2)

# Usando esrtrutura condicional(if) para criar opções múltiplas de retorno:
def divisao_num_positivos(dividendo,divisor):
    if divisor == 0:
        return 'Não é possível dividir um número por "0"'
    if dividendo < 0 or divisor < 0:
        return 'Esse método foi projetado apenas para calcular divisão de números positivos'
    # Assim como nas duas condições anteriores,
    # essa última linha apenas será executada 
    # se nenhuma das duas anteriores for
    # verdadeira.
    return dividendo/divisor

resultado_divisao1 = divisao_num_positivos(8,2)
print(resultado_divisao1)
resultado_divisao2 = divisao_num_positivos(8,0)
print(resultado_divisao2)
resultado_divisao3 = divisao_num_positivos(-8,2)
print(resultado_divisao3)




