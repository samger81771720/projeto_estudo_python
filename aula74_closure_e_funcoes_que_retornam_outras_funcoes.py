'''
    Closure(fechamento) e funções que retornam outras funções


 Um closure em Python é uma função interna que "lembra" 
 o ambiente onde foi criada, mesmo após a execução da 
 função externa. Isso ocorre porque a função interna 
 captura as variáveis não locais (do escopo da função externa) 
 usadas por ela.

 No contexto, o "ambiente" refere-se às variáveis do escopo externo 
 da função interna. Ou seja, quando dizemos que um closure 
 "lembra o ambiente", significa que ele captura e mantém 
 uma referência às variáveis da função externa (não locais) 
 que são usadas dentro da função interna.

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


# O valor de y é definido quando chamamos a função closure.
# No exemplo anterior, quando usamos soma(5), estamos passando 
# 5 como argumento para a função interna. Assim, y recebe o valor 5.



# Observe outra forma no exemplo abaixo:
def criar_saudacao2(saudacao, nome):
    def frase_saudacao2():
        return f'{saudacao}, {nome}'
    # Aqui a função "frase_saudacao2" 
    # "não está sendo executada", ou seja, 
    # "o seu corpo não está sendo executado", 
    # ela está sendo apenas retornada, mas "lembrando 
    # o ambiente", ou seja, ela captura e 
    # mantém uma referência às variáveis da 
    # função externa (não locais) que são usadas 
    # dentro da função interna. Como "frase_saudacao2"
    # está sem o () a função não está sendo executada.
    # Observe abaixo no return:
    return frase_saudacao2

# Cada uma das duas variáveis abaixo aponta
# para a função correspondente na memória.
# Observe os prints abaixo:
saudacao3 = criar_saudacao2('Bom dia','André')
saudacao4 = criar_saudacao2('Boa noite', 'André')
print(saudacao3)
print(saudacao4)

# Agora efetuando "Closure"
print(saudacao3())
print(saudacao4())




# Outro exemplo, mas agora fazendo 
# um melhor aproveitamento de um closure:
def criar_saudacao3(saudacao):
    def frase_saudacao4(nome):
        return f'{saudacao}, {nome}'
    return frase_saudacao4

saudacao_bom_dia = criar_saudacao3('Bom dia')
saudacao_boa_noite = criar_saudacao3('Boa noite')

# Efetuando "Closure"
print(saudacao_bom_dia('João'))
print(saudacao_boa_noite('João'))

# Ou:
for nome in ['Catarina', 'Joana', 'Maria', 'Amanda']:
    print('\n',saudacao_bom_dia(nome))
    print(saudacao_boa_noite(nome))