'''
Métodos em Python: 

Em Python, a distinção entre procedimentos e funções 
não é tão rígida quanto em linguagens como Java. Embora 
ambos os conceitos envolvam blocos de código que realizam 
tarefas específicas, em Python, a tendência é tratar tudo 
como uma função.



Por que essa diferença?

Tudo é um objeto: Em Python, até mesmo funções são objetos 
de primeira classe. Isso significa que elas podem ser atribuídas 
a variáveis, passadas como argumentos para outras funções e 
retornadas por funções.


Foco na flexibilidade: Python busca uma sintaxe mais simples 
e intuitiva. A distinção entre procedimentos e funções pode 
adicionar complexidade desnecessária.




Então, como funciona em Python?

Funções: Um bloco de código reutilizável que pode receber 
argumentos e retornar um valor.

Métodos: Funções que pertencem a uma classe e operam sobre 
os objetos dessa classe. O primeiro argumento de um método 
é geralmente self, que se refere à instância do objeto.




Exemplo:

Python
class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        print(f"{self.nome} está latindo!")

# Criando um objeto da classe Cachorro
meu_cachorro = Cachorro("Rex")

# Chamando o método latir
meu_cachorro.latir()  # Saída: Rex está latindo!
Use o código com cuidado.

No exemplo acima:

latir é um método da classe Cachorro.
self.nome se refere ao atributo nome do objeto específico.
Em resumo:

Python unifica procedimentos e funções em um único conceito: funções.
Métodos são funções associadas a classes.
A flexibilidade de Python permite tratar funções de forma mais versátil.
'''