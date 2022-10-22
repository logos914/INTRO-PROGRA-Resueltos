#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
f=input("ingrese su frase")
c=""
i=1
vocales="aeiou"
for letra in f:
    if letra!=" ":
        if (letra in vocales ):
            c= c+ str(random.randrange(1,6))
        else:
                if not (letra in vocales):
                    c= c+ letra.upper()

    else:
        i=i+1
c=c+str(i)


print(c)
