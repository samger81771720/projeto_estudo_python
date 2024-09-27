"""
                    Formatação básica de strings
s - string
d - int
f - float

x ou X - Hexadecimal

(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro


Sinal + ou -
Ex.: 0>-100,.1f ou 0>+100,.1f 

Sinal de "=" força o sinal de "+" ou de "-" a aparecer antes dos zeros.


Conversion flags(SERÃO ESTUDADOS MAIS A FRENTE EM AULAS POSTERIORES):  
--->  !r (chama o método "repr") 
--->  !s (chama o método "str") 
--->  !a (chama o método "asc")



"""


variavel = 'ABCD'

# print de uma simples formatação
print(f'{variavel}')

# print de uma formatação usando um "pad"
# pad --> "Largura fixa na variável"
print(f'{variavel: >10}')
'''
    No exemplo acima inseriu 7 espaços a esquerda usando um
    espaço " " e o operador de ">", pois os três outros caracteres
    já se encontravam preenchidos pelas letras "ABC" 

'''

print(f'{variavel: <10}.')
'''
    No exemplo acima ocorreu o oposto do exemplo anterior e foi inserido
    um "." para mostrar a existência dos espaços gerados a direita.
'''

print(f'{variavel: ^10}.')
'''
    No exemplo acima o conteúdo da variável foi centralizado de acordo
    com a soma dos espaços axcrescentados nas extremidades:
    "3 espaços + ABCD + 3 espaços"
'''

print(f'{variavel:$<10}')
print(f'{variavel:0>10}')
print(f'{variavel:+^10}')
'''
    O exemplo acima evidência que, além de espaços, qualquer outro
    caracter pode ser utilizado.
'''

print(f'{1000.65555641414:+,.1f}')
''' 
    No exemplo acima o sinal de "+" foi inserido com o objetivo de forçar
    a exibição de um número positivo.
'''

print(f'{1000.65555641414:0>+10,.1f}')
'''
    No exemplo acima repare que o sinal de "+" não 
    se posicionou totalmente a esquerda do número.
    Ele se posicionou logo após os dois zeros.
'''

print(f'{1000.65555641414:0=+10,.1f}')
'''
    No exemplo acima o sinal de "=" substituiu o sinal 
    de ">", mas não interferiu na função do sinal ">", 
    pois o mesmo continua movendo os dois "0" a esquerda. 
    O que o sinal de "=" fez foi mover o sinal de "+" 
    para o início da string.
'''




print(f'O hexadecimal de 1500 é {1500:X}(com letras maiúsculas)')
print(f'O hexadecimal de 1500 é {1500:x}(com letras minúsculas)')

numero_inteiro = 20
print(f'Esse é um número inteiro: {numero_inteiro:d}')

numero_float = 20.256978
print(f'Esse é um número float: {numero_float:.2f}')
'''
    Os prints acima mostram exemplos de formatação de números
    utilizando as f-strings. 
'''


# "Conversion flags" SERÃO ESTUDADOS MAIS A FRENTE, EM AULAS POSTERIORES.
print(f'{variavel!r}')
print(f'{variavel!s}')
print(f'{variavel!a}')

print('\n')

