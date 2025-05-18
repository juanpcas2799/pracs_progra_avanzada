{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45a07bb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "####Metodo vector\n",
    "import math\n",
    "class Vector:\n",
    "    def __init__(self,x,y):\n",
    "        self.x = x\n",
    "        self.y = y \n",
    "    \n",
    "    def magnitud(self):\n",
    "        r = math.sqrt(self.x**2 + self.y**2)\n",
    "        return f'La magnitud del vector ({self.x},{self.y}) es {round(r,3)}'\n",
    "    \n",
    "    def angulo_grados(self):\n",
    "        theta = math.atan(self.y/self.x)\n",
    "        return f'El ángulo en grados del vector ({self.x},{self.y}) es {round(theta,4)}'\n",
    "    \n",
    "    def radianes(self):\n",
    "        rad = math.atan(self.y/self.x)*180/math.pi\n",
    "        return f'El ángulo en grados del vector ({self.x},{self.y}) es {round(rad,4)}º'\n",
    "    \n",
    "    def __add__(self,other):\n",
    "        xsum = self.x + other.x\n",
    "        ysum = self.y + other.y\n",
    "        return f'El resultado de la suma de los vectores ({self.x},{self.y}) y ({other.x},{other.y}) es el vector ({xsum},{ysum})  '\n",
    "\n",
    "    def __str__(self):\n",
    "        return f'({self.x},{self.y})'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "id": "6748c939",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(5,-1) (2,-4)\n"
     ]
    }
   ],
   "source": [
    "#Vectores mostrados como coordenadas\n",
    "p = Vector(5,-1)\n",
    "q = Vector(2,-4)\n",
    "print(p,q)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "0085ea2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'La magnitud del vector (5,-1) es 5.099'"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Magnitud de los vectores\n",
    "p.magnitud()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "acb397e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'El ángulo en grados del vector (5,-1) es -0.1974'"
      ]
     },
     "execution_count": 178,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Angulo en grados\n",
    "p.angulo_grados()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "10152a46",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'El ángulo en grados del vector (5,-1) es -11.3099º'"
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Angulo en radianes\n",
    "p.radianes()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "fe571b2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'El resultado de la suma de los vectores (5,-1) y (2,-4) es el vector (7,-5)  '"
      ]
     },
     "execution_count": 180,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Suma de vectores\n",
    "p + q"
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
