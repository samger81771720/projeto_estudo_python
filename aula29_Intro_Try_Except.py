

numero_str = input(
    'Vou dobrar um número que vc digitar:'
)


# O if não impede que as exceções do sistema sejam lançadas quando ocorram.
# No exemplo abaixo se o método "isdigit()" for removido a exceção será lançada nesse trecho: "numero_float_convertido = float(numero_str)"
'''
if numero_str.isdigit():
    print('O que vc digitou é um digito.')
    numero_float_convertido = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float_convertido * 2:.2f}')
else:
    print('O que vc digitou não é um digito.')
'''


try:
    print('Aqui é uma variável do tipo string: ', numero_str)
    numero_float_convertido = float(numero_str)
    print('Aqui é uma variável do tipo float: ', numero_float_convertido)
    print(f'O dobro de {numero_str} é {numero_float_convertido * 2:.2f}')
    print('O dobro de %s é %.2f' % (numero_str, (numero_float_convertido * 2)))
except:
    # Aqui no except a exeção foi tratada de forma personalizada no console.
    print('Isso não é um número.')    
    



