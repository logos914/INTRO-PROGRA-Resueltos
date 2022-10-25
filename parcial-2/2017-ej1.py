"""
Ejercicio 1: (2.5 puntos)
Se cuenta con las siguientes listas:
    • lista: con las materias en las que un alumno ("Pedro") desea inscribirse.
    • lista1: con las materias de la carrera. (*)
    • lista2: con las vacantes disponibles para cada materia. (*)
(*) lista1 y lista2 son de igual tamaño y las materias se corresponden con las vacantes.
Se solicita escribir una función llamada inscribirEn(lista,lista1,lista2) que inscriba al alumno en cada una de las materias solicitadas, siempre y cuando haya vacantes disponibles. La función deberá mostrar para cada materia solicitada un cartel que diga "Pedro se inscribió en la materia x" ó "Pedro no se pudo inscribir en la materia x " (según corresponda). Además deberá devolver las vacantes disponibles, descontando las vacantes asignadas al alumno. 

Ejemplo: 
lista=["IP","P1","TU"]
lista1=["P1","P2","P3",""TU","MD","BD1","BD2","IP"]
lista2=[58,42,21,40,25,15,12,0]

Debería emitir "Pedro no se pudo inscribir en IP"
"Pedro se inscribió  en P1"
"Pedro se inscribió  en TU"
Devolviendo 
lista2=[57, 42, 21, 39, 25, 15, 12, 0]
"""


def inscribirEn(lista,lista1,lista2):
    
    # Este proceso hay que hacerlo para cada materia en la que el estudiante se haya inscripto
    # El listado son los elementos de lista
    for materia in lista:
        
        
        # Por cada materia en la que el estudiante intenta inscribirse, necesito saber que índice tiene en lista1 y lista2
        indice = encontrarIndiceDeMateria(materia, lista1)
        
        # Si se puede inscribir en la materia actual
        if sePuedeInscribirEnMateria(indice, lista2):
            
            # Entonces imprimo mensaje de que se puede inscribir y decremento las vacantes de dicha materia
            print("El estudiante se inscribió en " + materia)
            
            # Es un poco exagerado, pero ojala este ejemplo sirva para ver como se pueden utilizar las funciones
            # para reorganizar el código. Esta línea se podía reemplazar con:
            # lista2[indice] = lista2[indice] - 1
            lista2 = decrementarElCupo(indice, lista2)
        
        
        # si no se pudo inscribir (porque ya no vacantes)
        else:
            
            # Entonces solamente imprimo el mensaje de que no se pudo inscribir
            print("El estudiante no se pudo inscribir en " + materia + " por falta de cupo")
            
            
        
    #Luego devolvemos la lista2 ya modificada
    return lista2
            
             


# Obtengo el indice que ocupa una materia en el listadoDeMaterias (lista1). Lo busca si como primer parámetro pasamos
# el nombre de la materia como una cadena de caractéres
def encontrarIndiceDeMateria(nombreMateria, listadoDeMaterias):
    for i in range(len(listadoDeMaterias)):
        if (nombreMateria == listadoDeMaterias[i]):
            return i


# Simplemente calcula si la materia indicada por el índice en la listaDeVacantes (lista2) tiene cupo (es mayor a cero)
# y retorna True si hay cupo o False en caso contrario
def sePuedeInscribirEnMateria(indice, listaDeVacantes):
    if listaDeVacantes[indice] > 0:
        return True
    else:
        return False
    


# Decrementa el cupo de la materia indicada por el índice en la listaDeVacantes
# y retorna True si hay cupo o False en caso contrario
def decrementarElCupo(indice, listaDeVacantes):
    listaDeVacantes[indice] = listaDeVacantes[indice] - 1
    return listaDeVacantes



# ¿Cómo se ejecuta? El ejercicio no lo pide, pero podemos probar usar las funciones con los valores de ejemplo

lista=["IP","P1","TU"]
lista1=["P1","P2","P3","TU","MD","BD1","BD2","IP"]
lista2=[58,42,21,40,25,15,12,0]

lista2 = inscribirEn(lista,lista1,lista2)



AsiTendriaQueSer=[57, 42, 21, 39, 25, 15, 12, 0]

if lista2==AsiTendriaQueSer:
    print("Genial, nuestro código da el mismo resultado que el ejemplo del enunciado")


