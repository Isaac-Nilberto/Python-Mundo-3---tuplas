#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:23:53 2024

@author: isaacnilberto
"""
'''
Crie um programa que tenha uma tupla unica com nomes de produtos e seus respec
tivos precos, na sequencia.

No final, mostre uma listagem de precos, organizando os dados em forma tabular.
'''
listagem = ('hambuerguer',20,
            'pizza',10,
            'pastel',15,
            'pão',25,
            'coxinha',5,
            'café',7,
            'refrigerante',6)

print('Produto\t\t\t\t\tPreco')
print('='*30)


for i in range(0, len(listagem), 2):
    print(f'{listagem[i].ljust(13)}',' ........ ',f'R$ {listagem[i + 1]}')