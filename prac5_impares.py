{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6a8f7e0d",
   "metadata": {},
   "outputs": [],
   "source": [
    "####Filtrar impares y sumar sus cuadrados\n",
    "from functools import reduce\n",
    "import numpy as np\n",
    "prueba = []\n",
    "for i in range(10):\n",
    "    valor = np.random.randint(1,100)\n",
    "    prueba.append(valor)\n",
    "\n",
    "impares = list(filter(lambda x : x%2 != 0,prueba))\n",
    "cuadrados = list(map(lambda x:x**2,impares))\n",
    "sumarlos = reduce(lambda x,y:x+y,cuadrados)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0f6a109f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lista generada: [34, 96, 36, 23, 97, 7, 28, 64, 4, 21]\n",
      "Números impares de la lista: [23, 97, 7, 21]\n",
      "Cuadrado de los impares: [529, 9409, 49, 441]\n",
      "Suma de los cuadrados de los impares: 10428\n"
     ]
    }
   ],
   "source": [
    "print(f'Lista generada: {prueba}')\n",
    "print(f'Números impares de la lista: {impares}')\n",
    "print(f'Cuadrado de los impares: {cuadrados}')\n",
    "print(f'Suma de los cuadrados de los impares: {sumarlos}')"
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
