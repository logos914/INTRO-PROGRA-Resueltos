#Ejercicio 17
#Definir una función llamada mcd que tome dos enteros positivos y devuelva el máximo común
#divisor usando funciones de los ejercicios anteriores.

def esta (entero,lista):
    for elemento in lista:
        if elemento==entero:
            return True
    return False

def interseccion(lista1,lista2):
    lista_Nueva=[]
    for i in lista1:
        if esta(i,lista2):
            lista_Nueva.append(i)
    return lista_Nueva

def divisores(n):
    divisoresDeN=[]
    for i in range(1,n+1):
        if n%i==0:
            divisoresDeN.append(i)
    return divisoresDeN



def maximo(lista):
    max=lista[0]
    for i in lista:
        if i > max:
            max=i
    return max

def mcd (a,b):
    divA=divisores(a)
    divB=divisores(b)
    divComunes=interseccion(divA,divB)
    MCD=maximo(divComunes)
    return MCD

a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero: "))
print (mcd(a,b))