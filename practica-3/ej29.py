#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Escribir un programa que pida al usuario una 
#  cadena e indique si esta posee un diptongo 
#  (dos vocales unidas).

cadena = input("Ingresá tu palabra: ")
banderaHayPrimeraVocal = False
banderaHayDiptongo = False

# Por cada caracter de la cadena
for caracter in cadena:

    # Es una vocal ese caracter?
    if(caracter == "a" or caracter == "e" or caracter == "i"
    or caracter == "o" or caracter == "u"):

        # La letra anterior no era vocal?
        if banderaHayPrimeraVocal == False:

            banderaHayPrimeraVocal = True
        else:
            banderaHayDiptongo = True
    
    # La letra no es vocal (es consonante)
    else:
        banderaHayPrimeraVocal = False
        
if (banderaHayDiptongo):
    print("La palabra tiene diptongo")
else:
    print("La palabra NO tiene dipontongo")#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Escribir un programa que pida al usuario una 
#  cadena e indique si esta posee un diptongo 
#  (dos vocales unidas).

cadena = input("Ingresá tu palabra: ")
banderaHayPrimeraVocal = False
banderaHayDiptongo = False

# Por cada caracter de la cadena
for caracter in cadena:

    # Es una vocal ese caracter?
    if(caracter == "a" or caracter == "e" or caracter == "i"
    or caracter == "o" or caracter == "u"):

        # La letra anterior no era vocal?
        if banderaHayPrimeraVocal == False:

            banderaHayPrimeraVocal = True
        else:
            banderaHayDiptongo = True
    
    # La letra no es vocal (es consonante)
    else:
        banderaHayPrimeraVocal = False
        
if (banderaHayDiptongo):
    print("La palabra tiene diptongo")
else:
    print("La palabra NO tiene dipontongo")
