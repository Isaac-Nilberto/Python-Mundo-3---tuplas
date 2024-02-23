#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:23:54 2024

@author: isaacnilberto
"""
'''
Crie um programa que tenha uma tupla com varias palavras (nao usar acentos).
Depois disso, voce deve mostrar, para cada palavra, quais sao suas vogais.
'''

palavras = ('amor','paixao','traicao',
            'amizade','amigo','amiga')

for palavra in palavras:
    print(f'\n Na palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end = ' ')
    print('vogais.')
