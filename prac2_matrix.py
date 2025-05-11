# %%
import numpy as np

# %%
#Dada la matriz H, Calcula la transpuesta de cada ”plano”1 dentro de la matriz tridimensional H. Guarde su programa en un archivo con extensión .py.
h = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
transpose_1 = np.transpose(h[0])
transpose_2 = np.transpose(h[1])

# %%
print(f'Dada la matriz: \n {h}')
print(f'La forma transpuesta del plano 1 sería: \n {transpose_1}')
print(f'La forma transpuesta del plano 2 sería: \n {transpose_2}')

# %%



