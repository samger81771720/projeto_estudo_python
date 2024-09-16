
''' AULA DE FORMATAÇÃO DE STRINGS '''

'''
    f-strings ----> "SINTAXE ESPECIAL EM PYTHON PARA FORMATAR STRINGS"

    Conceitualmente, f-strings são uma sintaxe especial 
    em Python que permite inserir valores de variáveis 
    diretamente dentro de uma string de forma clara e 
    intuitiva.

    O "f" é um modificador de string que nos 
    permite criar strings mais dinâmicas e 
    legíveis. É uma parte integrante da sintaxe 
    das f-strings em Python.

    O "f" antes de uma string em Python indica 
    que estamos utilizando uma f-string. Essa 
    sintaxe, introduzida no Python 3.6, permite 
    inserir valores de variáveis diretamente 
    dentro da string, simplificando a formatação 
    e tornando o código mais legível. As expressões 
    dentro das chaves {} são avaliadas e seus 
    resultados são inseridos na string final.
    
'''



nome = 'André Luiz Geraldo Sampaio'
altura = 1.78
altura2 = 10000000
peso = 90
imc = ... # Os três pontos(Ellipsis) podem ser usados como placeholders
print(imc,'\r\n')




'''
    Após uma variável numérica, caso seja inserido 
    ":.(número de casas decimais desejado)f", 
    define-se o número de casas decimais que será 
    apresentado na impressão. Exemplo abaixo
'''
imc = peso / (altura ** 2)
linha_1 = f'{nome} tem altura de {altura:.4f}, pesa {peso} quilos e o seu IMC atual é {imc}. \n\n'
print(linha_1)




'''
Possível também separar as casas por "," 
'''
linha_2 = f'{nome} tem altura de {altura2:,.4f}, pesa {peso} quilos e o seu IMC atual é {imc}. \n\n'
print(linha_2)




print(
    nome + ' tem', altura, 'de altura',
    'pesa', peso, 'quilos e o seu IMC atual é', 
    imc, end = '.' + '\n\n'
)





