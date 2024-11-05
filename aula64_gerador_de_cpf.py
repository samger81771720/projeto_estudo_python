# O módulo random, em Python, fornece funções 
# para gerar números aleatórios, criar escolhas 
# aleatórias e embaralhar sequências, útil para 
# simulações e jogos.
import random

# A função randint() do módulo random em Python 
# retorna um número inteiro aleatório dentro de 
# um intervalo especificado, inclusivo em ambos 
# os extremos. Ex.: random.randint(0,9) números
# que estejam entre 0 e 9.

NUMERO_DIGITOS_CPF = 11
NUMERO_PARTE_COMPOSICAO_DIVISOR = 10
NUMERO_LIMITE_RESTO_DIVISAO = 9
NUMERO_PARA_EXCEDENTE = 0
POSICAO_NONO_DIGITO_CPF = 9
POSICAO_DECIMO_DIGITO_CPF = 10
lista_cpf = []
cpf_str = ''
contagem = 1
for i in range(100):
    cpf_str = ''
    somatorio_resultados1 = 0
    somatorio_resultados2 = 0
    contador_regressivo1 = 10
    contador_regressivo2 = 11
    for i in range(9):
        # função randint() do módulo random
        cpf_str += str(random.randint(0,9))
    for digito in cpf_str[:POSICAO_NONO_DIGITO_CPF]:
        somatorio_resultados1 += int(digito) * contador_regressivo1
        contador_regressivo1 -= 1
    divisor = somatorio_resultados1 * NUMERO_PARTE_COMPOSICAO_DIVISOR
    resto_divisao = divisor % NUMERO_DIGITOS_CPF
    condicao_penultimo_digito = resto_divisao <= NUMERO_LIMITE_RESTO_DIVISAO
    penultimo_digito_cpf = resto_divisao if (condicao_penultimo_digito) else NUMERO_PARA_EXCEDENTE
    cpf_str = cpf_str + str(penultimo_digito_cpf)
    for digito in cpf_str[:POSICAO_DECIMO_DIGITO_CPF]:
        somatorio_resultados2 += int(digito) * contador_regressivo2
        contador_regressivo2 -= 1
    divisor = somatorio_resultados2 * NUMERO_PARTE_COMPOSICAO_DIVISOR
    resto_divisao = divisor % NUMERO_DIGITOS_CPF
    condicao_ultimo_digito = resto_divisao <= NUMERO_LIMITE_RESTO_DIVISAO
    ultimo_digito_cpf = resto_divisao if (condicao_ultimo_digito) else NUMERO_PARA_EXCEDENTE
    cpf_str = cpf_str + str(ultimo_digito_cpf)
    cpf_nove_primeiros_digitos_formatados = f'{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}'
    cpf_dois_ultimos_digitos_formatados = f'{penultimo_digito_cpf}{ultimo_digito_cpf}'
    cpf_formatado = f'{cpf_nove_primeiros_digitos_formatados}-{cpf_dois_ultimos_digitos_formatados}'
    lista_cpf.append(cpf_formatado)
for i in lista_cpf:
    print(f'CPF nº {contagem}:', i)
    contagem +=1
