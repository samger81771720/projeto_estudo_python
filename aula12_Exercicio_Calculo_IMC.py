# IMC - Dividir o peso em quilos pela altura ao quadrado(em m)

#   IMC = peso / (altura * altura)

nome = 'André Luiz Geraldo Sampaio'

altura = 1.78

peso = 90

imc = ... # Os três pontos(Ellipsis) podem ser usados como placeholders

print(imc,'\r\n')

imc = peso / (altura ** 2)

'''
Observe no print abaixo que a concatenação pode ser 
feita tanto usando o sinal de "+" como também usando a ","
'''

print(
    nome, 'tem', altura, 'de altura',
    'pesa', peso, 'quilos e o seu IMC atual é', 
    imc, end = '.' + '\n\n'
)

