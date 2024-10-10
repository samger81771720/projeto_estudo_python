'''
Iterável --> Elemento que entrega um valor de cada vez
            str, range, etc

///////////////

"iterador":

    __iter__() é um método especial chamado "dander iter" que qualquer classe 
    pode implementar para definir como ela deve ser iterada. 
    É parte da definição de uma classe. Esse método entrega 
    um "objeto iterador".

    iter() é uma função embutida em Python que chama o 
    método __iter__() do objeto que você passou para ela.

///////////////

    "__next__()" é o método especial chamado "dander next" 
    que os iteradores possuem e implementam para definir 
    como avançar para o próximo item.

    "next()" é a função embutida que chama "__next__()"
     do iterador fornecido. E assim, ambos trabalham 
     juntos para permitir a iteração de maneira simples 
     e eficiente. O método "__next__()" avança para 
     o próximo item do iterador e retorna esse item. 
     Se o iterador estiver vazio e não houver mais itens, 
    é lançada uma exceção "StopIteration".

'''

iterable = 'abc'
# "Iterável" --> Variável de exemplo:
iterator = iterable.__iter__()
# ou
iterator = iter(iterable)
# Quando você usa iter('abc'), isso é o mesmo que chamar 
# 'abc'.__iter__(). Ambos retornam um iterador para a string 'abc'. 
# No seu código, eles fazem a mesma coisa: criam um iterador que 
# pode ser usado para percorrer cada letra da string.




print(iterator)
'''
Retorna no console:

"<str_ascii_iterator object at 0x0000023B715458D0>"

Traduzindo: A expressão "str_ascii_iterator object" é 
um objeto que é o iterador da str que está nesse endereço 
de memória "0x0000023B715458D0"
'''




print(f'Aqui imprime a letra: ',{iterator.__next__()})
print(f'Aqui imprime a letra: ',{next(iterator)})
print(f'Aqui imprime a letra: ',{iterator.__next__()})

print(
       f'Aqui imprime um erro apontando o fim da iteração: ',
       {iterator.__next__()}
)
# Observe o comando "StopIteration" que determina o término da iteração.




