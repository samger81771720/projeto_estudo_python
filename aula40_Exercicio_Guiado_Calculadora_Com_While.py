'''Calculadora com While'''

while True:
    primeiro_numero_str = input('\nDigite o primeiro número: ')
    segundo_numero_str = input('Digite o segundo número: ')
    primeiro_numero_float = 0
    segundo_numero_float = 0
    numeros_validos_digitados = None

    try:
        primeiro_numero_float = float(primeiro_numero_str)
        segundo_numero_float = float(segundo_numero_str)
        numeros_validos_digitados = True
    except Exception as error:
        numeros_validos_digitados = None
        print(f'\nMensagem de erro do sistema: {error}')
        
        if numeros_validos_digitados is None:
            print('\nParece que você não preencheu um ou ambos números corretamente. \n'
            'Vamos retornar ao prenchimento inicial dos números.')
            continue
   
    operador_matematico = input('Digite o operador matemático desejado: ')
    operadores_permitidos = '-+*/'

    while operador_matematico not in operadores_permitidos:
        operador_matematico = input(
            'Os únicos operadores possíveis nessa calculadora, '
            ' são: "+", "-", "/" e "*". Por favor escolha uma '
            ' dessas quatro opções: '
        )

    condicao_errada_divisao = (operador_matematico == '/') and (segundo_numero_str == '0')

    if condicao_errada_divisao:
        while segundo_numero_str == '0':
            segundo_numero_str = input('Por favor, digite um número que seja diferente de zero: ')
            segundo_numero_float = float(segundo_numero_str)
            
    soma = (primeiro_numero_float + segundo_numero_float)
    subtracao = (primeiro_numero_float - segundo_numero_float)
    multiplicacao = (primeiro_numero_float * segundo_numero_float)
    divisao = (primeiro_numero_float / segundo_numero_float)
    resultado = 0

    if operador_matematico == '+':
        resultado = soma
    elif operador_matematico == '-':
        resultado = subtracao
    elif operador_matematico == '*':
        resultado = multiplicacao
    else:
        resultado = divisao

    print('O resultado da operação é %.2f' % (resultado))

    sair = input(
        '\nDeseja realizar outra operação ou sair do programa? [C] Continuar / [S] Sair: '
    ).lower().startswith('s')

    if sair:
        break
    



