                                    # Operador lógico "and"

# and (e) or (ou) not (não)

# and - Todas as condições precisam ser verdadeiras.

# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)

# Também existe o tipo None que é
# usado para representar um não valor


senha_permitida = '123456'

entrada = input('[E]ntrar [S]air: ')
if entrada == 'S':
    print('Saiu do programa.')
elif entrada == 'E':
    senha_digitada = input('Digite a senha: ')
if entrada == 'E' and (senha_digitada == senha_permitida):
    print('Entrou')
elif entrada == 'E' and (senha_digitada != senha_permitida):
    print('A senha digitada é diferente da senha permitida.')
elif entrada != 'E' and entrada != 'S':
   print('As únicas opções diponíveis são "E" ou "S". Digite uma das duas opções.')


'''
No caso da verificação do print abaixo, o 
fluxo é interrompido no "False".
O último True não será lido. "
'''
print(True and False and True)


#  0  0.0  '' serão False.
print(bool(0))
print(bool(0.0))
print(bool(''))

'''
 Essa é uma "Avaliação de Curto Circuito". É  chamada assim porque quando 
 o operador "and" é utilizado, uma condição para ser considerada verdadeira, 
 somente assim o será "se todas as condições inseridas como argumentos no 
 parâmetro sejam verdadeiras". Caso alguma condição seja falsa essa mesma 
 condição irá ser a causadora da interrupção de qualquer outra(s) verificação
 que vier(caso tenham outras condições além dela). E além disso,
 ao ser identificada como falsa, o valor de todo um possível conjunto de 
 verificações será dado por ela. 
 Exemplos abaixo:
'''
print(True and 0 and True)
print(True and False and 0)




'''
Em Python, um valor falsy é aquele que é interpretado como falso 
em um contexto booleano, como em um if ou while.

Exemplos de valores falsy:

None
False
Números zero (0, 0.0, 0j)
Sequências vazias (listas, tuplas, strings, dicionários)
Conjuntos vazios
Em resumo: Se você usar um valor falsy em uma condição, a condição será considerada False.

Exemplo:

Python
if []:  # Lista vazia é falsy
    print("Isso não será impresso")



Falsy vs. False em Python: Qual a diferença?
Falsy e False são conceitos relacionados em Python, mas não são idênticos.

False: É um valor booleano específico que representa o falso. É um dos dois valores booleanos possíveis em Python (o outro é True).
Falsy: É uma categoria mais ampla que inclui False, mas também outros valores que são considerados falsos em contextos booleanos.
Em resumo:

Todos os valores False são falsy, mas nem todos os valores falsy são False.
Um valor falsy é qualquer valor que, quando avaliado em um contexto booleano (como em um if, while, ou em operações lógicas), é considerado como False.
Por que isso importa?

Essa distinção é crucial para entender como as condições são avaliadas em Python. Quando você usa um valor em uma condição, o Python implicitamente o converte para um booleano. Se o valor for falsy, a condição será considerada False.

Exemplo:

Python
if 0:  # 0 é um valor falsy
    print("Isso não será impresso")

if False:
    print("Isso também não será impresso")
Use o código com cuidado.

Por que existem valores falsy?

Conveniência: Facilita a escrita de código mais conciso e legível. Por exemplo, em vez de verificar se uma lista está vazia, você pode simplesmente usar a lista diretamente na condição.
Semântica: Reflete a ideia de "ausência de valor" ou "condição não satisfeita" em muitos casos.
Quais são os valores falsy em Python?

Booleano: False
Números: 0 de qualquer tipo numérico (inteiro, float, complexo)
Sequências e coleções vazias: strings vazias, listas vazias, tuplas vazias, dicionários vazios, conjuntos vazios
None: Representa a ausência de valor
Quando usar um valor falsy?

Verificando se uma variável está vazia: if minha_lista:
Condições simples: if usuario_logado:
Expressões ternárias: valor = x if condicao else y
Em resumo:

Ao entender a diferença entre falsy e False, você poderá escrever código Python mais eficiente e expressivo. Lembre-se que a maioria dos valores que representam "nada", "vazio" ou "falso" são considerados falsy.


'''