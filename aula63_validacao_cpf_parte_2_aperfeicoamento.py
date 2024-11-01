'''
"EXPRESSÃO REGULAR"

Expressões regulares em Python são 
padrões de busca definidos por uma 
sequência de caracteres que permitem 
localizar e manipular texto de forma 
eficiente. Elas são usadas com o 
módulo "re(regular expression)" 
para tarefas como validação 
de formatos e extração de informações 
específicas.

'''
import os

import re
 # FUNÇÃO  "sub()" DO MÓDULO "re"

# A função sub() do módulo re em Python substitui 
# todas as ocorrências de um padrão em uma string 
# por outra string. Essencialmente, é usada para 
# busca e substituição de texto usando expressões regulares


# PARÂMETROS DA FUNÇÃO "sub()":

# pattern: O padrão de busca (expressão regular).
# repl: A string para substituir o padrão encontrado.
# string: A string na qual a busca e substituição serão feitas.

import sys
# O módulo sys em Python fornece funções e variáveis 
# para manipular diferentes partes do ambiente de tempo 
# de execução do Python, como interagir com a entrada e 
# saída do sistema.
cpf_invalido = True
NUMERO_DIGITOS_CPF = 11
NUMERO_PARTE_COMPOSICAO_DIVISOR = 10
NUMERO_LIMITE_RESTO_DIVISAO = 9
NUMERO_PARA_EXCEDENTE = 0
POSICAO_NONO_DIGITO_CPF = 9
POSICAO_DECIMO_DIGITO_CPF = 10
QTDE_NUMEROS_CPF_SEM_DIGITOS = 9
indice_lista = 0
contador_regressivo1 = 10
contador_regressivo2 = 11
somatorio_resultados1 = 0
somatorio_resultados2 = 0
cpf_str = ''
while cpf_invalido:
    cpf_str = input('\nDigite os números do cpf:')
    if not cpf_str:
        os.system('cls')
        print('Você não digitou "nada". Portanto o programa será encerrado.')
        #Usando a função "exit()" do módulo "sys":
        sys.exit('\n"Programa encerrado."\n')
    # Usando a função "sub()" do módulo "re":
    cpf_str = re.sub(r'[^0-9]', '', cpf_str)
    if not cpf_str:
        os.system('cls')
        print('O CPF precisa ser composto "apenas" por números. Por favor, tente novamente.')
        continue
    if len(cpf_str) != NUMERO_DIGITOS_CPF:
        os.system('cls')
        print('\nVocê não digitou exatamente 11 números.')
        continue
    numeracao_sequencial_repetida = cpf_str[:9] == (cpf_str[0] * QTDE_NUMEROS_CPF_SEM_DIGITOS)
    if numeracao_sequencial_repetida:
        os.system('cls')
        print('Os 9 primeiros números do CPF não podem ser idênticos. Tente novamente.')
        continue
    cpf_invalido = False
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



