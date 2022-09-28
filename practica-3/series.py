#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = int(input("Ingrese hasta que valor de n calcular la serie"))

valor = 0 # variable acumuladora
for i in range(1,n+1,1):
    TotalConGanancia = ((-1)**(i+1)) * (i) / (i**(i+1)) 
    print(i,"->",TotalConGanancia)
    valor += TotalConGanancia

print("El resultado de la serie hasta n =",n, " es: ", valor)
