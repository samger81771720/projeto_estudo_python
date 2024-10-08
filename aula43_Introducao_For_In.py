'''
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input("Digite a sua senha: ")
    repeticoes += 1

print(repeticoes)
'''

                              # "for in"

#''' Itera sobre "cada índice" da string(um de cada vez) '''

# A variável inserida logo após o "for" é de livre escolha o nome,
# na qual será armazenada o conteúdo de cada índice.


palavra = 'Paralelepípedo'
nova_palavra = ''

for letra in palavra:
    nova_palavra += f'*{letra}'
    print(nova_palavra)