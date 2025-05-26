{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "b200fbf3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#####Práctica Rectangulo\n",
    "class Rectangulo:\n",
    "    def __init__(self, altura, base):\n",
    "         self.altura = altura\n",
    "         self.base = base\n",
    "    \n",
    "    def __eq__(self,other): #Verifica si los rectángulos son iguales\n",
    "        return (self.altura,self.base ) == (other.altura, other.base)\n",
    "    \n",
    "    def __ne__(self,other): #Verifica si los rectángulos son distintos\n",
    "        return (self.altura,self.base ) != (other.altura, other.base)\n",
    "\n",
    "    def __gt__(self,other): #Verifica si el area del primer rectangulo es mayor que la del segundo\n",
    "        return (self.altura * self.base) >  (other.altura * other.base)\n",
    "    \n",
    "    def __lt__(self,other): #Verifica si el area del primer rectangulo es menor que la del segundo\n",
    "        return (self.altura * self.base) < (other.altura * other.base)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "4a4072b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "True\n",
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "r1 = Rectangulo(5,10)\n",
    "r2 = Rectangulo(6,7)\n",
    "r3 = Rectangulo(5,10)\n",
    "r4 = Rectangulo(10,10)\n",
    "\n",
    "print(r1==r2)\n",
    "print(r1 == r3)\n",
    "print(r1>r2)\n",
    "print(r1<r2)\n",
    "print(r1>r4)\n",
    "print(r1<r4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d61e302",
   "metadata": {},
   "outputs": [],
   "source": []
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
