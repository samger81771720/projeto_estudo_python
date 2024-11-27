'''
                "Tipo Tupla - Uma lista imutável"

    Uma tupla é uma estrutura de dados que armazena um 
conjunto de valores. Ao contrário das listas, 
que podem ser alteradas, as tuplas são imutáveis
ou seja, não podem ser modificadas após serem criadas. 
Isso torna as tuplas úteis quando você deseja uma coleção 
de itens que não devem ser alterados. 

Observações importantes:
---> "Os valores de uma tupla são imutáveis!"
---> "As regras de desempacotamento funcionam tanto 
para "listas" como para "tuplas".

'''

# Diferentemente de uma lista onde se usa os "[]" 
# logo após o sinal de "=", numa tupla os colchetes
# não são utilizados.

# Ex.: Ao invés de: 
lista_nomes = ['André', 'Sabrina', 'Theo']

# Ex.: Pode ser escrito dessa forma:
lista_nomes = 'André', 'Sabrina', 'Theo'

# Ex.: Assim como oode ser escrito dessa forma:
lista_nomes = ('André', 'Sabrina', 'Theo')


print(lista_nomes)

# Experimente tentar acessar os métodos
#  de uma lista como insert, del, clear,
# append, etc. para ver que eles não se
# encontram acessíveis para a "tupla" criada.
# ex.: digite "lista_nomes."


# Os índices podem ser acessados assim 
# como os índices de uma lista:
print(lista_nomes[1])

# Listas também podem ser convertidas para tuplas:
lista_nomes2 = ['Josué', 'Marcos', 'Mario']
print(f'Aqui a variável {lista_nomes2 = } é uma lista.')

lista_nomes2 = tuple(lista_nomes2)
print(f'Aqui a variável {lista_nomes2 = } se tornou uma tupla, pois foi convertida pela função "tuple()".')


# Assim como podem se transformar novamente numa lista.
lista_nomes2 = list(lista_nomes2)
print(f'Aqui a variável {lista_nomes2 = } se tornou novamente uma lista, pois foi convertida pela função "list()".')

# Uma simples tupla:
tupla = ()
print(tupla)

# Uma tupla que contém outra tupla 
# dentro dela(tupla de vírgula final):
tupla_com_tupla = (),
print(tupla_com_tupla)

# Uma tupla que contém outras tuplas dentro dela:
tupla_com_tuplas = (),()
print(tupla_com_tuplas)

# Uma tupla que contém outras tuplas dentro dela:
tupla_com_tuplas = (),()
print(tupla_com_tuplas)