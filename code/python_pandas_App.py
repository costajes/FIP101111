#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pandas : aplicaçao a Analise de Dados
"""

#%% Coisas uteis para o codigo:
print2 = lambda titulo, obj : print(50*"=","\n",titulo, "\n", obj, 50*"=", end="\n\n")
Msun = 2.e30 # massa solar (em Kg)

#%% Importar a biblioteca Pandas:
import pandas as pd

#%% Ler dados de um arquivo CSV:
dir_data = "/home/costajes/aula/FIP10111/data/"
fdata = dir_data + "Exoplanets_2023.10.24_08.34.54.csv"

df = pd.read_csv(fdata, 
                 comment='#',
                 index_col=0)

#%% Examinar estrutura interna do DataFrame
show = False
if show:
    print2("DataFrame df:", df)
    print2("Colunas do df:", df.columns)
    print2("Indices das linhas:", df.index)
    
#%% Construir um novo DataFrame contendo 
# somente colunas de interesse:
cols = ['kepler_name', # star name (Kepler Catalogue)
        'koi_smass',   # stellar mass (Msun)
        'ra',          # Right Ascension (deg)
        'dec'          # Declination (deg)
        ]

# CUIDADO! 
# Fazer uma copia independente usando o metodo .copy()
df1 = df[cols].copy()
    
#%% Renomear colunas (do novo df)
mapper = {'kepler_name' : 'Name',
          'koi_smass' : 'Mass',
          'ra' : 'RA',
          'dec' : 'DEC'}

df1.rename(columns = mapper,
           inplace = True)

#%% Inserir uma nova coluna:
MassKg = df1['Mass'].values * Msun
df1["MassKg"] = MassKg

#%% Descartar uma coluna:
df1.drop(columns="Name", inplace=True)

#%% Filtrar dados:
filtro1 = df1.Mass <= 0 
filtro2 = df1.Mass.isna() 
filtro3 = filtro1 | filtro2 

df1_bad = df1[filtro3]
df1_good= df1[~filtro3]

df1.plot(kind='scatter', x='RA', y='DEC')

df1.hist(column='Mass', bins=30)