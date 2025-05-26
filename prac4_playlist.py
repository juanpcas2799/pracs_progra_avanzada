{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9a1242c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Practica Playlist\n",
    "class Playlist:\n",
    "    def __init__(self, miLista):\n",
    "        self.miLista = list(miLista)\n",
    "    \n",
    "    def __len__(self):\n",
    "        return len(self.miLista)\n",
    "    \n",
    "    def __getitem__(self,index):\n",
    "        if index < 0 or index >= len(self.miLista):\n",
    "            raise IndexError(\"Índice fuera de rango\")\n",
    "        return self.miLista[index]\n",
    "    \n",
    "    def __setitem__(self,index,nueva_cancion):\n",
    "        if 0 <= index < len(self.miLista):\n",
    "            self.miLista[index] = nueva_cancion\n",
    "        else:\n",
    "            raise IndexError('Indice fuera de rango')\n",
    "    \n",
    "    def __str__(self, miLista):\n",
    "        return self.miLista\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4a6f4d82",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Ivy', 'Paranoia', 'Lo mismo de siempre', 'Bailando solo']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "canciones1 = Playlist(['Ivy', 'Paranoia', 'Lo mismo de siempre', 'Bailando solo'])\n",
    "nueva_rola = 'Kids See Ghosts'\n",
    "\n",
    "#Ver lista original\n",
    "canciones1.miLista"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4bb61be5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Cantidad de elementos en la playlist\n",
    "len(canciones1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5def03f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Bailando solo'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "##Llamar un elemento\n",
    "canciones1[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "11472ce7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Ivy', 'Paranoia', 'Lo mismo de siempre', 'Kids See Ghosts']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "###Añadir un elemento a la playlist\n",
    "canciones1[3] = nueva_rola\n",
    "canciones1.miLista"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0cd29aa5",
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
