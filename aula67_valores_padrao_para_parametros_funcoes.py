"""
             "Valores padrão para parâmetros de funções"

Ao definir uma função, os parâmetros podem
ter valores padrão. Caso não seja enviado 
um argumento para o parâmetro, "o argumento 
padrão será usado".

Refatorar =  "editar o seu código".

"None" em Python é um tipo especial que 
representa a ausência de um valor ou um valor nulo.

"Um não-valor geralmente se refere a algo como "None" em Python."

"""

# Observe o argumento nomeado(keyword) "c":
def multiplicar(a,b, c = 0): # "c" foi definido sem nenhum valor
    if c:
        print(f'{a = } | {b = } | {c = } / multiplicação = ', a * b * c)
    else:
        # Apenas esse trecho será executado
        print(f'{a = } | {b = } | {c = } / multiplicação = ', a * b)
    print('\n',a,b,c,'\n')

multiplicar(1,5,0)
# Tal fato ocorre porque a condição "c = 0" 
# representa a um valor do tipo "falsy"

# É comum criar funções em python e definir um 
# valor para algum determinado parâmetro como sendo "um não-valor"
# É uma maneira de indicar que uma variável ou um parâmetro 
# não tem um valor válido ou está "vazio". Isso pode ser 
# útil como valor padrão para parâmetros opcionais em funções 
# e o exemplo acima ilustra bem isso.



#  Outro exemplo usando agora o valor "None"
def saudacao(nome, mensagem = None):
    if mensagem is None:
        mensagem = "Olá"
    print(f"{mensagem}, {nome}!")

saudacao("Maria")
saudacao("João", "Bom dia")
# Abaixo, os argumentos estão fora de ordem e são nomedados:
saudacao(mensagem="Hi", nome = 'André')


# Uma vez definindo um parâmetro com valor padrão dentro do ()
# todos os demais parâmetros que vierem depois dele deverão ser parâmetros com valor padrão.
# Tal estrutura abaixo apresentaria um erro:
'''
def numeros(num1, num2 = 0, num3):
    print(num1,num2,num3)
'''