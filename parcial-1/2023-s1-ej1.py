"""
    Cada cliente de un banco, recibe por su cuenta bancaria (caja de ahorros o cuenta corriente) un CBU. Este CBU o Clave Bancaria Uniforme consiste en una cadena de caracteres compuesta de 22 dígitos. En ella se encuentra codificados ciertos datos:
•	La entidad bancaria es identificada con un número de tres cifras. Y son los tres primeros dígitos del CBU.
•	La sucursal del banco en dónde se encuentra creada la cuenta son los dígitos 4 a 7 inclusive del CBU.
•	El número de cuenta bancaria son 11 dígitos compuestos por el número de sucursal del banco y los dígitos 15 a 21 del CBU.

a) Se solicita un programa, que al ingresarle un CBU, imprima en pantalla a qué número de banco pertenece y cuál es el número de cuenta en dicho banco.

Ejemplo: 
Dado el CBU: “0720173488000020067922”, el programa devuelve:
banco = “072” y cuenta = “01732006792”

b) Además se quiere saber cuánto vale la suma de dígitos que componen el número de cuenta sin los dígitos que corresponden al número de sucursal

Ejemplo: 2+0+0+6+7+9+2 = 26

Nota: No se puede acceder a los caracteres de la cadena por posición

"""

cbu = input("Ingrese el CBU: ")
banco = ""
sucursal = ""
soloCuenta = ""
cuentaConSucursal = ""

posicion = 0

for carac in cbu:
    posicion = posicion + 1
    
    if posicion <= 3:
        banco = banco + carac
    
    if posicion > 4 and posicion <= 7:
        sucursal = sucursal + carac
    
    if posicion >= 15 and posicion <= 21:
        soloCuenta = soloCuenta + carac

cuentaConSucursal = sucursal + soloCuenta

print("El banco es: " + banco, " y la cuenta es: " + cuentaConSucursal)
    
suma = 0
for i in soloCuenta:
    suma = suma + int(i)
print(suma)