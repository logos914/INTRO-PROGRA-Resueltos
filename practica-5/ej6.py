"""
Definir una funcion que tome una lista y devuelva True si tiene al menos un elemento repetido,
y False en caso contrario.
"""



def tieneElementosRepetidos(lista):

    posActual = 0

    # Voy a recorrer cada elemento de la lista, excepto el anteúltimo
    while posActual < len(lista) - 1:

        # Voy a recorrer desde el siguiente de la posición actual, hasta el último...
        for i in range(posActual+1, len(lista)):

            # ... Para comparar siempre posActual con cada uno
            if lista[posActual] == lista[i]:
                # Si hay uno igual a otro, devolver Verdadero inmediatamente
                return True
        posActual = posActual + 1


    #Si al terminar el bucle, no devolvió Verdadero, es porque no hay elementos repetidos. Asi que devolver Falso
    return False


# Defino unas listas para probar que funcione bien
listaDePrueba1 = [1,3,3,5] # True
listaDePrueba2 = [1,3,5,7,3] # True
listaDePrueba3 = [7,2,6,1] # False
listaDePrueba4 = [1,3,5,7] #False
listaDePrueba5 = [1,3,5,7,1] #True

#No voy a guardar los valores que retorna la función, solamente imprimirlos
print(tieneElementosRepetidos(listaDePrueba1))
print(tieneElementosRepetidos(listaDePrueba2))
print(tieneElementosRepetidos(listaDePrueba3))
print(tieneElementosRepetidos(listaDePrueba4))
print(tieneElementosRepetidos(listaDePrueba5))
