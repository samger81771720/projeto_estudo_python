"""

             "Valores padrão para parâmetros de funções"

Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.

Refatorar =  "editar o seu código".

"""

# Observe que mesmo que embora o argumento "c" 
# seja nomeado(keyword), o seu valor não é 
# reconhecido na definição da função:
def multiplicar(a,b, c = 0):
    if c:
        print(f'{a = } | {b = } | {c = } / multiplicação = ', a * b * c)
    else:
        # Apenas esse trecho será executado
        print(f'{a = } | {b = } | {c = } / multiplicação = ', a * b)

multiplicar(1,5,0)
# Tal fato ocorre porque a condição, ou seja, 
# "c = 0", representa a um valor do tipo "falsy"

# É comum criar funções em python e definir um 
# valor para algum determinado parâmetro como sendo um não valor.
# É uma maneira de indicar que uma variável ou um parâmetro 
# não tem um valor válido ou está "vazio". Isso pode ser 
# útil como valor padrão para parâmetros opcionais em funções 
# e o exemplo acima ilustra bem isso.


