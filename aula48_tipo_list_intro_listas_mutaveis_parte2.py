"""
                            __Listas em Python__

* Tipo list - É um tipo "Mutável"

* Suporta vários valores de qualquer tipo

* Conhecimentos anteriores que podem ser reutilizáveis: "índices" e "fatiamento"

* Métodos úteis: 
- append(acrescentar)
- insert(inserir)
- pop
- del(deletar)
- clear(limpar), extend
-  +

CRUD = "Create", "Read", "Update" and "Delete"
Criar, ler, alterar, apagar = lista[i] (CRUD)

IMPORTANTE: "EVITAR REMOVER ITENS QUE NÃO ESTEJAM 
NO FINAL DA LISTA, POIS DO CONTRÁRIO,
CASO A SUA LISTA SEJA MUITO GRANDE SERÁ DEMANDADO 
MUITO PROCESSAMENTO PARA REORGANIZAR OS VALORES QUE 
ESTIVEREM A FRENTE DO ÍNDICE REMOVIDO PARA QUE CADA
UM "VENHA A OCUPAR O ÍNDICE ANTERIOR A SUA POSIÇÃO ATUAL", 
DEVIDO À REMOÇÃO DAQUELE VALOR QUE FOI FEITA 
FORA DO FINAL DA LISTA. ISSO SE APLICA 
MAIS A LISTAS QUE SEJAM MUITO EXTENSAS. 

"""

lista = [18, 2, 91, 55]
lista2 = [99,55,66,77]
lista3 = [59,60,33]


#Atribuindo o valor de um índice da lista para uma variável
numero_do_indice_2 = lista[2]
print(f'Imprimindo a variável "{numero_do_indice_2 = }"')


# Apagando um valor da lista
del lista[3]
print(f'Imprimindo a lista após o valor do índice 3(55) ter sido removido: {lista=}')


# Apagando um valor da lista
del lista[3]
print(f'Imprimindo a lista após o valor do índice 3(55) ter sido removido: {lista=}')

# Apagando o valor do último índice da lista acessando pelo método del por meio do número 
# do índice que é -1
del lista[3]
print(f'Imprimindo a lista após o valor do índice 3(55) ter sido removido: {lista=}')


# Adicionando valores no final da lista
lista.append(50)
print(f'Imprimindo a lista após adicionar o valor "50" no último índice da lista: {lista=}')


# Removendo valores no final da lista pela função "pop"
lista2.pop()
print(f'Imprimindo a lista2 após remover o valor do último índice da lista2. O valor "77" não aparece mais: {lista2=}')

# O método "pop" retorna o tipo do valor que foi removido
# Atribuindo o valor removido do índice para uma variável.
# Se não mencionar nenhum índice dentro do parêmetro, será
# removido o vaklor do último índice.
valor_removido = lista2.pop()
print(f'Atribuindo o valor removido do último índice(66) para uma variável "{valor_removido = }", lista agora: {lista2=}')

# Removendo o índice desejado
valor_do_indice_selecionado = lista.pop(1)
print(f'Removendo o valor do índice 1(2): {lista =}')


print('\n')