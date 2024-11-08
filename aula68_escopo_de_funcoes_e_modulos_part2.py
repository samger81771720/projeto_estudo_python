'''
Em Python, uma função interna pode acessar 
variáveis da função externa onde foi definida. 
Esse acesso ocorre devido ao conceito de escopo 
léxico, onde a função interna "lembra" o ambiente 
onde foi criada, mesmo que seja chamada 
posteriormente em um contexto diferente. 
Assim, a função interna consegue acessar variáveis 
de funções englobantes sem recebê-las como parâmetros 
diretamente.
'''

# Variável global
global_var = "Global"

def func_externa():
    # Variável no escopo da função externa
    externa_var = "Externa"

    def func_intermediaria():
        # Variável no escopo da função intermediária
        intermediaria_var = "Intermediária"

        def func_interna():
            # Variável no escopo da função interna
            interna_var = "Interna"
            
            # Acessa todas as variáveis dos escopos anteriores
            print("Variável interna:", interna_var)
            print("Variável intermediária:", intermediaria_var)
            print("Variável externa:", externa_var)
            print("Variável global:", global_var)

        # Chama a função interna
        func_interna()

    # Chama a função intermediária
    func_intermediaria()

# Chama a função externa
func_externa()



# Observe que o acesso foi obtido 
# "de dentro para fora", pois do 
# contrário não é possível. Descomente 
# o código abaixo e veja:

'''
def func_externa():
    externa_var = "Externa"

    def func_interna():
        interna_var = "Interna"
        print("Dentro de func_interna:", interna_var)

    # Acessa a variável externa_var aqui
    print("Dentro de func_externa:", externa_var)

    # Tenta acessar interna_var diretamente, o que gera um erro
    print("Tentando acessar interna_var fora de func_interna:", interna_var)

# Chama a função externa
func_externa()
'''