"""
                "Escopo de funções em Python"

   Escopo em Python define onde variáveis podem ser acessadas ou modificadas. 
   
   Há dois tipos principais: 
   
   * "escopo local" (dentro de funções) 
   
   * "escopo global" (fora de funções)

   É possível acessar as variável dos escopos externos, 

"""

# A variável "x" possui um escopo global,
# pois pode ser acessada em qualquer 
# parte do escopo do módulo, ou seja, 
# do arquivo em si:
x = 10

def func1():
    # Tudo o que está definindo dentro 
    # do escopo da função possui um
    # escopo apenas local:
    y = 9
    print(y)
func1()


# Observe que a variável "x" não pode 
# ser acessada, pois a mesma faz parte 
# do escopo local da função "func", 
# descomente a linha abaixo e veja:

# print(y)

def func2():
    # Acessando a variável de escopo global "x":
    print(x)
func2()

def func3():
    # Variável "x" abaixo é de escopo local, ou seja, 
    # é uma variável declarada dentro do escopo da "func3" 
    # e não tem nenhuma relação com a variável de escopo 
    # global "x = 10":
    x = 111
    y = 15
    print(x,y)
    # Definindo uma função "func4" 
    # dentro da função "func3": 
    def func4():
        x = 222
        print(x,y)
    func4()
# Observe que a função "func4" somente 
# será executada se for invocada dentro 
# da "func3" e se a "func3", posteriormente, 
# tbm for invocada, ou seja, exatamente de 
# acordo com a ordem mencionada:
func3()


# Não é boa prática de programação, mas 
# tbm é possível alterar o valor de uma 
# varíavel de escopo global ao longo do 
# código: 
def func5():
    # A expressão "global" faz com que 
    # uma variável de escopo externo 
    # seja a mesma do escopo interno:
    global x
    x = 1000
    print(x)
func5()

# Observe que logo após a execução da "func5" 
# o valor original da variável global "x" 
# que era "10" passou a ser "1000":
print(x)

# Observe que a variável "x" da func6 não foi 
# afetada pela declaração "global x" dentro do 
# corpo da func 5 onde a variável global "x" 
# passou a possuir valor "1000", pois essa 
# variável "x" de func6 possui um escopo local:
def func6():
    x = 999
    print(x)
func6()

