def anotarIdioma(idioma, listaA, listaI, listaD):

  posicionesDelIdioma = obtenerListaConPosicionesDeIdioma(idioma,listaI)

  if esteIdiomaTieneCupo(posicionesDelIdioma, listaD):
    posicionConCupo = primeraPosicionConCupo(posicionesDelIdioma, listaD)
    listaD[posicionConCupo] = listaD[posicionConCupo] - 1
    aula = listaA[posicionConCupo]
    return aula
  else:
    return 0
  



# Le paso un idioma y la lista de idiomas
# Me devuelve las posiciones donde se encuentra este idioma
def obtenerListaConPosicionesDeIdioma(idioma,listaI):
  lista = []
  for i in range(len(listaI)):
    if listaI[i] == idioma:
      lista.append(i)
  return lista



def esteIdiomaTieneCupo(posiciones, listaD):
  tieneCupo = False
  for posicion in posiciones:
    if listaD[posicion] > 0:
      tieneCupo = True
  return tieneCupo


def primeraPosicionConCupo(posiciones, listaD):
  for i in posiciones:
    if listaD[i] > 0:
      return i




AulasHabilitadas = [ 1, 2, 3, 4, 5, 6, 7, 8]
IdiomaDeCadaAula = ["I", "P", "E", "I", "E", "P", "E", "I"] # (I=Italiano P=Portugués E=Inglés) 
CantidadDispPorAula = [3, 10, 8, 15, 15, 10, 15, 15]

idioma = input("Eligir idioma")
inscriptoEnElAula = anotarIdioma(idioma, AulasHabilitadas, IdiomaDeCadaAula, CantidadDispPorAula)

if inscriptoEnElAula == 0:
  print("Lo sentimos, no hay cupo para ese idioma")
else:
  print("Su aula es: " + str(inscriptoEnElAula))

print(CantidadDispPorAula)
