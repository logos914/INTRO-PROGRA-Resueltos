#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio 2, Tema B, Primer Parcial, Comisión 2, Semestre 2, 2022

Escribir un programa que calcule el valor de la siguiente suma de n términos,
teniendo en cuenta que n es un número natural introducido por el usuario.
(Controlar el valor de n que ingresa el usuario)
Por ejemplo para n = 6, la seguir siguiente:

1/1 , 1/2 , 1/4 , 1/8 , 1/16 , 1/32
"""

n = 0 
resultado = 0
while (n<=0):
    n = int(input("Ingrese un número natural (por ejemplo: 6): "))


for i in range(1,n+1):
    resultado +=  ( 1 ) / ( (2)**(i-1) )

print(resultado)




