#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ejercicio 1 d
#Hacer un programa para cada inciso que pida al usuario un número decimal x y muestre por
#pantalla el resultado de evaluar las siguientes fórmulas:
#d)modulo de raiz de x-5


def moduloDeRaizCuadradaDeEquisMenosCinco(x):
    resultado=(x-5)**(1/2)
    if resultado<0:
        resultado *= -1
    return resultado



ElNumeroQueIngresaElUsuario=float(input("Ingrese un valor:"))
elResultadoQueHayQueMostrarEnPatalla = moduloDeRaizCuadradaDeEquisMenosCinco(ElNumeroQueIngresaElUsuario)
print("El resultado de restar cinco, obtener la raíz cuadrada y luego el módulo de", ElNumeroQueIngresaElUsuario, "es:", elResultadoQueHayQueMostrarEnPatalla)


