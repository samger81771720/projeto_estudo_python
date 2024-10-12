"""
                            __Listas em Python__

* Tipo list - É um tipo "Mutável"

* Suporta vários valores de qualquer tipo

* Conhecimentos anteriores que podem ser reutilizáveis: "índices" e "fatiamento"

"""

#        +01234 índices positivos
#        -54321 índices negativos
string = 'ABCDE'  # 5 caracteres (len)


lista = list()
# ou
lista = []

   # índices positivos :   0º     1º      2º     3º
   # índices negativos :  -4º    -3º     -2º    -1º
lista_com_varios_tipos = [123, 'André', True, 2.3658]
                    # índices positivos:   0º     1º      2º     3º            4º
                    # índices negativos : -5º    -4º     -3º    -2º           -1º
lista_com_varios_tipos_e_com_uma_lista = [123, 'André', True, 2.3658, lista_com_varios_tipos]


# Alterando um valor de um índice numa lista:
lista_com_varios_tipos[3] = 'Aqui era o número float "2.3658" aqgora mudou para uma "string".'


# IMPRESSÕES:
print(lista, type(lista))

print(bool(lista)) 

print(bool([]))

print(lista_com_varios_tipos)

print(lista_com_varios_tipos_e_com_uma_lista)

print(lista_com_varios_tipos_e_com_uma_lista[4])

print(type(lista_com_varios_tipos[-2]))

print(lista_com_varios_tipos[1].upper())

print(lista_com_varios_tipos[3])

print(lista_com_varios_tipos)