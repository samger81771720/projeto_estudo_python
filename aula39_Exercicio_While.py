''' 
                Iterando strings com while 

Crie um código que modifique o seu nome completo acrescentando 
"*" a cada letra mas respeitando(mantendo) os espaços entre os 
nomes. Use a estrutura condicional while para isso.

'''

# Índices positivos:
#       0123456789...            25 
nome = 'André Luiz Geraldo Sampaio'
#      26               ...7654321
#                  Índices negativos:

tamanho_do_nome = len(nome)
ultimo_indice = len(nome) - 1
novo_nome = ''
simbolo = '*'
contador = 0


while contador < tamanho_do_nome:
    indice_atual = contador
    novo_nome += simbolo + nome[indice_atual]
    if indice_atual == ultimo_indice:
        novo_nome += simbolo
    contador += 1
    
print('\n Novo nome: ',novo_nome,'\n')


