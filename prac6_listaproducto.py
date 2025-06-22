{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "368d6736",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3d996164",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dadas dos listas de números, por ejemplo [1, 2, 3] y [4, 5, 6], genera una \n",
    "# nueva lista que contenga el producto de los elementos correspondientes\n",
    "n = int(input(\"Cual es la cantidad de elementos de las listas: \"))\n",
    "lista_1 = [np.random.randint(0,10) for i in range(n)]\n",
    "lista_2 = [np.random.randint(0,10) for i in range(n)]\n",
    "producto_listas = [lista_1[i] * lista_2[i] for i in range(n)]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dc80a13f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lista 1: [8, 1, 1, 3, 8]\n",
      "Lista 2: [7, 8, 6, 5, 1]\n",
      "El producto de las listas es: [56, 8, 6, 15, 8]\n"
     ]
    }
   ],
   "source": [
    "print(f'Lista 1: {lista_1}')\n",
    "print(f'Lista 2: {lista_2}')\n",
    "print(f'El producto de las listas es: {producto_listas}')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
