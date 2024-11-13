'''
Passe o debuger para verificar como as 
variáveis são acessadas e a observar a 
execução:
'''
# Adicione um breakpoint:
# na linha 24(x = 12) 
# na linha 28(x = 19)
# na linha 32(x = 24)


x = 1  # Inicialmente, x é uma variável global com valor 1

# Ao definir a função escopo, o Python armazena a função 
# (incluindo o corpo, com toda a lógica contida nela)como 
# um objeto na memória alocando um espaço na memória para ela:
def escopo():
    global x  # Declara que x dentro de escopo() é a variável global x
    x = 10  # Atualiza a variável global x para 10

    # Armazenado outra função, alocando um outro espaço na memória para ela:
    def outra_funcao():
        global x  # Declara que x dentro de outra_funcao() é a variável global x
        x = 11  # Atualiza a variável global x para 11
        y = 2  # y é uma variável local de outra_funcao() e vale 2
        print(x, y)  # Imprime os valores de x e y: (11, 2)

    outra_funcao()  # Chama outra_funcao(), o que executa o código dentro dela
    print(x)  # Imprime o valor de x, que agora é 11

print(x)  # Passo 1: Imprime o valor inicial de x, que é 1
escopo()  # Passo 2: Chama a função escopo(), que altera x e chama outra_funcao()
print(x)  # Passo 3: Imprime o valor de x após a chamada de escopo(), que é 11

'''
                    Etapas detalhadas de execução:

Linha x = 1

Define a variável global x com o valor 1.
Estado: x = 1
Linha print(x) (fora de qualquer função)

Imprime o valor atual de x, que é 1.
Chamada escopo()

Entra na função escopo().
Linha global x dentro de escopo()

Declara que x dentro de escopo() se refere à variável global x.
Linha x = 10 dentro de escopo()

Atualiza a variável global x para o valor 10.
Estado: x = 10
Chamada outra_funcao() dentro de escopo()

Entra na função outra_funcao().
Linha global x dentro de outra_funcao()

Declara que x dentro de outra_funcao() se refere à variável global x.
Linha x = 11 dentro de outra_funcao()

Atualiza a variável global x para 11.
Estado: x = 11
Linha y = 2 dentro de outra_funcao()

Define a variável local y com o valor 2, que só existe dentro de outra_funcao().
Linha print(x, y) dentro de outra_funcao()

Imprime os valores de x e y, que são 11 e 2, respectivamente.
Saída de outra_funcao()

Retorna ao ponto de chamada dentro de escopo().
Linha print(x) dentro de escopo()

Imprime o valor de x, que agora é 11 (depois de ter sido alterado em outra_funcao()).
Saída de escopo()

Retorna ao ponto de chamada fora da função.
Linha print(x) (fora de qualquer função)

Imprime o valor atual de x, que é 11.
'''

