{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "d9b60c9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Filtrar valores de una lista de diccionarios y aplicar descuentos\n",
    "from functools import reduce\n",
    "\n",
    "productos = [{'producto':'Horno','precio':200},{'producto':'Estufa','precio':500},{'producto':'Termo','precio':130},\n",
    "{'producto':'Mesa','precio':1000},{'producto':'Florero','precio':100},{'producto':'Black Label','precio':1200},\n",
    "{'producto':'Bacardi','precio':300}]\n",
    "\n",
    "productos_filtrados = list(filter(lambda x: x['precio'] > 200,productos))\n",
    "productos_descontados = dict(map(lambda x:(x['producto'],x['precio']*.9),productos_filtrados))\n",
    "suma_precios_descuento = reduce(lambda x,y: x+y,productos_descontados.values())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "6aeee1b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Los productos con descuento son: [('Estufa', 450.0), ('Mesa', 900.0), ('Black Label', 1080.0), ('Bacardi', 270.0)]\n",
      "La suma de los precios de los productos descontados es: $2700.0\n"
     ]
    }
   ],
   "source": [
    "print(f'Los productos con descuento son: {list(productos_descontados.items())}')\n",
    "print(f'La suma de los precios de los productos descontados es: ${suma_precios_descuento}')"
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
