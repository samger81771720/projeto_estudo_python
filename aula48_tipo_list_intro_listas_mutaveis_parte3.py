"""
                        "Listas em Python"
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas

    Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)


IMPORTANTE: "PROCURE INSERIR ITENS APENAS 
NO FINAL DA LISTA, POIS DO CONTRÁRIO,
CASO A SUA LISTA SEJA MUITO GRANDE, SERÁ DEMANDADO 
MUITO PROCESSAMENTO PARA REORGANIZAR OS VALORES.
ISSO SE APLICA MAIS A LISTAS QUE SEJAM MUITO EXTENSAS. 


"""
lista = [10, 20, 30, 40]
lista2 = [50, 60, 70, 80]

# "clear" --> Método para limpar lista
lista.clear()

print(lista)


# "insert" - Adiciona um item no índice escolhido
# Inserindo o "valor 99" no "índice 0" na variável "lista2"
lista2.insert(0, 90)
# Observe que todos os outros valores "50, 60, 70, 80" foram
# realocados para outros índices, pois o índice 0 passou a 
# armazenar o valor 90.
print(lista2)

