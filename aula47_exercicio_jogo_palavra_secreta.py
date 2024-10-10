"""
        "Faça um jogo para o usuário adivinhar qual a palavra secreta"


- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.


- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.


- Se a letra digitada estiver na
palavra secreta; exiba a letra;


- Se a letra digitada não estiver
na palavra secreta; exiba *.


Faça a contagem de tentativas do seu
usuário.


"""

palavra_secreta = 'Segredo'.lower()
tamanho_da_palavra = len(palavra_secreta)
palavra_mascarada = tamanho_da_palavra * '*'
texto_inicial = (
                  '"Jogo da palavra secreta"'\
                   '\n A palavra secreta tem '\
                   f'{tamanho_da_palavra} letras'
)


print(texto_inicial)


while True: 
    letra_digitada = input('Digite uma letra: ')
    for i in palavra_secreta:
        if letra_digitada in i:
            print('achou')
        else:
            continue
    print(palavra_mascarada[])
  
        
