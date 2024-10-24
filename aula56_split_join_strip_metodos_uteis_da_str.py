"""

split, strip e join com list e str

split - O método split() divide uma string em uma 
"lista" de substrings com base em um delimitador 
especificado. "Por padrão, o delimitador é o espaço". 


strip( ) - O método strip() remove espaços em branco 
(ou caracteres especificados) do início e do fim de 
uma string. Útil para limpar entradas de usuário.

join - O método join() concatena elementos 
usando um delimitador específico. 

"""

frase1 = 'Python uma linguagem de dados.'
lista_de_palavras = frase1.split()
print('Usando a função split():\n', lista_de_palavras)


frase2 = 'Python uma linguagem de dados, porém difere de Java.'
lista_de_frases1 = frase2.split(',')
print('\nUsando a função split() com o delimitador ","\n', lista_de_frases1)
print('A vírgula que aparece é da "lista" que foi gerada.\n')


frase3 = (
    ' Python uma linguagem de dados. Java também é bem interessante. Linguagens muito utilizadas. '
    )
lista_de_frases2 = frase3.split('.')
print('\nUsando a função split() com o delimitador "."\n', lista_de_frases2)




frase4 = (
    '     Primeira parte da frase    .       Segunda parte da frase         '
    )
lista_de_frases3 = frase4.split('.')

print('\n')
for i, frase in enumerate(lista_de_frases3):
    print('Sem espaços no início e no fim:')
    print(lista_de_frases3[i].strip())

print('\n"Lista de frases3" com espaços no início e no fim:')
print(lista_de_frases3)


print('\n')
for i, frase in enumerate(lista_de_frases3):
    print('Sem espaços a direita:')
    print(lista_de_frases3[i].rstrip())

print('\n"Lista de frases3" com espaços no início e no fim:')
print(lista_de_frases3)


print('\n')
for i, frase in enumerate(lista_de_frases3):
    print('Sem espaços a esquerda:')
    print(lista_de_frases3[i].lstrip())

print('\n"Lista de frases3" com espaços no início e no fim:')
print(lista_de_frases3)



print('\n')
# "PRÁTICA POUCO RECOMENDÁVEL"
# Alterando a própria lista a partir do 
# da aplicação do método strip() sobre 
# ela mesma e atribuindo a mesma lista 
# após as alterações a cada iteração:
for i, frase in enumerate(lista_de_frases3):
    lista_de_frases3[i] = lista_de_frases3[i].strip()

print('\n"Lista de frases3" sem espaços no início e no fim:')
print(lista_de_frases3)



print('\n')
# "PRÁTICA RECOMENDÁVEL"
# Criando uma nova lista:3

lista_de_frases4 = list()
# ou
lista_de_frases4 = []

for i, frase in enumerate(lista_de_frases3):
    lista_de_frases4.append(lista_de_frases3[i].strip())  

print('\n"Lista de frases4" sem espaços no início e no fim:')
print(lista_de_frases4)

print('\n')



# Método "join()""
letras = '-'.join('abcdefg')
print('\nAplicando o método join() para concatenar os elementos de uma string usando o delimitador "-":')
print(letras)


frase_concatenada = '-'.join(lista_de_frases4)
print('\nAplicando o método join() para concatenar os elementos de numa lista usando também o delimitador "-":')
print(frase_concatenada)


print('\n')