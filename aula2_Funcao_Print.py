# Observe que a vírgula é utilizada também como um separador

# "sep" e "end" são parâmetros da função print()

# A função print tem por padrão o parâmetro "sep" como espaço.

print(12, 34, 55, end = '\r')

print(66, 77, 88, sep = '-', end = "\n\n\n")

'''
 
Imprime 123455 e move o cursor de volta ao início da linha com \r,  mas ainda na mesma linha.
O cursor está agora no início da linha e sobrescreveu qualquer conteúdo anterior.

Imprime 66-77-88 a partir do início da linha. 
Resultado:

A saída será 66-77-88, acrescida de três quebras de linha. 

O 123455 foi sobrescrito pelo \r devido ao retorno de carro (\r), que fez o cursor voltar ao início da linha antes da nova impressão.
Se você não viu 123455, pode ter sido muito rápido para perceber.

'''


print(12, 34, 55, sep = '', end = '\r\n')
print(66, 77, 88, sep='-', end = '\n\n')

'''
O processo é:

Imprime 123455 na linha atual.
Move o cursor de volta ao início da linha com \r, mas ainda na mesma linha.
Move o cursor para a próxima linha com \n, preparando o console para a próxima impressão na linha seguinte.
Então, a impressão subsequente ocorre na nova linha criada após o 123455.

'''


print(12, 34, 55, sep = '-', end = '#')
print(66, 77, 88, sep='-', end = '.\n\n')

'''
Vamos analisar o que acontece com esses dois comandos print():

print(12, 34, 55, sep='-', end='#'):

Impressão: Exibe 12-34-55.
Comportamento do end='#': Adiciona um # no final da impressão, sem pular para a próxima linha. O cursor permanece na mesma linha após o #.
print(66, 77, 88, sep='-', end='.\n\n'):

Impressão: Exibe 66-77-88.
Comportamento do end='.\n\n': Adiciona um . e depois acrescenta duas novas linhas. Isso move o cursor para a linha seguinte e adiciona uma linha em branco adicional.
Saída Final:

Linha 1: 12-34-55#
Linha 2: (Em branco)
Linha 3: 66-77-88. (depois de dois saltos de linha)
Resumo:

O primeiro print() coloca 12-34-55# na primeira linha.
O segundo print() coloca 66-77-88. e move o cursor para duas linhas em branco a partir da posição após o #.
'''