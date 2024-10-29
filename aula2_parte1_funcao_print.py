'''

Em Python, sep é um parâmetro usado na 
função print(). Ele especifica o que 
deve ser usado para separar os diferentes 
itens que você está imprimindo. Por padrão, 
o print() usa um espaço como separador, mas 
com o sep, você pode substituir isso por 
qualquer outra coisa. Aqui estão alguns exemplos:
'''

# Exemplo padrão, separador é um espaço
print("Olá", "mundo")
# Saída: Olá mundo

# Usando o parâmetro sep
print("Olá", "mundo", sep="-")
# Saída: Olá-mundo

print("Python", "é", "incrível", sep=" * ")
# Saída: Python * é * incrível



###################################################



'''
O parâmetro end em Python define o que 
será adicionado no final da saída do print(). 
"Por padrão, o print() adiciona uma nova linha 
ao final de cada chamada", mas com o end, você 
pode substituir isso por qualquer outra coisa, 
incluindo um espaço, uma vírgula ou mesmo um 
texto personalizado. Veja alguns exemplos:
'''

# Exemplo padrão, com nova linha no final
print("Olá")
print("mundo")
# Saída:
# Olá
# mundo

# Usando o parâmetro end
print("Olá", end=" ")
print("mundo", end="!")
# Saída: Olá mundo!

print("Python", end=" >>> ")
print("é", end=" >>> ")
print("incrível")
# Saída: Python >>> é >>> incrível

'''
Quando você usa o parâmetro end, o 
texto especificado em end é acrescentado 
ao final de cada chamada da função print().

Primeira Linha: print("Python", end=" >>> ") imprime 
"Python" e, em vez de adicionar uma nova linha, adiciona " >>> " 
e o próximo print sengue nessa mesma linha.

Segunda Linha: print("é", end=" >>> ") imprime "é" e, 
de novo, adiciona " >>> " em vez de uma nova linha e o 
próximo print sengue nessa mesma linha.

Terceira Linha: print("incrível") imprime "incrível" e, 
como end não foi especificado nesta linha, o padrão 
(nova linha) é usado.


Resultado final é:  

Python >>> é >>> incrível


Então, end substitui o caractere de nova linha 
ao final de cada chamada print(), unindo todas 
as chamadas print() em uma linha contínua. Por 
isso, cada chamada de print() segue uma após a outra, 
até que uma chamada use o end padrão, que é uma nova linha.

'''

