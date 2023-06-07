listaV1 = []
listaV2 = []
listaV3 = []


for vuelvo in vuelos():
    if horasdeVuelvo(vuelo) > 12 and escalasenVuelo(vuelo) == 0:
        listaV1.append(vuelo)
    else:
        if horasdeVuelvo(vuelo) <= 12 and horasdeVuelvo(vuelo) > 8 and escalasenVuelo(vuelo) == 1:
            listaV2.append(vuelo)
        else:
            listaV3.append(vuelo)


confirmaVuelosV1(listaV1)
confirmaVuelosV2(listaV2)
confirmaVuelosV3(listaV3)

if len(listaV1) + len(listaV2) < len(listaV3):
    emitirAlerta()
