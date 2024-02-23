#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:23:52 2024

@author: isaacnilberto
"""

'''
Crie um programa que vai gerar cinco numeros aleatorios e colocas em uma tupla.

Depois disso, mostre a listagem de numeros gerados e também indique o menor 
e o maior valor que estao na tupla.
'''

import random 


numeros = tuple(random.randint(1,10) for i in range(0,5))
print(f'Os numeros aleatorios gerados foram: {numeros}.')
print(f'O maior numero gerado foi: {max(numeros)}.')
print(f'O menor numero gerado foi: {min(numeros)}.')