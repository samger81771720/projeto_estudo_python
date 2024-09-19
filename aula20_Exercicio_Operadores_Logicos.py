primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

primeiro_valor_convertido = int(primeiro_valor)
segundo_valor_convertido = int(segundo_valor)

if primeiro_valor_convertido > segundo_valor_convertido:
    print(
        f'O primeiro valor digitado "{primeiro_valor_convertido} "'
        f' é maior que o segundo "{segundo_valor_convertido}".'
    )
elif primeiro_valor_convertido == segundo_valor_convertido:
    print(
        f'O primeiro valor digitado "{primeiro_valor_convertido}"'
        f' é igual ao segundo "{segundo_valor_convertido}".'
    )
else:
    print(
        f'O primeiro valor digitado "{primeiro_valor_convertido}"' 
        f' é menor que o segundo "{segundo_valor_convertido}".'
    )    



