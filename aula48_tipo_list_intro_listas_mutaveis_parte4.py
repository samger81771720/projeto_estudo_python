lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# Concatenando listas com o sinal de "+"
lista_c = lista_a + lista_b
print(lista_c)

# Método "extend"
# No caso do exemplo abaixo o método extende está extendendo 
# a lista_a para a lista_b
lista_a.extend(lista_b)
# Observe a lista_a está sendo extendida(unida) à lista_b
print(lista_a)
# Observe que o contrário não ocorre.
print(lista_b)


