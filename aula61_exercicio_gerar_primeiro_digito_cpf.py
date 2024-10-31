"""

SITE PARA GERAR CPF:
https://www.4devs.com.br/gerador_de_cpf


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
NUMERO_DIGITOS_CPF = 11
NUMERO_PARTE_COMPOSICAO_DIVISOR = 10
NUMERO_LIMITE_RESTO_DIVISAO = 9
NUMERO_PARA_EXCEDENTE = 0
POSICAO_NONO_DIGITO_CPF = 9
indice_lista = 0
contador_regressivo = 10
somatorio_resultados = 0
while cpf_invalido:
    try:
        cpf_str = input('\nDigite os números do cpf:')
        cpf_str = cpf_str.replace('.','').replace('-','')
        cpf_int = int(cpf_str)
        if len(cpf_str) != NUMERO_DIGITOS_CPF:
            os.system('cls')
            print('\nVocê não digitou exatamente 11 números.')
            continue
        cpf_invalido = False
    except ValueError:
        os.system('cls')
        print('\nO cpf precisa ser composto apenas por números.')
        continue
for digito in cpf_str[:POSICAO_NONO_DIGITO_CPF]:
    somatorio_resultados += int(digito) * contador_regressivo
    contador_regressivo -= 1
    indice_lista += 1
divisor = somatorio_resultados * NUMERO_PARTE_COMPOSICAO_DIVISOR
resto_divisao = divisor % NUMERO_DIGITOS_CPF
penultimo_digito_cpf = resto_divisao if (resto_divisao <= NUMERO_LIMITE_RESTO_DIVISAO) else NUMERO_PARA_EXCEDENTE



print(somatorio_resultados)
print(divisor)
print(f'{cpf_str[:POSICAO_NONO_DIGITO_CPF]=}')
print(resto_divisao)
print('\n')
print(penultimo_digito_cpf)


#746.824.890-70
#123.456.789-09(resulta em 0)

