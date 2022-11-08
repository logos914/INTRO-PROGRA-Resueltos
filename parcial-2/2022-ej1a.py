def validarPIN(cadena):

    if noTieneCuatroDigitos(cadena):
        return False

    if tieneAlgunaLetra(cadena):
        return False

    if tieneSecuencia(cadena):

        return False

    if tieneMasDeUnRepetido(cadena):
        return False

    return True









def noTieneCuatroDigitos(cadena):
    if (len(cadena) != 4):
        return True
    else:
        return False


def tieneAlgunaLetra(cadena):
    listadoDeNumerosvalidos = "0123456789"

    for nro in cadena:
        if nro not in listadoDeNumerosvalidos:
            return True
    return False


def tieneSecuencia(cadena):

    a = int(cadena[0])
    b = int(cadena[1])
    c = int(cadena[2])
    d = int(cadena[3])

    if esUnaSecuenciaAscendente(a,b,c,d) or esUnaSecuenciaDescendente(a,b,c,d):
        return True
    else:
        return False

def esUnaSecuenciaAscendente(a,b,c,d):
    if a<b and b<c and c<d:
        return True
    else:
        return False




def esUnaSecuenciaDescendente(a,b,c,d):
    if a>b and b>c and c>d:
        return True
    else:
        return False




def tieneMasDeUnRepetido(cadena):

    queNumerosAparecen = []
    cuantasVecesAparece = []

    for i in cadena:
        if aparece(i,queNumerosAparecen):
            pos = EnQuePosicionEsta(i,queNumerosAparecen)
            cuantasVecesAparece[pos] += 1
        else:
            queNumerosAparecen.append(i)
            cuantasVecesAparece.append(1)


    hayUnNumeroRepetido = False


    for cant in cuantasVecesAparece:

        if cant > 2:
            return True

        if cant == 2 and hayUnNumeroRepetido:
            return True

        if cant == 2 and (not hayUnNumeroRepetido):
            hayUnNumeroRepetido = True



    return False











def aparece(elemento, lista):
    for i in lista:
        if elemento == i:
            return True
    return False


def EnQuePosicionEsta(elemento, lista):
    for i in range(0,len(lista)):
        if lista[i] == elemento:
            return i




pin = input("Ingresá tu pin: ")

if validarPIN(pin):
    print(pin, "Pin Válido")
else:
    print(pin, "Pin no Válido")
