#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Esta función debe devolver ¡unaCadena!
def exclamar(unaCadena):
    
    #Exclamar consiste en concatenar a la cadena origna, los signos de admiración adelante y atras
    cadenaConExclamacion = "¡" + unaCadena + "!"

    # Una vez que tengo la frase con la exclamación la devuelvo
    return cadenaConExclamacion


# Esta función debe devolver ¡¡¡unaCadena!!!
def gritar(unaCadena):

    #Necesito exclamar la cadena 3 veces antes de retornarla, tengo varias maneras de hacerlo

    # Opción 1, muy repetitiva
    nuevaCadena = exclamar(unaCadena)
    nuevaCadena = exclamar(nuevaCadena)
    nuevaCadena = exclamar(nuevaCadena)


    # Opción 2, metiendo el resultado de exclamar, dentro de otra exclamar, así 3 veces. Muy confusa de escribir y leer
    nuevaCadena  = exclamar(exclamar(exclamar(nuevaCadena)))
    
    # Opción 3, buclear
    nuevaCadena = unaCadena
    for i in range(3):
        nuevaCadena = exclamar(nuevaCadena)

    return nuevaCadena


# Aquí empieza mi progama principal
# Le pido una frase al usuario, la hago gritar a la frase, la guardo en una variable y finalmente la imprimo


fraseParaGritar = input("Escribí una frase: ")

fraseGritando = gritar(fraseParaGritar)

print(fraseGritando)
