# Ejercicio 3: (2,5 puntos)
"""
Hacer un programa que solicite al usuario n números enteros y muestre por pantalla 
los que se ingresaron más de una vez (sin repetirlos). 

El número n se debe solicitar primero al usuario y controlar que sea un número natural. 
Observación: de ser necesario se pueden crear y usar funciones.
"""

def estanRepetidos(listaParaEncontrarRepetidos):
    
    listaRepetidos = []
    
    for i in range(0,len(listaParaEncontrarRepetidos)-1):
        for o in range(i+1, len(listaParaEncontrarRepetidos)):
            if (listaParaEncontrarRepetidos[i] == listaParaEncontrarRepetidos[o]):
                if not estaEnLaLista(listaRepetidos,listaParaEncontrarRepetidos[i]):
                    listaRepetidos.append(listaParaEncontrarRepetidos[i])
    
    return listaRepetidos
      

def estaEnLaLista(lista, numero):
    for e in lista:
        if e == numero:
            return True
    return False


#Programa Principal
n = int(input("¿Qué cantidad de números queres ingresar? "))
cantidadDeNumerosPreguntados = 0
lista = []


while (cantidadDeNumerosPreguntados < n):
    nroIngresado = int (input("Ingresá el número "))
    lista.append(nroIngresado)
    cantidadDeNumerosPreguntados +=1
    

listaConLosRepetidos = estanRepetidos(lista)
print(listaConLosRepetidos)


