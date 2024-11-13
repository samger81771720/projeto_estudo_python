'''
            CALL STACK(PILHA DE CHAMADAS)

    A call stack é uma estrutura de dados usada 
pelo Python (e outras linguagens de programação) 
para manter o controle das funções que estão sendo 
chamadas em um determinado momento. Ela funciona 
como uma "pilha" (ou stack) onde cada chamada de 
função é "empilhada" (inserida no topo da pilha) 
quando é chamada, e "desempilhada" (removida) 
quando a função termina.

Quando uma função é chamada, ela é empilhada 
na call stack. E, ao terminar, é removida da stack, 
permitindo que o programa continue a execução de 
onde parou.

'''
# Adicione um breakpoint:
# na linha 24(x = 1) 
# na linha 28(x = 10)
# na linha 32(x = 11)

# na aba "debuger", após iniciar o mesmo, 
# clique em "call stack" e observe 
# as funções sendo empilhadas a medida em que são
# executadas e sendo desempilhadas a medida
# que cada uma termina a sua execução.

x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)

'''
Análise da execução do código linha a linha para 
observar como a call stack seria preenchida:

----------------------------------------------------------------
1. Linha x = 1:

O Python define x como uma variável global com valor 1.
Nenhuma função foi chamada ainda, então a call stack está vazia.

----------------------------------------------------------------

2 -Linha print(x):

O Python imprime 1.

Nenhuma função foi chamada, então a call stack ainda está vazia.

----------------------------------------------------------------

3 - Linha escopo():

O Python chama a função escopo.

escopo é empilhada na call stack.

----------------------------------------------------------------

4 - Dentro de escopo():

x = 10 é executado, atualizando o valor de x para 10.

A função outra_funcao é definida, mas ainda não é 
chamada, então nada muda na call stack.

----------------------------------------------------------------

5 - Linha outra_funcao() dentro de escopo():

outra_funcao é chamada, então ela é empilhada 
na call stack, acima de escopo.

Agora, a call stack tem duas funções: escopo e outra_funcao.

----------------------------------------------------------------

6 - Dentro de outra_funcao():

x = 11 é executado, alterando x para 11.

y = 2 é definido como uma variável local com o valor 2.

print(x, y) imprime 11 2.

outra_funcao termina sua execução e é removida (desempilhada) da call stack.

----------------------------------------------------------------

7 - De volta em escopo():


A call stack agora tem apenas escopo.

print(x) imprime 11 (valor atual de x).

escopo termina sua execução e é removida da call stack.

----------------------------------------------------------------

8 - Linha print(x) após escopo():

O Python imprime o valor atual de x, que é 11.

A call stack está vazia novamente, pois todas as funções terminaram.

----------------------------------------------------------------

"Resumo da Call Stack Durante a Execução"

    A call stack nos ajuda a gerenciar a sequência de chamadas de funções.
No seu código, a call stack organiza a ordem de execução para que outra_
funcao seja executada dentro de escopo e as funções sejam chamadas e finalizadas 
na sequência correta.

    No final, todas as funções são removidas da call stack, 
deixando-a vazia para próximas execuções.
'''