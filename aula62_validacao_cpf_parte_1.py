import os
cpf_invalido = True
NUMERO_DIGITOS_CPF = 11
NUMERO_PARTE_COMPOSICAO_DIVISOR = 10
NUMERO_LIMITE_RESTO_DIVISAO = 9
NUMERO_PARA_EXCEDENTE = 0
POSICAO_NONO_DIGITO_CPF = 9
POSICAO_DECIMO_DIGITO_CPF = 10
indice_lista = 0
contador_regressivo1 = 10
contador_regressivo2 = 11
somatorio_resultados1 = 0
somatorio_resultados2 = 0
cpf_str = ''
while cpf_invalido:
    try:
        cpf_str = input('\nDigite os números do cpf:')
        cpf_str = cpf_str.replace('.','').replace('-','')
        cpf_int = int(cpf_str)
        if len(cpf_str) != NUMERO_DIGITOS_CPF:
            os.system('cls')
            print('\nVocê não digitou exatamente 11 números.')
            continue
        if cpf_str[:9] == cpf_str[0] * 9:
            os.system('cls')
            print('Os 9 primeiros números do CPF não podem ser idênticos. Tente novamente.')
            continue
        cpf_invalido = False
    except ValueError:
        os.system('cls')
        print(
            '\nO cpf precisa ser composto apenas por números, ' \
            ' ou, "opcionalmente" separá-lo com pontos e travessão.')
        continue
for digito in cpf_str[:POSICAO_NONO_DIGITO_CPF]:
    somatorio_resultados1 += int(digito) * contador_regressivo1
    contador_regressivo1 -= 1
    indice_lista += 1
indice_lista = 0
for digito in cpf_str[:POSICAO_DECIMO_DIGITO_CPF]:
    somatorio_resultados2 += int(digito) * contador_regressivo2
    contador_regressivo2 -= 1
    indice_lista += 1
divisor = somatorio_resultados1 * NUMERO_PARTE_COMPOSICAO_DIVISOR
resto_divisao = divisor % NUMERO_DIGITOS_CPF
penultimo_digito_cpf = resto_divisao if (resto_divisao <= NUMERO_LIMITE_RESTO_DIVISAO) else NUMERO_PARA_EXCEDENTE
divisor = somatorio_resultados2 * NUMERO_PARTE_COMPOSICAO_DIVISOR
resto_divisao = divisor % NUMERO_DIGITOS_CPF
ultimo_digito_cpf = resto_divisao if (resto_divisao <= NUMERO_LIMITE_RESTO_DIVISAO) else NUMERO_PARA_EXCEDENTE
cpf_formatado = f'{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{penultimo_digito_cpf}{ultimo_digito_cpf}'
print(f'{penultimo_digito_cpf}')
print(f'{ultimo_digito_cpf}')
if cpf_str == cpf_str[:9] + str(penultimo_digito_cpf) + str(ultimo_digito_cpf):
    os.system('cls')
    print(
        f'\nO cpf {cpf_formatado} foi devidamente verificado ' \
            'e está em conformidade com as regras da Receita Federal.\n'
    )
    # exemplo de cpf válido 74682489070
else:
    print('CPF inválido, tente novamente.')
    # exemplo de cpf inválido 74682489071
