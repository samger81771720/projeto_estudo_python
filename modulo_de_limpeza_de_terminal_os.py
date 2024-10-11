# Importando o módulo do python "os"
import os

palavra_secreta = 'abc'.lower()
tamanho_da_palavra = len(palavra_secreta)
simbolo_de_mascara = '*'
palavra_mascarada = (tamanho_da_palavra * simbolo_de_mascara)
contagem_de_tentativas = 0
texto_inicial = (
                  '"Jogo da palavra secreta"'\
                   '\n A palavra secreta tem '\
                   f'{tamanho_da_palavra} letras.'
)

print(texto_inicial)

while True: 
    
    contagem_de_tentativas += 1
    letra_digitada = input('\nDigite uma letra: ').lower()

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra de cada vez.')
        continue
    
    nova_palavra_mascarada = ''
    
    for i in range(tamanho_da_palavra):
        if letra_digitada in palavra_secreta[i]:
            nova_palavra_mascarada += palavra_secreta[i]
        else:
            nova_palavra_mascarada += palavra_mascarada[i]
    
    palavra_mascarada = nova_palavra_mascarada
    print(palavra_mascarada)

    if palavra_mascarada == palavra_secreta:
        
        # Implementando o módulo "os" para limpar o 
        # terminal nesse ponto de execução do código
        os.system('cls')

        erros = (contagem_de_tentativas - tamanho_da_palavra)
        print('\nParabéns, você conseguiu!!!' \
              f'\n\nHouveram {erros} tentativas sem sucesso.' \
               '\n\n"Fim do Programa"\n')
        break
 
