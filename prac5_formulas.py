{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2a495b3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "####Calculo de las formulas a0 y a1 de una recta\n",
    "from functools import reduce\n",
    "datos = [(1, 1.3), (2, 3.5), (3, 4.2), (4, 5), (5, 7), (6, 8.8), (7, 10.1), (8, 12.5), (9, 13), (10, 15.6)]\n",
    "m = len(datos)\n",
    "x_cuadradas = reduce(lambda x,y:x+y,map(lambda x:x**2,map(lambda x:x[0],datos)))\n",
    "x_normales = reduce(lambda x,y:x+y,map(lambda x:x[0],datos))\n",
    "y_normales = reduce(lambda x,y:x+y,map(lambda x:x[1],datos))\n",
    "x_y = reduce(lambda x,y:x+y,map(lambda x,y:x*y,map(lambda x:x[0],datos),map(lambda x:x[1],datos)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "532782ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a0 es -0.360 y a1 es 1.538\n",
      "La recta resultante es y = -0.360 + 1.538x\n"
     ]
    }
   ],
   "source": [
    "a0 = (x_cuadradas*y_normales-x_y*x_normales)/(m*x_cuadradas-x_normales**2)\n",
    "a1 = (m*x_y-x_normales*y_normales)/(m*x_cuadradas-x_normales**2)\n",
    "print(f'a0 es {a0:.3f} y a1 es {a1:.3f}')\n",
    "signo = \"+\" if a1 > 0 else \"-\"\n",
    "print(f'La recta resultante es y = {a0:.3f} {signo} {a1:.3f}x')"
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
