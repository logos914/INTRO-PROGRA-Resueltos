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
  return cadena[-3:0]


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
