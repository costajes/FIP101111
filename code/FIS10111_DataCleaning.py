#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Data Cleaning - demonstraçao

"""

#%% Importar modulos
import pandas as pd

#%% Leitura dos dados
fdata = "/home/costajes/aula/FIP10111/data/Cardio.csv"
df = pd.read_csv(fdata, 
                 comment='#',
                 header=None)

#%% Renomeando colunas
df.columns = ['Duration', 'Date', 'Pulse',
              'MaxPulse', 'Calories']

#%% Inspecionar dados
print(df)

print(df.head(7))

print(df.tail(6))

#%% 1. Celulas vazias (NaN, NAs, None)
print(df.info())

print(df.isnull())
print(df.isnull().sum())

#%% 1.a Removendo vazios
df1 = df.dropna()

#%% 1.b Substituir pela media
xmed = df['Calories'].mean()
xmedian = df['Calories'].median()
print(f"Media = {xmed}\nMediana = {xmedian}")

df2 = df.copy()
x = df2["Calories"].fillna(xmed,
                           inplace=True)
#%% 1.c Substituir por valor especifico

df2.loc[22, 'Date'] = "'2020/12/22'"

#df2.loc[26, 'Date'] = "xxx"

df2.loc[26, 'Date'] = f"'{df2.loc[26, 'Date']}'"

#%% 2. Celulas com valores errados ou outliers

MAX_DURATION = 120

for i in df2.index:
    if df2.loc[i, 'Duration'] > MAX_DURATION:
        df2.drop(i, inplace=True)
        
#%% 3. Entradas duplicadas

print(df2.duplicated())

print( df2.loc[df2.duplicated()])

df2.drop_duplicates(inplace=True)
