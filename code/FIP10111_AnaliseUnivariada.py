#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analise Univariada

Dados: Sloan Digital Sky Survey - Release 17

by J.E.S.Costa

"""

#%% Importanto os modulos
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

#%% Leitura dos dados:
fdata = "/home/costajes/aula/FIP10111/data/SDSS-r17.csv"

df = pd.read_csv(fdata)

#%% Data cleaning?

print(f"Numero de NaNs: {df.isnull().sum()}")
print(f"Entradas repetidas: {df.duplicated().sum()}")

#%% Filtrando os dados
cols = ['alpha', 'delta', 'u', 'g', 'r', 'i', 'z',
        'class', 'redshift', 'MJD']

filtro1 = (df['u'] < 0) | (df['g'] < 0) | (df['z'] < 0)

print(f"Celulas contendo magnitudes < 0: {filtro1.sum()}")

df = df[~filtro1]


#%% Explorando os dados com Estatistica Univariada
#%% Estatisticas basicas
with pd.option_context('display.max_columns', 40):
    print(df[cols].describe()) 

stat2 = df[cols].describe(percentiles=[0.01, 0.10, 0.50, 0.90, 0.99])

#%% Histogramas:
#%%
mode = 3
nbins = int(np.sqrt(len(df))) 
#nbins = 20

# Utilizando funçoes graficas do Pandas:
if mode == 1:
    #df.hist()
    df[cols].hist(xlabelsize=7,
                  ylabelsize=7,
                  bins=nbins)
    
    plt.tight_layout()
    plt.show()
    
# Histogramas individuais via Matplotlib:
elif mode == 2:
    for c in cols:
        plt.hist(df[c],
                 bins=nbins)
        
        plt.xlabel(c)
        plt.ylabel("Counts")
        plt.title(f"Histogram of {c}")
        
        plt.show()
        
# Histogramas via seaborn:
elif mode == 3:
    
    k=-1
    for c in cols:
        k+=1; plt.figure(k)
        
        sb.histplot(data=df[c])
        
        plt.xlabel(c)
        plt.ylabel("Counts")
        plt.title(f"Histogram of {c}")
        
        plt.show()
           
#%% Curvas de densidade:
for c in cols:
    sb.kdeplot(data=df, x=c)
    
    #plt.xlabel(c)
    #plt.ylabel("Counts")
    #plt.title(f"Histogram of {c}")
    
    plt.show()
        