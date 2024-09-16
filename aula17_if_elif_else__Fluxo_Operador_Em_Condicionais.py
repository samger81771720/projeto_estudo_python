# if(Primeira condição) / elif(Segunda opção) ...... / 
# else(Sempre será a última opção a ser executada)

# if(se) / elif(se não se) / else(se não)

condicao = False
soma = 10 + 20
ultima_Variavel = True


if condicao:
    print('A condição é verdadeira.\n')
else:
    print('A condição é falsa.\n')

if 10 == 10:
    # "..." elipses podem ser usadas para dizer que algo ainda não foi codificado
    # "pass" tem o mesmo tipo de uso. Embora no exemplo tenham sido expostos juntos,
    # é preciso escolher entre um e o outro.
    ...
    pass

if soma == 20:
    print('A soma é igual a 20.\n')
elif soma == 30:
    print('A soma é igual a 30.\n')
elif soma == 10:
    print('A soma é igual a 10')
elif soma == 15:
    print('A soma é igual a 15')

if ultima_Variavel:
    print('Após ter interrompido o fluxo de veirificações em "soma == 30" veio para esse bloco final.\n')





