'''
------------------------------------------------------
        Funções de Primeira Classe (First-Class Functions)

Em Python, funções de primeira classe são funções que 
são tratadas como objetos comuns, ou seja, elas podem:

*** Ser atribuídas a variáveis.

*** Ser passadas como argumentos para outras funções.

*** Ser retornadas por outras funções.
------------------------------------------------------
        Funções de Ordem Superior (Higher Order Functions)

Funções de ordem superior são funções que:

*** Podem receber outras funções como argumentos.

*** Podem retornar funções como resultado.
------------------------------------------------------

'''
                # Funções de Primeira Classe (First-Class Functions)


# ATRIBUINDO FUNÇÕES A VARIÁVEIS:
def mensagem1(texto):
    return texto
variavel_msg1 = mensagem1('texto da função mensagem1')
print(variavel_msg1)


def mensagem2(texto):
    return texto
variavel_msg2 = mensagem2
# Observe, nesse caso, que foi adicionado 
# um parâmetro para "variavel_msg2"
outra_variavel_msg2 = variavel_msg2('texto da função mensagem2')
print(outra_variavel_msg2)
print(variavel_msg2('texto da função mensagem2'))


# outro exemplo:
def somar(x, y):
    return x + y
# Atribuindo uma função a uma variável
minha_funcao = somar
# Passando a função como argumento
def executar_funcao(func, a, b):
    return func(a, b)
resultado = executar_funcao(minha_funcao, 10, 5)
print(resultado)  # Saída: 15



#############################################################################


            # Funções de Ordem Superior (Higher Order Functions)


def mensagem3(texto):
    return texto
# PASSANDO UMA FUNÇÃO COMO UM ARGUMENTO:
def executa_funcao(funcao, texto):
    return funcao(texto)
variavel_executa_funcao = executa_funcao(mensagem3,'texto da função mensagem3')
print(variavel_executa_funcao)




def mensagem4(texto1, texto2):
    return f'{texto1}{texto2}'
# CRIANDO UMA FUNÇÃO "executa_funcao2"
# QUE EMPACOTA OS ARGUMENTOS DA CHAMADA EM "*args"
# E OS DESEMPACOTA AO CHAMAR A FUNÇÃO RECEBIDA COMO PARÂMETRO:
def executa_funcao2(funcao,*args):
    return funcao(*args)
variavel_executa_funcao2 = executa_funcao2(mensagem4,'"argumento da variável _texto1_ da função mensagem4"', ' "argumento da variável _texto2_ da função mensagem4"')
print(variavel_executa_funcao2)

print(
    executa_funcao2(
        mensagem4,'"argumento da variável _texto1_ da função mensagem4"', \
            ' "argumento da variável _texto2_ da função mensagem4"'
    )
)

# outro exemplo:
def aplicar_operacao(func, valor):
    return func(valor)
def dobro(x):
    return x * 2
resultado = aplicar_operacao(dobro, 5)
print(resultado)  # Saída: 10















