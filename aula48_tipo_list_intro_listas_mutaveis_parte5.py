# Exemplo de manipulação apenas com o uso
# de referência e sem o uso de cópia:
lista_a = ['João', 'Carlos', 'Sabrina']
lista_b = lista_a
print(lista_b)

lista_a[0] = 'Alvarenga'
print(lista_b)

string1 = 'Valor da String 1'
string2 = string1
print(string2)


# Exemplo de manipulação com 
# o uso de cópia:
lista_c = ['José', 'Peixoto', 'Marcos']

lista_d = lista_c.copy()

lista_c[0] = 'Amanda'

print(lista_c)

print(lista_d)

'''
Foi invocado o método "copy()" na variável lista_c "lista_c.copy()" 
para criar a "lista_d". O método .copy() cria uma cópia rasa da 
lista original, o que significa que "lista_d" é uma nova lista 
com os mesmos elementos da lista original no momento da cópia, 
"mas as duas listas são independentes". Quando você altera 
"lista_c[0]" para 'Amanda', apenas lista_c é afetada, enquanto 
"lista_d" mantém seus valores originais. Por isso, "lista_c" 
é ['Amanda', 'Peixoto', 'Marcos'] e "lista_d" é ['José', 'Peixoto', 'Marcos'].
A lógica é a seguinte: "A partir do momento que se cria uma cópia, 
se cria um outro objeto, pois uma 'cópia' não é o 'original'",


Uma "referência" significa que duas variáveis apontam para o 
mesmo objeto na memória. Ou seja, qualquer modificação feita 
em uma, afeta a outra. Já uma "cópia" (como no caso de lista_c.copy())
cria um novo objeto na memória, independente do original. 
Daí, alterações em uma não refletem na outra.

Em Python, "variáveis mutáveis" (como "listas", "dicionários") 
podem ser alteradas após serem criadas, o que significa que 
"operações feitas em uma 'referência' afetarão o objeto original". 
Já "variáveis imutáveis" (como "tuplas", "strings") não podem ser 
alteradas após a criação.

Quando você trabalha com cópias de variáveis mutáveis, 
a independência das cópias se torna crucial para evitar 
alterações indesejadas. Com variáveis imutáveis, isso não 
é um problema, já que suas referências sempre apontarão 
para o mesmo valor.
'''