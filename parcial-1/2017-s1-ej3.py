"""
Ejercicio 3: (2.5 puntos)
Hacer un programa que solicite el ingreso de 2 palabras que deben ser distintas y determine si ambas tienen la misma cantidad de vocales (aunque estas sean distintas).
 
Ejemplo: roma y amor tienen 2 vocales, tienen igual cantidad 
	    siesta y mueble tienen 3 vocales, igual cantidad
	    rama y pizza tienen 2 vocales, igual cantidad
	    carpeta y lápiz, no tienen igual cantidad de vocales	
"""

# La primera palabra se la pido al usuario
palabra1 = input("Ingrese la primera palabra: ")

#Para no tener problemas en dónde una vocal mayúscula no es igual a una 
#vocal mínúscula, pongo todo en minúscula. (Como "A" != "a")
palabra1= palabra1.lower()

# La segunda palabra la dejo vacía por ahora.
palabra2 = ""

# Evito que la segunda palabra sea igual que la primera o que quede vacía
while palabra1 == palabra2 or palabra2 == "":
  palabra2 = input("Ingrese la segunda palabra: ")
  palabra2 = palabra2.lower()

# Inicializo unos contadores. Voy a contar vocales para cada palabra. 
# Por ahora no conté ninguna vocal. Así que empiezan en cero
cantVocalesPalabra1=0
cantVocalesPalabra2=0




# Recorrermos caracter por caracter de la primera palabra
# Para ello usamos un for y la variable caracterActual para evaluar
# justamente cada caracter o letra de la primera palabra.
for caracter in palabra1:

  #Pregunto si este caracter es una vocal, método largo.
  if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":

    #Si es vocal, le sumamos al contador
    cantVocalesPalabra1+=1
  

#Hacemos lo mismo con la segunda palabra
for caracter in palabra2:

  #Pregunto si este caracter es una vocal, método vagancia.
  if caracter in "aeiou":

    cantVocalesPalabra2+=1



#Comparamos las cantidades de vocales para mostrar el mensaje final adecuado

if cantVocalesPalabra1 == cantVocalesPalabra2:
  print(palabra1, "y",palabra2,"tinen", cantVocalesPalabra1, "vocales. Es decir igual cantidad.")

else:
  print(palabra1, "y",palabra2,"no tinen la misma cantidad de vocales")



