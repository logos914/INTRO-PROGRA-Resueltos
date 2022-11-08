
def corregirEspacios(frase):

    fraseCorregida = quitarEspaciosEnPrimeraPalabra(frase)
    fraseCorregida = quitarEspaciosAlFinalDeLaUltimaPalabra(fraseCorregida)
    fraseCorregida = soloUnEspacioEntrePalabras(fraseCorregida)
    return fraseCorregida




def quitarEspaciosEnPrimeraPalabra(frase):
    if frase[0] == " ":
        return frase[1:]
    else:
        return frase



def soloUnEspacioEntrePalabras(frase):

    banderaHayEspacioEnBlanco = False
    fraseSinDoblesEspacios = ""

    for caracter in frase:
        if caracter == " ":
            if not banderaHayEspacioEnBlanco:
                fraseSinDoblesEspacios = fraseSinDoblesEspacios + caracter
                banderaHayEspacioEnBlanco = True
        else:
            fraseSinDoblesEspacios = fraseSinDoblesEspacios + caracter
            banderaHayEspacioEnBlanco = False

    return fraseSinDoblesEspacios


def quitarEspaciosAlFinalDeLaUltimaPalabra(frase):
    longitud = len(frase)
    if frase[longitud - 1] == " ":
        return frase[0:longitud - 1]
    else:
        return frase



dato = " Nos los  represetantes  del pueblo de la  Nación "
corregida = corregirEspacios(dato)
print(corregida)