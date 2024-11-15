'''
            Closure e funções que retornam outras funções

Um closure em Python é uma função que lembra 
o ambiente em que foi criada. Em outras palavras, 
é uma função interna que captura e lembra as variáveis 
do seu escopo contidas na função externa.

'''

def externa(x):
    def interna(y):
        return x + y  # 'y' recebe o valor na chamada da função closure
    return interna

soma = externa(10)  # 'x' é definido como 10
resultado = soma(5)  # 'y' é definido como 5 ao chamar a função interna
print(resultado)  # Saída: 15

# ou:
soma = externa(10)
print(soma(5))
# A função interna é um closure, 
# pois ela lembra o valor de x mesmo 
# após a função externa ter sido executada.

'''
O valor de y é definido quando chamamos a função closure. 
No exemplo anterior, quando usamos soma(5), estamos passando 
5 como argumento para a função interna. Assim, y recebe o valor 5.
'''


def criar_saudacao(saudacao, nome):
    def frase_saudacao():
        return f'{saudacao}, {nome}'
    return frase_saudacao()

saudacao1 = criar_saudacao('Olá','André')
saudacao2 = criar_saudacao('Olá', 'Sabrina')
print(saudacao1)
print(saudacao2)