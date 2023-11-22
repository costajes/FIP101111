'''
Revisao sobre a linguagem Python.
'''

#%%
# Palavras reservadas do Python
help('keywords')

#%%
# Tipos basicos de dados:
# int:
# float:
# complex: 
print( type(10), type(10.12), type(1.02e-13), type(1+5j))

#%%
# Identificadores (variaveis)
# - primeiro caracter: letra ou _
# - seguido de quaisquer outros caracteres
# - nao usar palavras reservadas do Python
A = 10
B = 10
c10 = 1.12
_abc = 3.12

#%%
# f-string
print(A, B, c10)
print(A, B, c10, sep="; ", end='\n\n')
print(A, B, c10, sep='\t')

print(f" A = {A};\n B = {B};\n c10 = {c10}")

#%%
# Importando modulos
import math
# import math as m
# from math import cos, sin, tan
# from math import *

print( math.cos(0.5))

#%% 
# Estruturas de repetiçao

obj = [1, 2, 3]
for e in obj:
    print(f"e = {e}")

lista = [e*4 for e in range(0,11)]

print()
for e in lista: print(e)

#%%
cont = 0 
while cont <= 10:
    if cont == 8: break
    print(f"cont = {cont}")
    cont +=1 
    
#%% 
# Estruturas de decisao
x = 10 
p = None
if x%2 == 0:
    p = 'par'
else:
    p = 'impar'
print( f"{x} e {p}")

#%%
x = 10 
p = 'par' if x%2 == 0 else 'impar'
print( f"{x} e {p}")

#%% 
import matplotlib.pyplot as plt 

lista = [10, 20, 30, 40]

x = [i/10. for i in range(-101, 102)]
y = [i**3 for i in x]

print(x, y)

plt.plot(x, y)
plt.show()
#%%
# Tuplas

tupla1 = (10, 20, 30)
lista1 = [10, 20, 30]

#%%
# Dicionarios
db = {'Name':'Sirius', 'magV':-1, 
      'magB':-0.5,
      'magU':0.1, '(U-B)':0.1-(-0.5), 
      '(B-V)':-0.5-(-1)}

for i in db.items():
    print(f"{i[0]} \t: \t{i[1]}")
    
#%%
# Conjuntos
set1 = {1, 5, 7, 18, 23, 23, 23}
set2 = {1, 23, 10, 20, 30, 1, 30}








