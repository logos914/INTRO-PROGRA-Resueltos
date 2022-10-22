#!/usr/bin/env python
# -*- coding: utf-8 -*-

cadena = "Hola Soy una Cadena"

for caracter in cadena:
    print(caracter)




contadoraDeLetras = 0
for caracter in cadena:
    contadoraDeLetras += 1
    print(contadoraDeLetras, "->", caracter)
