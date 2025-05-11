# %%
import pandas as pd
import numpy as np

# %%
#Desarrolle un programa en Python que genere una arreglo NumPy tridimensional de tama˜no 5×4×3 con valores aleatorios entre 0 y 100. Posteriormente el programa debe encontrar el elemento m´as peque˜no
#y el m´as grande e indicar la ubicaci´on de dichos elementos dentro del arreglo. Imprima la matriz, los valores menor y mayor, as´ı como sus ubicaciones. Guarde su programa en un archivo con extensi´on .py

arreglo = np.random.randint(0,100,size=[5,4,3])
arreglo

# %%
#Hallar máximo y mínimo del arreglo
max_arreglo = np.max(arreglo)
max_coor = np.argwhere(arreglo == max_arreglo)

min_arreglo = np.min(arreglo)
min_coor = np.argwhere(arreglo == min_arreglo)

print(f'La matriz es la siguiente:\n {arreglo}')
print(f'El valor mínimo del arreglo es {min_arreglo} y se encuentra en las coordenadas:{min_coor}')
print(f'El valor máximo del arreglo es {max_arreglo} y se encuentra en las coordenadas:{max_coor}')


# %%



