"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

(Operador Ternário resolve essa parte abaixo)
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import os
cpf_invalido = True
lista_manipulacao_numeros = []
NUMERO_DIGITOS_CPF = 11
NUMERO_PARTE_COMPOSICAO_DIVISOR = 10
NUMERO_LIMITE_RESTO_DIVISAO = 9
NUMERO_EXCEDENTE_RESTO_DIVISAO = 0
contador_progressivo = 0
contador_regressivo = 10
somatorio_resultados = 0
str_nove_primeiros_digitos_cpf = ''
while cpf_invalido:
    try:
        cpf_str = input('\nDigite os números do cpf:')
        cpf_str = cpf_str.replace('.','').replace('-','')
        cpf_int = int(cpf_str)
        if len(cpf_str) != 11:
            os.system('cls')
            print('\nVocê não digitou exatamente 9 números.')
            continue
        cpf_invalido = False
        nove_primeiros_digitos_cpf = cpf_str[:9]
    except ValueError:
        os.system('cls')
        print('\nO cpf precisa ser composto apenas por números.')
        continue
for digito in nove_primeiros_digitos_cpf:
    lista_manipulacao_numeros.append(int(digito) * contador_regressivo)
    somatorio_resultados += lista_manipulacao_numeros[contador_progressivo]
    contador_regressivo -= 1
    contador_progressivo += 1
composicao_do_divisor = somatorio_resultados * NUMERO_PARTE_COMPOSICAO_DIVISOR
resto_divisao = composicao_do_divisor % NUMERO_DIGITOS_CPF
penultimo_digito_cpf = resto_divisao if (resto_divisao <= NUMERO_LIMITE_RESTO_DIVISAO) else NUMERO_EXCEDENTE_RESTO_DIVISAO







print(lista_manipulacao_numeros)
print(somatorio_resultados)
print(composicao_do_divisor)
print(nove_primeiros_digitos_cpf)
print(resto_divisao)
print('\n')
print(penultimo_digito_cpf)


#746.824.890-70
#123.456.789-09(resulta em 0)

