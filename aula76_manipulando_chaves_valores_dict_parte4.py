''' 
        "Shallow Copy" vs "Deep Copy" em dados mutáveis em python
            Cópia rasa(ou suferficial) vs cópia profunda
'''

# "list" e "dict"(ambos mutáveis) possuem o método "copy"

# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro




# Para fazer uma cópia total(deep copy) de um dado 
# mutável utiliza-se um módulo chamado "copy":
import copy


imovel1 = {
    'endereco': 'Av. das Américas, nº 100.',
    'tipo': 'Apartamento',
    'lista': [1,2,3,4,5]
}

# A variável "imovel2" não está copiando 
# a variável  "imovel1" e sim apontando
# para o mesmo local na memória de "imovel1", 
# pois “imovel1” representa um dicionário, 
# que por sua vez representa um dado mutável:
imovel2 = imovel1


# Ao alterar o valor de uma 
# chave em imovel2 afetará tbm o mesmo
# valor da mesma chave em "imovel1".
# Exemplo: 

# Antes de fazer alteração em "imovel2"
print('\n 1 -->')
print(imovel1)
print(imovel2)

imovel2['endereco'] = 'Av. Lúcio Costa, nº 300.'
# Após fazer a alteração
print('\n 2 -->')
print(imovel1)
print(imovel2)
# Resumo: "Não foi feita uma cópia."




# Usando o método "copy()" 
# para fazer uma "cópia rasa":
print('\n 3 -->')

# Na linha abaixo, o método copy é método 
# de instância específico dos dicionários:
imovel2 = imovel1.copy() 

# Nessa outra linha abaixo está sendo usada 
# "a função copy()" do "módulo copy"
# (importado logo no início), que é mais 
# genérica e pode ser usada com qualquer objeto:
imovel2 = copy.copy(imovel1)

imovel2['endereco'] =  'Av. Presidente Vargas, nº 1999.'
print(imovel1)
print(imovel2)
# Faz uma cópia rasa porque copia apenas os dados 
# "imutáveis". A variável "lista" é um dado "mutável", 
# logo "não será copiada".



# No outro exemplo abaixo isso fica melhor evidenciado. 
print('\n 4 -->')
# A "lista" da variável "imovel3" não está copiando e 
# sim apontando para a "lista" da variável "imovel1". 
# Observe que ao tentar realizar uma alteração na "lista" 
# da "suposta" cópia de "imovel1", ou seja, em "imovel3" 
# a "lista" de "imovel1" tbm foi afetada:
imovel3 = imovel1.copy()
imovel3['lista'][2] = 9898989898
print(imovel1)
print(imovel3)
# Resumindo ambos dicionários "imovel1" e
# "imovel3" apontam "para a mesma lista" na
# memória.



# Usando o método "deepcopy()"
print('\n 4 -->')
# O método "deepcopy()" tbm pertence 
# ao módulo "copy" e cria uma cópia 
# independente de um objeto, copiando 
# recursivamente todos os objetos aninhados.
# Isso assegura que modificações na cópia 
# não afetem o original:
imovel4 = copy.deepcopy(imovel1)
print(imovel1)
print(imovel4)

print('\n 5 -->')
imovel4['lista'][2] = 1111111111111
print(imovel1)
print(imovel4)

print('\n')