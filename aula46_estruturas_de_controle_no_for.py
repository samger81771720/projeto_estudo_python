'''
As mesmas estruturas de controle(continue, break, else, etc) 
que funcionam no "while" também funcionam no "for"

'''

for i in range(10):
    if i == 2:
        print(f'The Iterator is 2 in this round. Check it out: {i}')
        continue
    if i == 8:
        print('finished in 8 and the else was not executed.')
        break
    for j in range(1,3):
        print(i,j)
else:
    print('The structure was complete.')
   


    