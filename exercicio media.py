# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:11:30 2020

@author: i_pra
"""

lista_nota = []
buffer = 0

while buffer>=0:
    buffer = int(input('Insira notas, para terminar insira "-1":\n'))
    if buffer >= 0:
        lista_nota.append(buffer)
        buffer = 0
    else:
        break

 
media = (sum(lista_nota)/len(lista_nota))         

print("A média das notas é de",media)

if media >= 10:
    print('Parabéns pela nota')
else:
    print('Tens que te esforçar mais')
    
    