productos = ["arvejas", "porotos", "choclo", "lentejas", "garbanzos"]
costo = [35,40,30,70,80]

def calcularOferta(precioA, precioB):
    return (precioA + precioB) * 0.70


# Arvejas con otros productos
for e in range(1,len(productos)):
    print("2 latas de", productos[0], "y 1 lata de", productos[e], "$",
          calcularOferta(2*costo[0], costo[e]))


# Desde la posición 1, hasta el final
for i in range(1,len(productos)-1):
    for o in range(i+1, len(productos)):
        print("1 lata de", productos[i],"y 1 lata de", productos[o], "$",
              calcularOferta(costo[i], costo[o]))
