{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9658d732",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dada una lista de listas de números, utiliza una expresión generadora para calcular la media de todos los números.\n",
    "import numpy as np\n",
    "from functools import reduce\n",
    "listota = [[np.random.randint(0, 5) for _ in range(np.random.randint(1, 6))]for _ in range(np.random.randint(1, 6))]\n",
    "media_listota = reduce(lambda x,y:x+y,(sum(sublista) for sublista in listota))/sum(len(sublista) for sublista in listota)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d2d3c429",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "La lista generada es: [[4, 3, 4, 4]]\n",
      "La media de los elementos de la lista es: 3.750\n"
     ]
    }
   ],
   "source": [
    "print(f'La lista generada es: {listota}')\n",
    "print(f'La media de los elementos de la lista es: {media_listota:.3f}')"
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
