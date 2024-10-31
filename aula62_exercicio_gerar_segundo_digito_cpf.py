"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import os
cpf_invalido = True
NUMERO_DIGITOS_CPF = 11
NUMERO_PARTE_COMPOSICAO_DIVISOR = 10
NUMERO_LIMITE_RESTO_DIVISAO = 9
NUMERO_EXCEDENTE = 0
POSICAO_DECIMO_DIGITO_CPF = 10
indice_lista = 0
contador_regressivo = 11
somatorio_resultados = 0
while cpf_invalido:
    try:
        cpf_str = input('\nDigite os números do cpf:')
        cpf_str = cpf_str.replace('.','').replace('-','')
        cpf_int = int(cpf_str)
        if len(cpf_str) != 11:
            os.system('cls')
            print('\nVocê não digitou exatamente 11 números.')
            continue
        cpf_invalido = False
    except ValueError:
        os.system('cls')
        print('\nO cpf precisa ser composto apenas por números.')
        continue
for digito in cpf_str[:POSICAO_DECIMO_DIGITO_CPF]:
    somatorio_resultados += int(digito) * contador_regressivo
    contador_regressivo -= 1
    indice_lista += 1
divisor = somatorio_resultados * NUMERO_PARTE_COMPOSICAO_DIVISOR
resto_divisao = divisor % NUMERO_DIGITOS_CPF
ultimo_digito_cpf = resto_divisao if (resto_divisao <= NUMERO_LIMITE_RESTO_DIVISAO) else NUMERO_EXCEDENTE


print(somatorio_resultados)
print(divisor)
print(f'{cpf_str[:10]=}')
print('\n')
print(ultimo_digito_cpf)

