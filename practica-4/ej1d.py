#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ejercicio 1 d
#Hacer un programa para cada inciso que pida al usuario un número decimal x y muestre por
#pantalla el resultado de evaluar las siguientes fórmulas:
#d)modulo de raiz de x-5



#Acá defino la función Módulo
def moduloDe(x):

    # Guardo el resultado de esta función, temporalmente aquí
    resultadoDelModulo = x

    # Si el número que pasaron por parámetro es negativo, entonces debo convertirlo
    # en un número positivo, porque el módulo es la distancia que hay entre el cero
    # y dicho número. Si es negativo, lo hago positivo multiplicandolo por -1
    if (x < 0):
        resultadoDelModulo *= (-1)
    
    # Devuelvo el resultado aquí
    return resultadoDelModulo


#Esta función le resta 5 al número, luego hace raiz cuadrada del resultado, y finalmente el módulo
def moduloDeRaizCuadradaDeEquisMenosCinco(x):
    
    # Primero los cálculos de restar 5 y luego obtener raíz cuadrada
    # Acá hay un tema, ¿Qué pasa si el x < 5? ¿Se puede obtener una raíz cuadrada de nro negativo?
    resultado=(x-5)**(1/2)

    # Luego le saco el módulo al resultado
    resultado = moduloDe(resultado)

    # Devuelvo este valor, luego de obtener los resultados
    return resultado


# Aquí empieza el programa princial
ElNumeroQueIngresaElUsuario=float(input("Ingrese un valor:"))
elResultadoQueHayQueMostrarEnPatalla = moduloDeRaizCuadradaDeEquisMenosCinco(ElNumeroQueIngresaElUsuario)
print("El resultado de restar cinco, obtener la raíz cuadrada y luego el módulo de", ElNumeroQueIngresaElUsuario, "es:", elResultadoQueHayQueMostrarEnPatalla)


