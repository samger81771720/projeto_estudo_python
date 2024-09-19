# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

'''
senha_permitida = '123456'

entrada = input('[E]ntrar [S]air: ')
if (entrada == 'S') or (entrada == 's'):
    print('Saiu do programa.')
elif (entrada == 'E') or (entrada == 'e'):
    senha_digitada = input('Digite a senha: ')
if ((entrada == 'E') or (entrada == 'e')) and (senha_digitada == senha_permitida):
    print('Entrou')
elif (entrada == 'E') or (entrada == 'e') and (senha_digitada != senha_permitida):
    print('A senha digitada é diferente da senha permitida.')
elif (entrada != 'E' and entrada != 'e') and (entrada != 'S') and (entrada != 's'):
   print('As únicas opções diponíveis são "E" ou "S". Digite uma das duas opções.')

'''


'''
 Essa tbm é uma "Avaliação de Curto Circuito". É tbm chamada assim porque quando 
 o operador "or" é utilizado, uma condição para ser considerada verdadeira, 
 basta apenas que "uma das condições inseridas como argumentos no 
 parâmetro sejam verdadeira". E além disso, ao ser identificada como verdadeira, 
 o valor de todo um possível conjunto de verificações será dado por ela. 
 Se todas as condições(ou uma) forem falsos então o valor será falso.
 Exmplos abaixo:
'''


senha = 0 or False or 0 or 'abc' or True
verificacao = False or 0
print(senha)
print(verificacao)


senha_opcional = input('Com Senha: ') or 'Sem senha'
#Será executado primeiro o input e depois a frase.
print(senha_opcional)




