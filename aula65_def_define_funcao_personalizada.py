'''
INTRODUÇÃO A FUNÇÕES EM PYTHON

"Funções são trechos de código usados 
para replicar determinada ação ao longo 
do seu código."

----------------------------------------------------------
Parâmetro: É uma variável(s) criada(s) na definição da função. 
É como a função espera receber dados. Por exemplo, em def 
minha_funcao(par1, par2), par1 e par2 são parâmetros.
----------------------------------------------------------
Argumento: É o valor real que você passa para a função 
quando a chama. 
Por exemplo, em minha_funcao(5, 10), 5 e 10 são argumentos.
----------------------------------------------------------

As funções podem receber argumentos nos 
parâmetros e retornar um valor específico.

"Por padrão, funções Python retornam None(nada)"

'''

# Utiliza-se a expressão "def" para definir uma função:
def func1(parametro_a,parametro_b,parametro_c):
    print('\nResultado da soma ou concatenação dos três argumentos dos parâmentros mencionados:')
    print(parametro_a + parametro_b + parametro_c)

func1(5,6,9)
func1(1,3,10)
func1('André',' Luiz',' Sampaio')

def func2(parametro_a = 5, parametro_b = 6, parametro_c = 7):
    print('\nResultado da soma dos três argumentos dos parâmentros mencionados "com valores atribuídos":')
    print(parametro_a + parametro_b + parametro_c)
func2()

def func3(parametro_a = 5, parametro_b = 6, parametro_c = 7):
    print(
        '\nResultado da soma dos três argumentos inseridos "na chamada ' \
        'da função". \nObserve nesse caso, que apesar dos parâmentros já ' \
        'terem valores atribuídos, \na prioridade será sempre dos valores' \
        ' que fores inseridos na declaração de chamada da função:'
    )
    print(parametro_a + parametro_b + parametro_c)
func3(10,20,30)
print(
    'Úteis para manter valores padrão quando na ausência ' \
        'de valores inseridos na chamada da função.'
)

def func4(texto = '\nTexto padrão, caso não insira outro na chamada da função.'):
    print(texto)
func4()
func4('Texto inserido na chamada da função\n')
