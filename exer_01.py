#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:23:50 2024

@author: isaacnilberto
"""

'''
Crie um pograma que contenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até 20. Seu programa deverá ler um numero pelo teclado 
(entre 0 e 20) e mostra-lo por extenso.
'''

contagem = ('zero','um','dois','tres','quatro','cinco',
            'seis','sete','oito', 'nove','dez',
            'onze', 'doze', 'treze','quatorze','quinze',
            'dezesseis','dezessete','dezoito','dezenove','vinte')

for numero in range(len(contagem)):
    numero_input = int(input('Entre com um numero de 0 a 20: '))
    while numero_input < 0 or numero_input > 20:
        numero_input = int(input('Numero digitado errado. Entre com um numero de 0 a 20: '))
        
    if numero_input == 0:
        print(f'O numero digitado foi {contagem[0]}')
        break
    
    if numero_input == 1:
        print(f'O numero digitado foi {contagem[1]}')
        break
    if numero_input == 2:
        print(f'O numero digitado foi {contagem[2]}')
        break
    if numero_input == 3:
        print(f'O numero digitado foi {contagem[3]}')
        break
    if numero_input == 4:
        print(f'O numero digitado foi {contagem[4]}')
        break
    if numero_input == 5:
        print(f'O numero digitado foi {contagem[5]}')
        break
    if numero_input == 6:
        print(f'O numero digitado foi {contagem[6]}')
        break
    if numero_input == 7:
        print(f'O numero digitado foi {contagem[7]}')
        break
    if numero_input == 8:
        print(f'O numero digitado foi {contagem[8]}')
        break
    if numero_input == 9:
        print(f'O numero digitado foi {contagem[9]}')
        break
    if numero_input == 10:
        print(f'O numero digitado foi {contagem[10]}')
        break
    if numero_input == 11:
        print(f'O numero digitado foi {contagem[11]}')
        break
    if numero_input == 12:
        print(f'O numero digitado foi {contagem[12]}')
        break
    if numero_input == 13:
        print(f'O numero digitado foi {contagem[13]}')
        break
    if numero_input == 14:
        print(f'O numero digitado foi {contagem[14]}')
        break
    if numero_input == 15:
        print(f'O numero digitado foi {contagem[15]}')
        break
    if numero_input == 16:
        print(f'O numero digitado foi {contagem[16]}')
        break
    if numero_input == 17:
        print(f'O numero digitado foi {contagem[17]}')
        break
    if numero_input == 18:
        print(f'O numero digitado foi {contagem[18]}')
        break
    if numero_input == 19:
        print(f'O numero digitado foi {contagem[19]}')
        break
    if numero_input == 20:
        print(f'O numero digitado foi {contagem[20]}')
        break
    
#%% Outra solucao

contagem = ('zero','um','dois','tres','quatro','cinco',
            'seis','sete','oito', 'nove','dez',
            'onze', 'doze', 'treze','quatorze','quinze',
            'dezesseis','dezessete','dezoito','dezenove','vinte')


numero_input = int(input('Entre com um numero de 0 a 20: '))
while numero_input < 0 or numero_input > 20:
    numero_input = int(input('Numero digitado errado. Entre com um numero de 0 a 20: '))
    
print(f'O numero digitado foi {contagem[numero_input]}')