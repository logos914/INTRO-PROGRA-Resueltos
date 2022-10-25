"""
Ejercicio 2: (2,5 puntos)
Se dispone de una lista con los precios de productos importados; el primer valor de la lista 
corresponde al valor del dólar con que fue calculada la lista. 

Se necesita modificar la lista por la variación del tipo de cambio.
El nuevo valor del dólar se ingresa por teclado.

a) Hacer una función que modifique la lista 
b) Hacer un programa principal que solicite el nuevo valor del dólar, llame a la función y luego muestre la lista modificada.

Ejemplo:
lista= [20.50,1.10 ,1.20, 2.50, 3.25, 5.50]
dolar= 24.60
listam= [24.60, 1.32, 1.44, 3.00, 3.90, 6.60]

"""

# Acá resolvemos la parte A del enunciado
def actualizarListaDePrecios(lista, valorDolarActualizado):
    
    
    
    # Ejecuto mi función que calcula la diferencia. El valor viejo del dolar se encuentra en la pŕimera posición de la lista "lista"
    # mientras que el nuevo valor, es la variable nuevoDolar
    diferencia = calcularDiferenciaEntreDolares(lista[0], valorDolarActualizado)
    
    # Ahora necesitamos saber que porcentaje representa esa diferencia con respecto al viejo valor
    # Consideramos que el precio viejo del dolar es el 100% (el 1.00)
    porcentajeDeDiferencia = calcularPorcentaje(lista[0],diferencia)
    
    #Redondeamos a dos dígidos el porcentaje
    porcentajeDeDiferencia = round(porcentajeDeDiferencia, 2)
    
    #Ahora obtener el porcentaje nuevo con el que cada producto debe modificarse. Esto sería la variación.
    # El 1.00 representa el 100% del valor anterior. Si el dolar nuevo es mayor, entonces el porcentajeDeDiferencia es
    # positivo, lo que significa que se aumentará el precio. Por ej, porcentajeDeDiferencia es 0.05 (5%) entonces, 
    # hay que multiplicar cada viejo valor por 1.05.
    #
    # Si el precio del dolar bajara, entonces el porcentajeDeDiferencia sería negativo, restándose al 1.00 del total
    # Por ej, si el dolar cae un 3%, entonces porcanteDeDiferencia == -0.03 Lo que da una variacion de 0.97
    variacion = 1.00 + porcentajeDeDiferencia
    
    
    
    
    
    # La nueva lista debe comenzar con el valor actual del dolar ,asi que guardemos como primer elemento el nuevoDolar
    nuevaLista = [valorDolarActualizado]
    
    
    # Recorremos los precios de la lista para agregarlos a la nueva. Obviamente exceptuamos recorrer la posición 0 porque no tiene precio de producto
    # Tiene el precio viejo del dolar.
    for i in range(1,len(lista)):
        
        # Antes de appendear los valores a la lista, debemos calcular el valor nuevo de cada producto, multiplicando su valor por
        # la variación
        nuevaLista.append(round(lista[i] * variacion,2))
        
    
    
    #Devolvemos la lista con el dolar actual y con los valores ya calculados
    return nuevaLista
        


   
# Funciones auxiliares que ayudan a que el código se entienda mejor y esté más ordenado
def calcularPorcentaje(ValorDelCienPorciento,ValorQueSeQuiereConocerQuePorcentajeEs):
    
    #regla de 3 simple
    return ValorQueSeQuiereConocerQuePorcentajeEs * 1.00 / ValorDelCienPorciento
    
    
def solicitarNuevoValorDelDolar():
    valor = float(input("Ingrese el valor actual el dolar: U$D"))
    
    while valor < 0:
        valor = float(input("Ingrese el valor actual el dolar: U$D"))
        
    return valor


def calcularDiferenciaEntreDolares(viejoValorolar, nuevoValorDolar):
    
    #El dolar puede subir de precio o bajar de precio, asi que es muy importante el órden en que saco la diferencia
    # y el signo de dicha variación
    # Si sube 5 dolares, return 5
    # Si baja 5 dolares, return -5
    return nuevoValorDolar - viejoValorolar
    
    
#Acá se responde la parte B del enunciado
def programaPrincipal():
    nuevoDolar = solicitarNuevoValorDelDolar()  
    lista = [20.50,1.10 ,1.20, 2.50, 3.25, 5.50]
    listam = actualizarListaDePrecios(lista, nuevoDolar)
    print(lista)
    print(listam)
    
    
    
    

#Ejecutamos la función de nuestro programa principal
programaPrincipal()
