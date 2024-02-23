#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:23:53 2024

@author: isaacnilberto
"""

'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final, mostre:
    a) quantas vezes o valor 9 apareceu
    b) em que posicao foi digitado o primeiro valor 3
    c) quais foram os numeros pares
'''

primeiro = int(input('Entre com o primeiro numero: '))

segundo = int(input('Entre com o segundo numero: '))

terceiro = int(input('Entre com o terceiro numero: '))

quarto = int(input('Entre com o quarto numero: '))

numeros = (primeiro, segundo, terceiro, quarto)

print('='*30)

print(f'O numero 9 foi digitado {numeros.count(9)} vezes.')

print('='*30)

encontrou_3 = False

for i in range(len(numeros)):
    if numeros[i] == 3:
        
        print(f'O numero 3 aparece na posicao {i + 1}.')
        encontrou_3 = True
if not encontrou_3:
    print('O numero 3 nao foi digitado.')
print('='*30)
contador = 0 
for i in range(len(numeros)):
    if i % 2 == 0:
        contador += 1
print(f'Há {contador} pares.')

