"""
Ejercicio 4: (2,5 puntos)
Una fábrica de motores debe organizar sus motores en función de sus códigos o sea según para que herramienta se utilicen 
dichos motores. Para lo cual cuenta con varias funciones:

motores(): Devuelve una lista de motores.
leerCodigoMotor(motor): Dado un motor la función devuelve un número; 
                        1 si el motor es para un taladro, 2 si es para una motosierra y 3 si es para una caladora.
ingStockT(motor): Si el motor tiene código 1 lo ingresa al stock.
ingStockM(motor): Si el motor tiene código 2 lo ingresa al stock.
ingStockC(motor): Si el motor tiene código 3 lo ingresa al stock.
alerta(): manda un aviso al supervisor en caso de que sea necesario.

Armar una función que dada la lista de motores, ingrese los mismos al stock que corresponda según el tipo de motor. 
La producción debe ser pareja en cuanto a las cantidades por lo que se mandará un alerta al supervisor en caso de que
alguno de los tipos de motores supere el 33%.

"""


#Me piden armar una función. La voy a llamar, organizadoraDeStock

def organizadoraDeStock():
    
    # Necesito la lista de motores que hay que organizar. Siempre que una función devuelve una valor o lista,
    # la guardo en una variable temporal.
    
    listadoDeMotores = motores()
    
    
    # También me piden que lleve un control de la cantidad de cada tipo de motor porque no se tiene que desbalancear la producción
    # Asi que agregamos algunos contadores para cada tipo de motor. Obviamente empezamos en cero.
    
    cantTipoTaladros = 0
    cantTipoMotosierra = 0
    cantTipoCaladora = 0
    
    # Necesito analizar el código de cada uno de los motores de la lista. Y analizo la propiedad del motor (el tipo de motor,
    # si es taladro, motosierra, etc). Entonces no necesito saber la posición en la lista. Recorro el listado entonces.
    
    
    
    for motor in listadoDeMotores:
        
        # La variable motor, contiene el motor actual. 
        # Lo analizo con la función que me devuelve su tipo y guardo ese número en otra variable temporal.
        tipo = leerCodigoMotor(motor)
        
        # Dependendiendo el tipo entonces debo mandarlo al stock que corresponde
        
        if (tipo ==1):
            ingStockT(motor)
            cantTipoTaladros +=1
        if (tipo ==2):
            ingStockM(motor)
            cantTipoMotosierra +=1
        if (tipo==3):
            ingStockC(motor)
            cantTipoCaladora +=1
    
    # Listo terminé con la parte principal pero también me pidieron dar alerta si el stock de algún motor supera el 33%
    # Fijarse que lo hacemos luego de que terminó el bucle.
    # Nuestra función, ya ha realizado dos tareas importantes:
    # 1) Clasificar cada motor en su stock
    # 2) Contar cada tipo de stock.
    # Quiere decir que nuestra función ya está muy cargada. Deberíamos crear otra función para que haga la tarea de revisar
    # que la producción se encuentre balanceada y dar el aviso. La que llamaremos desde nuestra propia función.
    
    revisarBalacenDeProduccion(cantTipoTaladros, cantTipoMotosierra, cantTipoCaladora)
    

def revisarBalacenDeProduccion(taladros, motosierras, caladoras):
    
    # Obtengo el total para saber cuantos motores es el 100%
    totalProduccion = taladros + motosierras + caladoras   
    
    # Regla de tres simple: Si el total de produción, es el 100% (es decir es 1 xq 1 es el 100% y 2 es el 200%)
    # Entonces el cant de taladros * 1 / totalProduccion es el porcentajeTaladros
    
    #Obtengo el procentaje de cada tipo
    porcentajeTaladros = taladros / totalProduccion
    porcentajeMotosierras = motosierras / totalProduccion
    porcentajeCaladoras = caladoras / totalProduccion
    
    #Utilizo otra función, creada por nosotros mismos que lanza la alarma si es necesario.
    siEsNecesarioLanzarAlerta(porcentajeTaladros)
    siEsNecesarioLanzarAlerta(porcentajeMotosierras)
    siEsNecesarioLanzarAlerta(porcentajeCaladoras)
    


def siEsNecesarioLanzarAlerta(cantidad):
    if cantidad > 0.33:
        alerta()
    
     
    
    
