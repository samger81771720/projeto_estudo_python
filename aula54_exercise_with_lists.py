''''
            "Faça uma lsita de compras" 

Em relação a lista de compras o 
usuário deve ter a possibilidade de:

* Inserir,
* Apagar,
* Listar

O programa não pode quebrar com erros
de índices inexistetes. 

'''

shopping_list = list()

while True:
    
    option = input('\n[i]nsert [d]elete [l]ist [c]lose the program ---> ').lower()

    if option not in {'i', 'd', 'l', 'c'}:
        print('\nPlease choose only one of the four options!')
        continue
    
    if option in 'i':
        item = input('\nWhite the desired product: ')
        shopping_list.append(item)
        continue

    if option in 'l':
        print('\n Shopping list:\n')
        for iterator in enumerate(shopping_list):
            print(iterator)
        continue

    if option in 'd':
        
        try:
            error_value = True

            while error_value:

                index_number = input('\nEnter the number corresponding to the item: ')
                index_number = int(index_number)
                
                if index_number <= len(shopping_list):
                    for index, value in enumerate(shopping_list):
                        if index_number == index:
                            del shopping_list[index_number]
                            error_value = False
                    
                else:
                    print('\nThe number entered does not match any product in the list.')
             
        except:
            print('\nPlease enter the "number" corresponding to the desired item.')

    
        continue   

    if option in 'c':
        print('\n')
        break

