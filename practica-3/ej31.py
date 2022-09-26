#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ejercicio 31
Hacer un programa que genere una clave provisoria para la gestión online de clientes de una
empresa. El programa le pedirá el apellido y generará una clave de 5 caracteres, tomará las
primeras 4 consonantes de la palabra ingresada. Cuando las consonantes no alcancen a 4, las
faltantes las reemplazará por "*". Ejemplos:
clemente CLMN
rivera RVR*
oreo R***
La clave se completará con 1 dígito generado aleatoriamente entre 0 y 9.
Ejemplos: CLMN1 RVR*4 R***7"""

import random

apellido = input("Ingrese el apellido: ")

vocales = "aeiou"

contrasenia = ""
consonantesDelApellido = ""

# Con este bucle, obtengo todas las letras consonantes
for letra in apellido:

    if (letra not in vocales):
        consonantesDelApellido += letra.upper()

# Voy a agregar las consonantes a la contraseña, siempre hasta llegar a 4 
for letra in consonantesDelApellido:
    if (len(contrasenia) < 4):
        contrasenia += letra

# Ahora reviso que si la contraseña por ahora tiene menos de 4 caracteres, agrego los asteriscos que faltan
if len(contrasenia) < 4:
    cuantosFaltanCaracteresFaltan = 4 - len(contrasenia)

    # Agrego los asteriscos que faltan
    for i in range(cuantosFaltanCaracteresFaltan):
        contrasenia += "*"

# Finalmente agrego el caracter numérico random que falta
contrasenia += str(random.randint(0,9))

# Muestro por salida la clave
print(contrasenia)
