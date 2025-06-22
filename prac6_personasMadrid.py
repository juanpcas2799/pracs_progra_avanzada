{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0ffc9667",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dada una lista de diccionarios que representan personas con claves “nombre”, “edad” y “ciudad”,\n",
    "# genera una nueva lista de nombres de personas que tengan más de 30 años y vivan en “Madrid”.\n",
    "\n",
    "personas_clasificar = [{\"nombre\": \"Ana\", \"edad\": 25, \"ciudad\": \"Madrid\"}, {\"nombre\": \"Juan\", \"edad\": 35, \"ciudad\": \"Madrid\"},\n",
    "{\"nombre\": \"Luis\", \"edad\": 32, \"ciudad\": \"Barcelona\"}]\n",
    "\n",
    "personas_30_Madrid = [i['nombre'] for i in personas_clasificar if (i['edad'] > 30) and (i['ciudad'] == 'Madrid')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b2953513",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Los individuos que tienen 30 años o más y viven en Madrid son: ['Juan']\n"
     ]
    }
   ],
   "source": [
    "print(f'Los individuos que tienen 30 años o más y viven en Madrid son: {personas_30_Madrid}')"
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
