#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:23:52 2024

@author: isaacnilberto
"""
'''
Crie uma tupla preenchida com os 20 primeiros colocados do campeonato brasileiro
de futebol, na ordem de colocacao. Depois mostre:
    a) apenas os 5 primeiros colocados
    b) os ultimos 4 colocados da tabela
    c) uma lista com os times em ordem alfabetica
'''

campeonato_brasileiro = (
                         'palmeiras', 'gremio', 'Atletico MG', 'Flamengo', 'Botafogo',
                         'Bragantino', 'Fluminense', 'Athletico Pr', 'Internacional', 'Fortaleza',
                         'Sao Paulo', 'Cuiaba', 'Corinthians', 'Cruzeiro', 'Vasco da Gama',
                         'Bahia','Santos', 'Goias', 'Coritiba', 'America MG',
                         )


print(f'Os primeiros 5 colocados foram: {campeonato_brasileiro[0:5]}.')
print(f'='*30)
print(f'Os ultimos 4 colocados foram: {campeonato_brasileiro[16:21]}.')
print(f'='*30)
print(f'Os primeiros 5 colocados foram: {sorted(campeonato_brasileiro, key = lambda x: x.lower())}.')