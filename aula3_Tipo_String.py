""" DOC STRING(Aspas usadas para fazer comentários como o que está sendo feito abaixo)

Python = Linguagem de Programação

Existem os seguintes tipos de tipagem para as linguagens de programação:

GRUPO 1:
*Fraca: Converte tipos automaticamente. Exemplo: Em JavaScript, 5 + '5' resulta em '55' (concatena).

*Forte: Exige correspondência de tipos. Exemplo: Em Python, 5 + '5' gera erro (não soma número com string).

GRUPO 2:
*Dinâmica: Define tipos em tempo de execução. Exemplo: Em Python, x = 5 e depois x = 'texto' muda o tipo.

*Estática: Define tipos em tempo de compilação. Exemplo: Em Java, int x = 5 e x = 'texto' gera erro.


Tipos de tipagem do Python: "Dinâmica" e "Forte"

"""

# STRING É UM TIPO "IMUTÁVEL"

#imprimindo "números" e não "strings"
print(1234)

''' EM PYTHON UMA STRING É UMA VARIÁVEL DO TIPO PRIMITIVA '''
#Imprimindo string com aspas simples
print('André')

#Imprimindo string com aspas duplas
print("André")

# Escape - "\" (Indica ao interpretador que ele ignore a leitura do caracter de escape "\" e passe para o próximo caracter.

# caracter que vem após ele, no caso, é uma aspa dupla. Poderia sem uma aspa simples também.)
print("André com o segundo nome \"Luiz\" entre aspas usando o caracter de escape.")

# r (read) - Lê também o caracter de escape dentro da string. 
print(r"André com o segundo nome \"Luiz\" entre aspas usando o caracter de escape o qual também está sendo lido pelo r.")

# Para que o código fique mais limpo, ao invés de usar o caracter de escape, "use aspas dupas dentro de aspas simples" ou o inverso.
print('Aqui está um "exemplo de aspas duplas dentro de aspas simples".')
print("Aqui está um 'exemplo de aspas simples dentro de aspas duplas'.")
print('Aqui está um "exemplo".')
print('Aqui está um outro "exemplo" com um número inserido como segundo ' 
      +'argumento ao lado direito do primeiro argumento',2)

