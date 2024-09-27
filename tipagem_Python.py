'''
Python é uma linguagem de tipagem dinâmica. 
Isso significa que o tipo das variáveis é 
determinado em tempo de execução e pode mudar 
ao longo do programa. Por exemplo, você pode 
atribuir um número inteiro a uma variável e, 
em seguida, atribuir uma string à mesma variável 
sem problemas:
'''

variavel = 10
print(type(variavel))  # <class 'int'>

variavel = "Olá, mundo!"
print(type(variavel))  # <class 'str'>


'''
Além disso, Python é uma linguagem de tipagem forte, 
o que significa que não permite operações entre tipos 
incompatíveis sem conversão explícita. Por exemplo, 
você não pode somar uma string e um número diretamente:
'''
numero = 10
texto = "20"
# Isso causará um erro
# resultado = numero + texto
# Correto seria converter a string para número
resultado = numero + int(texto)
print(resultado)  # 30
