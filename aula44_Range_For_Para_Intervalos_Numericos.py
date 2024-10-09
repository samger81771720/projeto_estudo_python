#                            FUNÇÃO "range()"

# range ---> range(start, stop, step)

# start -> "Refere-se ao valor onde se deseja iniciar"
# stop ->  "Refere-se ao valor onde se deseja parar"
# step ->  "Refere-se ao número de vezes para alternar a iteração"

# O primeiro índice é sempre "0", ou seja, se um intervalo de 
# valores compreender entre 0 e 7, ex.: "intervalo = range(0, 7)" 
# o primeiro índice será "0"(e seu respectivo valor será "1"),
# o último índice será "6" cujo respectivo valor será "6" e 
# o valor da variável "step" será 1"

# "Para encontrar o "número do índice" de "stop" 
# subtraia o valor declarado dentro do parâmetro por 1"



            # "OBSERVAÇÕES BEM IMPORTANTES": 

# 1ª Observação:

# Para "acessar" o valor dentro do intervalo declarado, 
# o mesmo deve ser feito por meio do "índice correspondente". 
# Os índices além de começarem sempre em "0" 
# também podem ser positivos e negativos(o que alterará a
# direção da iteração).


# 2ª Observação:

# Por exemplo: Suponha que um determinado intervalo termine em 
# "5"(numeros = range(5)) o primeiro valor do intervalo será 
# contado no índice "0" de "numeros", ou seja: "numeros[0] = 0"
# e o último será contado no índice 4 de "numeros", ou seja:
# em "numeros[4] = 4"




# Se apenas um valor for declarado no parâmetro este será reconhecido 
# como sendo o valor de "stop" e o valor "start" será "0" e o de "step"
# será "1".
primeira_faixa_de_numeros = range(10)
# "primeira_faixa_de_numeros" passará a representar um intervalo de 
# valores que, no caso do exemplo acima, será de "0" à "10", pois 
# "inicia no 0(start = 0) vai até 10(stop = 10) e não pula 
# nenhum valor(step = 0)", lembrando que os índices serão contados de 
# "0" à "9" e os valores também, no caso, serão de "0 à 9".

segunda_faixa_de_numeros = range(5,10)
# "segunda_faixa_de_numeros" passará a representar um intervalo de 
# valores que, no caso do exemplo acima, será de "5" à "10", pois 
# "inicia no "índice 5"(start = 5) vai até o "índice 9"(stop = 10)
#  e não pula nenhum valor(step = 1)" 


terceira_faixa_de_numeros = range(5,10,2)
# "terceira_faixa_de_numeros" passará a representar um intervalo de 
# valores que no caso do exemplo acima será de "5" à "10", pois 
# "inicia no "índice 5"(start = 5), vai até o "índice 9"(stop = 10)
#  e pula 2 índices(step = 2)" 


quarta_faixa_de_numeros = range(-10,-2)
# Também é possível iterar no sentido negativo por 
# meio da inserção do sinal negativo "-"

quinta_faixa_de_numeros = range(-1,-10,-2)
# Também é possível pular índices no sentido negativo 
# usando sinal negativo na variável step("-2").
# Porém torna-se necessário declarar índices negativos.

print('\n', primeira_faixa_de_numeros)

print('\n', segunda_faixa_de_numeros)

print('\n', terceira_faixa_de_numeros, '\n')

print('\n', quarta_faixa_de_numeros, '\n')


# No caso da estrutura de repetição "for in" 
# os valores da variável "primeira_faixa_de_numeros" 
# estão sendo acessados diretamente e "um valor" 
# é iterado a cada rodada(iteração).
# Obs.: A variável de iteração("iterável"), no caso
# abaixo "valor",pode receber qualquer nome desejado.
for valor in primeira_faixa_de_numeros:
    print('1º for in: ',valor)
    # 1º for in

print('\n')

# Imprimindo do índice 5 ao índice 9
for valor in segunda_faixa_de_numeros:
    print('2º for in: ',valor)
    # 2º for in

print('\n')

# Nesse caso começou no índice 5, pulou 
# 2 índices, parou no índice 7. Em seguida
# pulou mais dois índices e parou no índice 9
for valor in terceira_faixa_de_numeros:
    print('3º for in: ',valor)
    # 3º for in


print('\n')

# Invertendo o sentido por meio do sinal "-"
for valor in quarta_faixa_de_numeros:
    print('4º for in: ',valor)
    # 4º for in

print('\n')

# Pulando índices no sentido inverso
for valor in quinta_faixa_de_numeros:
    print('5º for in: ',valor)
    # 5º for in


print('\n')