#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Pandas : Python Data Anlysis
'''

#%% Importando a biblioteca Pandas
import pandas as pd

#%% Criando uma estrutura de dados

data = [[5.96, 7.86, 9.706, 11.007, 12.122],
        ['Oph', 'Leo', 'Sgr', 'Vir', 'Cet'],
        [0.144, 0.090, 0.170, 0.168, 0.103],
        ['M4.0V', 'M6.0V', 'M3.5V', 'M4.0V', 'M5.5V'],
        [9.55, 13.44, 10.43, 11.13, 13.09],
        [13.22, 16.55, 10.43, 13.51, 15.26]
        ]

cols = ['Distance', 'Constellation', 'Mass',
        'Spectral_Class', 'mV', 'MV']

ids = ['Bernard', 'Wolf 359', 'Ross 154', 
      'Ross 128', 'YZ Ceti']

#%% Criando um dataframe
df1 = pd.DataFrame(data)

print(df1, end='\n\n')
print(type(df1), end='\n\n')

# Atribuindo nomes para as colunas:
df2 = pd.DataFrame(data).T
df2.columns = cols 
df2.index = ids

# Atribuindo ids para as linhas
print(df2, end='\n\n')


df3 = df2[ ['Mass', 'MV', 'mV']]
print(df3, end='\n\n')

df2.to_latex('df2.tex')

df2.to_csv('df2.csv')

df2[['Mass', 'MV']].to_csv('dfx.csv', 
                           sep=' ',
                           header=False,
                           index=False)


df5 = pd.read_csv('dfx.csv',
                  header=None)