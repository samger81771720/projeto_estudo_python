"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    str_numero_inteiro = input('Digite um número inteiro: ')
    numero = int(str_numero_inteiro) 
    numero_par = numero % 2 == 0
    if numero_par:
        print(f'\nO número {numero} é um número par.\n')
    else:
        print('\nO número %d não é um número par.\n' % numero)
except:
    print('\nVc não digitou um número inteiro.\n')

