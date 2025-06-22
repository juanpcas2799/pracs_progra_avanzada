{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7230f986",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Utiliza una expresión generadora para calcular la varianza de una lista de números. \n",
    "# La varianza se calcula como la media de los cuadrados de las diferencias con la media.\n",
    "\n",
    "import numpy as np\n",
    "from functools import reduce\n",
    "lista = [np.random.randint(0,20) for _ in range(np.random.randint(1,10))]\n",
    "varianza = reduce(lambda x,y:x+((y-reduce(lambda x,y:x+y,(i for i in lista))/len(lista))**2),lista,0)/len(lista)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "73b0b1fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "La varianza de la lista [13, 7, 7, 8, 5, 9, 18] es 17.102\n"
     ]
    }
   ],
   "source": [
    "print(f'La varianza de la lista {lista} es {varianza:.3f}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "29e802c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "17.102040816326532\n"
     ]
    }
   ],
   "source": [
    "#Comprobación con numpy\n",
    "print(np.var(lista))"
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
