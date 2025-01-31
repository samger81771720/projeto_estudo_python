'''

Interpolação é o processo de inserir valores 
de variáveis dentro de uma string. Em Python, 
temos diferentes sintaxes para realizar essa tarefa,
cada uma com suas particularidades e melhor utilizada 
em diferentes contextos. O uso do método "format()" é 
um outro tipo pelo qual é possível fazer a interpolação.


Em Python, format() é um método associado a strings. 
Ele é utilizado para formatar strings de forma concisa 
e flexível, permitindo a inserção de valores de variáveis 
em posições específicas dentro de uma string.

Associação a objetos: Métodos são funções que pertencem 
a objetos de uma determinada classe. No caso do format(), 
ele pertence à classe str, ou seja, a todas as strings em 
Python.

Chamada: Para utilizar o método, você chama ele 
diretamente em uma string, como em string.format().



Como funciona:

String de formato: Você cria uma string com marcadores 
de posição, indicados por chaves {}. 



Valores a serem inseridos: 

Dentro do método format(), você passa os valores que serão 
inseridos nesses marcadores.



Substituição: 

O método format() substitui os marcadores de posição 
pelos valores correspondentes, gerando a string 
formatada final.

'''

# EXEMPLOS PRÁTICOS

a = 'A'
b = 'B'
numero = 1.1





'Seguindo pela ordem natural dos índices na "lista de argumentos", ou seja no "()"'

string1 = '\n Letra a = {}, Letra b = {} e o número = {}'

string2 = '\n Letra a = {}, Letra b = {} e o número {:.4f}'


'''
Procurando agora de acordo com a posição do 
número de cada índice do respectivo argumento 
(são argumentos pois estão representando valores 
de variáveis que já foram anteriormente declaradas) 
na lista de argumentos:
'''
string3 = '\n Pegando agora por "índices": '+'Número = {2}(índice 2),'+'Letra b = {1}(índice 1),'+'Letra a = {0}(índice 0).'


''' 
    Nesse exemplo, "a", "b" e "c" são 
    exemplos de "argumentos" passados 
    na lista de argumentos no método format.
'''
formato1 = string1.format(a, b, numero)

formato2 = string2.format(a, b, numero)

formato3 = string3.format(a, b, numero)







'''
Procurando agora de acordo com o nome do parâmetro nomeado:
'''

string4 = '\n Por parâmetro nomeado: Letra b = {letraB}, numero = {numeroNomeado:.2f} e a Letra a = {letraA}'

''' 
    Já nesse outro exemplo, os mesmos argumentos "a", 
    "b" e "c" agora estão relacionados a parâmetros que 
    foram nomeados.
'''

formato4 =  string4.format(letraA = a, letraB = b, numeroNomeado = numero)

'''
Também é possível nomear apenas uma parte dos argumentos, 
porém deverá ser obedecida a ordem da "esquerda para a direita" e
"todos os parâmetros a direita deverão ser nomeados".
'''
string5 = '\n Letra a = {0}(Não nomeado), Número = {numeroNomeado:.3f}(nomeado) e Letra b = {letraB}(nomeado)'

formato5 =  string5.format(a, letraB = b, numeroNomeado = numero)


'''Impressões'''

print(formato1)

print(formato2)

print(formato3)

print(formato4)

print(formato5)

print('\n\n')