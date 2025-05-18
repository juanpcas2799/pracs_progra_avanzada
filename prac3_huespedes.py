{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a75470f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "class persona:\n",
    "    def __init__(self, nombre, edad):\n",
    "        self.nombre = nombre\n",
    "        self.edad = edad\n",
    "    \n",
    "    def __str__(self):\n",
    "        return f'Nombre: {self.nombre} \\nEdad: {self.edad}'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "9a2fb58e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "class huesped(persona):\n",
    "    def __init__(self, nombre, edad, habitacion, rfc, num_cuenta, fecha_ingreso, hospedado, servicio_habitacion):\n",
    "        super().__init__(nombre, edad)\n",
    "        self.habitacion = int(habitacion)\n",
    "        self.rfc = str(rfc)\n",
    "        self.num_cuenta = int(num_cuenta)\n",
    "        self.fecha_ingreso = fecha_ingreso\n",
    "        self.hospedado = bool(hospedado)\n",
    "        self.servicio_habitacion = servicio_habitacion\n",
    "        \n",
    "    def saldo(self):\n",
    "        if self.hospedado == True:\n",
    "            diashosp = ((datetime.date.today()-self.fecha_ingreso)).days\n",
    "            servhab = sum(self.servicio_habitacion.values())\n",
    "            return f'Saldo al día de hoy de {self.nombre}: \\nCosto por noche $1000 \\nDías de hospedaje: {diashosp} \\nCosto estancia: ${diashosp*1000} \\nServicio a la habitación: ${servhab} \\nTotal: ${(diashosp*1000)+servhab}'\n",
    "        else:\n",
    "            return \"Esta persona ya no se encuentra hospedada\"\n",
    "        \n",
    "    def hinfo(self):\n",
    "        print(f\"Nombre: {self.nombre}\")\n",
    "        print(f\"Edad: {self.edad}\")\n",
    "        print(f\"Habitación: {self.habitacion}\")\n",
    "        print(f\"Número de cuenta: {self.num_cuenta}\")\n",
    "        print(f\"Fecha de ingreso: {self.fecha_ingreso}\")\n",
    "        print(f\"Hospedado: {self.hospedado}\")\n",
    "        print(f\"Servicio a la habitación: {self.servicio_habitacion}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "f4a0e317",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nombre: Juan \n",
      "Edad: 25\n"
     ]
    }
   ],
   "source": [
    "#Insertando una persona\n",
    "p1 = persona(\"Juan\", 25)\n",
    "print(p1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "3ef2e692",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nombre: Juan\n",
      "Edad: 25\n",
      "Habitación: 123\n",
      "Número de cuenta: 271299\n",
      "Fecha de ingreso: 2025-05-14\n",
      "Hospedado: True\n",
      "Servicio a la habitación: {'Sandwich': 120, 'Jugo de Naranja': 45}\n"
     ]
    }
   ],
   "source": [
    "#Insertando info huesped\n",
    "h1 = huesped(\"Juan\",25, 123, \"CARJ\", 271299, datetime.date(2025,5,14), True, {\"Sandwich\": 120, \"Jugo de Naranja\": 45})\n",
    "\n",
    "#Info personal del huesped\n",
    "h1.hinfo()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "d838aa89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saldo al día de hoy de Juan: \n",
      "Costo por noche $1000 \n",
      "Días de hospedaje: 4 \n",
      "Costo estancia: $4000 \n",
      "Servicio a la habitación: $165 \n",
      "Total: $4165\n"
     ]
    }
   ],
   "source": [
    "#Saldo al día de hoy\n",
    "print(h1.saldo())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "d865bfe4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nombre: Pablo\n",
      "Edad: 25\n",
      "Habitación: 456\n",
      "Número de cuenta: 28012000\n",
      "Fecha de ingreso: 2025-05-13\n",
      "Hospedado: False\n",
      "Servicio a la habitación: {'Papas': 50, 'Coca-Cola': 35}\n",
      "Esta persona ya no se encuentra hospedada\n"
     ]
    }
   ],
   "source": [
    "#Un cliente que no está hospedado\n",
    "h2 = huesped(\"Pablo\",25, 456, \"JPCR\", 28012000, datetime.date(2025,5,13), False, {\"Papas\": 50, \"Coca-Cola\": 35})\n",
    "h2.hinfo()\n",
    "print(h2.saldo())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0fb3dc82",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e9cc390",
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
