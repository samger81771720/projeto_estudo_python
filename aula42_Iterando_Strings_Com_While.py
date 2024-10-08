# Qual letra apareceu mais vezes na frase?

frase = (
         'O Python é uma linguagem de programação multiparadigma. '\
         'Python foi criado por Guido Van Rossum.'
         )

tamanho_da_frase = len(frase)
letra_que_mais_apareceu = ''
qtde_vezes_letra_que_mais_apareceu = 0
i = 0

while i < tamanho_da_frase:
    letra_atual = frase[i]
    if ' ' in letra_atual:
        i += 1
        continue
    qtde_vezes_letra_atual = frase.lower().count(letra_atual)
    if qtde_vezes_letra_atual > qtde_vezes_letra_que_mais_apareceu:
        letra_que_mais_apareceu = letra_atual
        qtde_vezes_letra_que_mais_apareceu = qtde_vezes_letra_atual
    i += 1 

print(
    f'\nA letra que mais apareceu foi a letra '
    f'"{letra_que_mais_apareceu}", pois apareceu '
    f'{qtde_vezes_letra_que_mais_apareceu} vezes.'
)