"""
Ejercicio 1: En un club de barrio se organizó un torneo de ajedrez. Realizar una función armarEquipos(participantes) que recibe la lista de participantes y arma una nueva lista compuesta de caracteres que representan los distintos equipos. Estos equipos serán armados con las 3 primeras letras en mayúscula del apellido de cada participante separado con un guión (“-“).

Los participantes se toman de la lista de “participantes”.
Ningún participante jugará consigo mismo.
El orden en que se arman las duplas no importa, siempre dará la misma dupla resultante (“RIO-ALV” es igual que “ALV-RIO”). Para esta lista de participantes: participantes = [‘rio’, ‘alvarez’, ‘perez’, ‘sosa’, ‘martinez’] La lista de equipos resultantes deberá verse como se ejemplifica: [“RIO-ALV”,”RIO-PER”,”RIO-SOS”,”RIO-MAR”,”ALV-PER”,”ALV-SOS”,”ALV- MAR”,”PER-SOS”,”PER-MAR”,”SOS-MAR”]
"""

def  armarEquipos(participantes):
  duplas = []
  
  for i in range(len(participantes)-1):
    participanteA = participantes[i]
    primerasLetrasParticipanteA = obtenerPrimerasLetras(participanteA,3).upper()
    
    for j in range(i+1,len(participantes)):
      participanteB = participantes[j]
      primerasLetrasParticipanteB = obtenerPrimerasLetras(participanteB,3).upper()

      resultante = primerasLetrasParticipanteA + "-" + primerasLetrasParticipanteB
      duplas.append(resultante)

  return duplas

      


# Método ultra corto
def obtenerPrimerasTresLetras(cadena):
  return cadena[0:3]


# Método recorriendo cadena y contando
def obtenerPrimerasLetras(cadena, cuantas):
  pos = 0
  primerasLetras = ""
  for letra in cadena:
    if pos < cuantas:
      primerasLetras = primerasLetras + letra
    pos = pos + 1
  return primerasLetras



jugadores =  ["rio", "alvarez", "perez", "sosa", "martinez"]
duplas = armarEquipos(jugadores)
print(duplas)
