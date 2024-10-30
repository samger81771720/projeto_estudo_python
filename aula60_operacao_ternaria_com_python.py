"""

Operação ternária (condicional numa única linha)

<valor> if <condicao> else <outro valor>

"""


###################################################################### 
primeiro_numero = 11
segundo_numero = 10
condicao = primeiro_numero == segundo_numero
variavel = 'É uma igualdade.' if condicao else 'Não é uma igualdade.'
######################################################################

######################################################################
digito = 9
novo_digito = digito if digito <= 9 else 0

# Condição invertida, mas produzindo o mesmo resultado:
novo_digito = 0 if digito > 9 else digito
######################################################################

print(variavel)

# A operação ternária também pode ser 
# empregada também dentro da função print
print('\nValor' if True else 'Outro')

print(f'\n{novo_digito = }')

# É possível fazer aninhamentos dentro da 
# operação ternária, porém devem ser evitados, 
# pois não se trata de uma boa prárica efetuar 
# muitos aninhamentos:
print('Valor' if False else '\nOutro Valor' if False else '\nFim')
print('Valor' if 3 > 5 else '\nOutro Valor' if 1 == 10 else '\nFim')
# IMPORTANTE ---> "Qualquer condição só é válida quando é verdadeira(True)"


print('\n')

