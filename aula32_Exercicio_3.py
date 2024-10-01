"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Escreva o seu primeiro nome: ')

tamanho_nome_curto = (len(nome) > 1) and (len(nome) <= 4)
tamanho_nome_normal = (len(nome) == 5) or (len(nome) == 6)

mensagem_nome_curto = f'\n{nome} o seu nome é curto.\n' 
mensagem_nome_normal = '\n%s o seu nome possui tamanho normal.\n' % nome
mensagem_nome_longo = '\n{} o seu nome possui um tamanho extenso.\n'
mensagem_nome_longo_format = mensagem_nome_longo.format(nome)
mensagem_nome_nao_digitado = '\nPor gentileza, escreva o seu nome.\n'

if not nome:
    print(mensagem_nome_nao_digitado)
elif tamanho_nome_curto:
    print(mensagem_nome_curto)
elif tamanho_nome_normal:
    print(mensagem_nome_normal)
else:
    print(mensagem_nome_longo_format)
