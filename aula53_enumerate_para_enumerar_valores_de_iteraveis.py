'''         
                Função enumerate - enumera "iteráveis" 
                
-----------------------------------------------------------------------

Iterável (iterable): é um objeto que pode ser percorrido 
por um loop, como listas, tuplas ou strings. Ele possui o 
método __iter__(), que retorna um iterador(iterator).

Iterador (iterator): é o objeto que faz a iteração de fato, 
retornado por __iter__(). Ele possui o método __next__() 
para acessar os elementos de iteração um por um até o final.


-------------------------------------------------------------------------

A função "enumerate" tem uma relação direta com iteráveis 
e iteradores. Ela atua da seguinte maneira:

 
A função enumerate internamente chama 
o método iter() no iterável que você passa como argumento, 
gerando um iterador. 
Depois disso, enumerate cria seu próprio iterador que, a cada 
chamada de next(), retorna uma tupla contendo o índice e o 
valor do elemento, utilizando o iterador original do iterável 
para percorrer os itens, associando um índice a cada 
elemento do iterável.

Com isso o iterador percorre índice por índice usando 
a função next() ou com um loop for. A cada iteração, 
o iterador retornado por enumerate fornece uma tupla 
contendo o índice e o valor do elemento."

--------------------------------------------------------------------------
Obs.: "Quem avança para o próximo item é a função next(). 

o método next() é chamado explicitamente por você ou pelo loop for. 
O iterador em si não "invoca o método next()" automaticamente. 

Abaixo está a sequência de como funciona por trás dos panos:

1 - Quando você usa o método iter() em um iterável (como uma lista), 
ela cria um iterador.

2 - O iterador mantém o estado atual da iteração e sabe em qual posição está.

3 - Cada vez que você chama o método next() sobre o iterador, ele:

* Acessa o item atual do iterável.
* Retorna esse item.
* Após isso o iterator aguarda a próxima chamada de next(), 
para acessar o próximo item.

4 - No caso da função enumerate, o iterador adicionalmente gera o índice 
junto com o valor.

---------------------------------------------------------------------------

'''


lista = ['A', 'B', 'C']


iterador = enumerate(lista)


# Usando a função next() para percorrer o iterador
print('Usando a função next:')
print(next(iterador))  # Saída: (0, 'A')
print(next(iterador))  # Saída: (1, 'B')
print(next(iterador))  # Saída: (2, 'C')
# NOTA: A cada iteração, "para cada objeto da lista" 
# é criada "uma tupla contendo o índice e o seu respectivo valor.
# No exemplo foram geradas três tuplas.
# OBSERVE QUE O SINAL DE PARÊNTESES E A VÍGURA QUE SEPARANDO 
# OS ELEMENTOS EVIDENCIAM UM TUPLA.


# O próximo next() daria erro porque o iterador chegou ao fim
# print(next(iterador))  # Levantaria um erro StopIteration


# Usando a estrutura for:
for indice_e_valor in iterador:
    print(indice_e_valor)
for indice_e_valor in iterador:
    print(indice_e_valor)
# Observe que em nenhuma das duas estruturas for acima nenhum 
# valor é obtido do iterator "iterador". Tal fato 
# ocorre porque o "interator" por ter sido atribuido anteriormente
# para a variável "iterador" foi completamente consumida nas chamadas 
# da função next() percorrendo todos os elementos da função "enumerate".




# uma forma de contornar o caso acima é sempre 
# criar um novo iterator diretamente no for:
print('\nAbaixo, produzidos por um constante novo iterador para ambas: ')
for indice_e_valor in enumerate(lista):
    print(indice_e_valor)
for indice_e_valor in enumerate(lista):
    print(indice_e_valor)


# Podem ser feitas conversões de um enumerate:
print('\nAbaixo, conversões de enumerate: ')
print('\nLista: ', list(enumerate(lista)))
print('\nTupla: ', tuple(enumerate(lista)))




# " Desempacotamento das tuplas com a função enumerate."
# No exemplo abaixo são gerados dois índices para cada
# tupla gerada pelo iterator, "um carregando o número 
# do índice da lista e outro carregando o valor desse 
# respectivo índice:
print('\nDesempacotamento com enumerate: ')
for valores_da_tupla_gerada in enumerate(lista):
    indice_da_lista, valor_do_indice_da_lista = valores_da_tupla_gerada
    print(indice_da_lista, valor_do_indice_da_lista)


# Os desenvolvedores Python simplificaram o processo, podendo ser
# feito da forma abaixo, onde a declaração de desempacotamento é feita
# diretamente sobrescrevendo a declaração do iterator, ou seja, ao 
# invés de declarar o iterator é declarada(s) a(s) variável(s) de
# desempacotamento onde fica subentendido para o interpretador que,
# no mesmo momento em que o iterador iterar sobre cada índice e gerar 
# uma tupla a cada iteração, será feito logo em seguida o desempacotamento 
# dessa mesma tupla e isso acontece a cada iteração:
print('\nDesempacotamento com enumerate mais simplificado: ')
for indice_da_lista, valor_do_indice_da_lista in enumerate(lista):
    print(indice_da_lista, valor_do_indice_da_lista)


