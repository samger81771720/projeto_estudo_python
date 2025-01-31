a = 'A'
b = 'B'
numero = 1.1


'''
Procurando agora de acordo com o nome do parâmetro nomeado:
'''

string4 = '\n Por parâmetro nomeado: Letra b = {LETRA_B}, numero = {NUMEROS:.2f} e a Letra a = {LETRA_A}'

''' 
    Já nesse outro exemplo, os mesmos argumentos "a", 
    "b" e "c" agora estão relacionados a parâmetros que 
    foram nomeados.
'''


format4 = string4.format(LETRA_B = b, LETRA_A = a, NUMEROS = numero)


string5 = 'ESSE É O NÚMERO = {NUMEROS:.4F}, LETRA B = {LETRA_B} E LETRA C  = {LETRA_C}'

print(string5)