contador = 0

while contador <= 20:
    
    contador += 1

    if contador == 6:
        print('Aqui voltou para o início do laço while.')
        continue

    elif (contador >= 10) and (contador <= 15): 
        print(
            'Aqui também voltou para o início do laço while e ficará nessa condição até que ela termine.'
        )
        continue
   
    print(f'Contador aqui é igual a {contador}')
    
    if contador == 19:
        print(f'Confirma que o valor do contador terminou em 19 mesmo: "{contador}"')
        break
    
    