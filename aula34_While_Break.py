''' O "while" é uma estrutura de repetição (ou loop) em Python. 
Ele permite que um bloco de código seja executado repetidamente 
enquanto uma condição específica for verdadeira.

"break" é uma declaração que interrompe o loop mais próximo dela.
'''

condicao = True

# OPÇÃO ABAIXO UTLIZA O VALOR "False" PARA ENCERRAR O while
'''
while condicao:
    nome = input("Digite o seu nome: ")    
    print(f'Seu nome é {nome}')
    resposta = input('Deseja continuar? S = SIM / N = NÃO ')
    if resposta == 'N':
        condicao = False
        print('Programa Encerrado.')
'''

# OPÇÃO ABAIXO UTILIZA O "break" PARA ENCERRAR O while
while condicao:
    nome = input("Digite o seu nome: ")    
    print(f'Seu nome é {nome}')
    resposta = input('Deseja continuar? S = SIM / N = NÃO ')
    if resposta == 'N':
        break
print('Programa Encerrado.')