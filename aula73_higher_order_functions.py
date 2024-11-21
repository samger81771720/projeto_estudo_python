'''
------------------------------------------------------------------

        Funções de Primeira Classe (First-Class Functions)

Funções tratadas como valores, podendo ser 
atribuídas a variáveis, passadas como 
argumentos ou retornadas.

------------------------------------------------------------------

        Funções de Ordem Superior (Higher Order Functions)

Higher-Order Functions: Funções que recebem 
outras funções como argumento ou as retornam.

------------------------------------------------------------------

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
# ou:
print(variavel_msg2('texto da função mensagem2'))


# outro exemplo:
def somar(x, y):
    return x + y
# Atribuindo uma função de primeira classe a uma variável
minha_funcao = somar
def executar_funcao(func, a, b):
    return func(a, b)
# Passando a função como argumento
resultado = executar_funcao(minha_funcao, 10, 5)
print(resultado)  # Saída: 15



#############################################################################


            # Funções de Ordem Superior (Higher Order Functions)


def mensagem3(texto):
    return texto
# RECEBENDO UMA FUNÇÃO COMO UM ARGUMENTO:
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
print(resultado)  


# outro exemplo
def desconto_10(preco):
    return preco * 0.9

def imposto_5(preco_com_desc):
    return preco_com_desc * 1.05

def calcular_precos(func_desconto, func_imposto,*precos_base):
    lista_precos_finais = []
    for preco in precos_base:
        preco_com_desconto = func_desconto(preco)
        preco_final = func_imposto(preco_com_desconto)
        lista_precos_finais.append(preco_final)
    return lista_precos_finais

precos = calcular_precos(desconto_10, imposto_5, 10, 30, 50)   
print(f'Lista com os preços finais: {precos}')















