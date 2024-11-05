"""
            "Argumentos nomeados(keywords) e não-nomeados(posicionais) em funções Python"

"Argumento nomeado" tem o nome da variável correspondente com sinal de igual"
"Argumento não-nomeado" recebe apenas o valor para preencher o parâmetro na ordem.

Parâmetro é o nome dado à variável na definição 
da função, enquanto argumento é o valor que você 
passa para essa variável ao chamar a função. Em 
resumo, parâmetros são placeholders(marcador de 
posição que será substituído por um valor real), 
e argumentos são os valores reais.

"""

# Definição da função soma:

# Def - Definição da função
# soma - Nome da função a qual se encontra alocada na memória
# (x,y,z) - Execução de função

def soma(x,y,z):
    print(f'{x = }, {y = } e {z =} | x + y + z = {x + y + z}')

# <function soma at 0x0000019F9BF5A3E0>
print('Aponta apenas o local onde a função se encontra na memória:\n',soma,'\n')

# Argumentos não nomeados: São passados na ordem correta para a função.
# Argumento posicional(não-nomeado) "1" para "x" e "2" para "y"
# Para executar a função é preciso inserir os parênteses "()":
soma(1,2,3)

# Argumentos nomeados: Especificamos o nome 
# do argumento ao passar o valor, a ordem 
# não importa:
soma(y = 5, z = 10, x = 5)

# Mesclando o uso dos nomeados e não-nomeados:
soma(1, 5, z = 2)

# "Em Python, os argumentos posicionais 
# não podem estar após os argumentos nomeados." 
# Na chamada soma(x=1, 5, z=2), o argumento 5 é 
# posicional e está vindo depois do nomeado x=1. 
# Isso não é permitido e a tentativa de execução 
# dessa linha de código geraria um erro: 
# SyntaxError: positional argument follows keyword argument
# (Erro de sintaxe: argumento posicional segue argumento de palavra-chave):

# soma(x =  1,5, z = 2)

# Em outras palavras: "Todos os argumentos 
# que vierem depois de um argumento nomeado 
# deverão ser nomeados."