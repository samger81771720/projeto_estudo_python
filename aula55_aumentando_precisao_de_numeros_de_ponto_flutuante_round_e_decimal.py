"""
Imprecisão de ponto flutuante:
    "Essa função decimal.Decimal() em Python é usada 
para realizar operações aritméticas de alta precisão, 
especialmente úteis quando você precisa de mais exatidão 
do que os tipos float nativos oferecem. Por exemplo, em 
cálculos financeiros, onde os pequenos erros de 
arredondamento podem se somar e causar problemas. 
Com o módulo decimal, você pode controlar a precisão 
e arredondamento das operações."

"Decimal() é uma função dentro do módulo decimal." 



Double-precision floating-point format IEEE 754
(Formato de ponto flutuante de precisão dupla)

https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

"""

import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1+numero_2


'''Usando o módulo decimal(foi importado acima).'
   Esse módulo "decimal" possui uma classe interna chamada "Decimal'''
numero_4 = decimal.Decimal(0.1)
numero_5 = decimal.Decimal(0.7)
numero_6 = numero_4 + numero_5

print('Imprimindo um número de ponto flutuante:')
print(numero_3)

# 1ª Forma de eliminar a imprecisão de números flutuantes:
print('\nO valor abaixo foi formatado mas como uma string, pois uma f-string é uma string:')
print(f'{numero_3:.2f}')


# 2ª Forma de eliminar a imprecisão de 
# números flutuantes, função "round":
print(
    '\nUsando a função round(numero_3):'
    '\nCaso não informe o número de casas decimais o valor será arredondado:'
)
print(round(numero_3))

print(
    '\nUsando a função round(numero_3,2):'
    '\nInformando o número de casas decimais:'
)
print(round(numero_3,2))


print(
    '\nUsando a classe Decimal() do módulo decimal'
    '\nRepare que a precisão númerica aumentou:'
)
print(numero_6,'\n')
