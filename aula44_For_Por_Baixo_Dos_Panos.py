'''
Iterável --> Elemento que entrega um valor de cada vez
            str, range, etc
            
Iterador --> "__iter__()" ou "iter()"
'''

texto = 'abc'.__iter__()
# ou
texto = iter('abc')

print(texto)
'''
Retorna no console:

"<str_ascii_iterator object at 0x0000023B715458D0>"

Traduzindo: A expressão "str_ascii_iterator object" é 
um objeto que é o iterador da str que está nesse endereço 
de memória "0x0000023B715458D0"
'''