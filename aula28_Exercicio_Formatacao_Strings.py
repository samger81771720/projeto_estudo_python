"""
Exercício
Peça ao usuário para digitar seu nome - OK
Peça ao usuário para digitar sua idade - OK
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} - OK
        Seu nome invertido é {nome invertido} - OK
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra} - OK
        A última letra do seu nome é {letra} - OK
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome completo: ')
idade = input('Digite a sua idade: ')


if nome and idade:
    print(f'\nSeu nome é {nome}.')
    print(f'Sua idade é idade é {idade}')
    print(nome[::-1])
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[len(nome)-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    if ' ' in nome:
        print('O seu nome contém espaços.')
    else:
        print('O seu nome não contém espaços.')
elif not nome and not idade:   
    print('\nDesculpe, você digitou nada.')
elif not nome:
    print('\nVocê precisa digitar o seu nome.')
else:
    print('O número que represente a sua idade precisa ser preenchido e positivo.')


print('\n')



