sabores = ["chocolate", "dulce de leche", "limón", "vainilla", "frutilla"]
costo_de_1_litro = [600, 480, 360, 420, 300]
listadoDeOfertas=[]

def combinarDosSaboresEnUnLitro(posA, posB, listadoDePrecios):
    precioA = listadoDePrecios[posA]
    precioB = listadoDePrecios[posB]

    return (precioA / 2) + (precioB / 2)

def combinarTresSaboresEnCincoLitros(posA, posB, posC, listadoDePrecios):
    precioA = listadoDePrecios[posA]
    precioB = listadoDePrecios[posB]
    precioC = listadoDePrecios[posC]

    total = round(1.667 * (precioA + precioB + precioC),0)
    return total


for i in range(0,len(sabores)-2):
    for o in range(i+1, len(sabores)-1):
        listadoDeOfertas.append(
            sabores[i] + " - " +
            sabores[o] + " x 1 litro : $" +
            str(combinarDosSaboresEnUnLitro(i,o,costo_de_1_litro))
                                )

        listadoDeOfertas.append(
        sabores[len(sabores) - 1] + " - " +
        sabores[i] + " - " + sabores[o] +
        " x 5 litros : $" +
        str(combinarTresSaboresEnCincoLitros(len(sabores) - 1, i, o, costo_de_1_litro))
                                )






for i in listadoDeOfertas:
    print(i)

