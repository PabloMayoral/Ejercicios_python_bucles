# 1. Imprime por pantalla tu nombre y apellidos
# Crea una variable de tipo int con tu edad e imprímela por pantalla (Ej: "Tengo X años")
# Crea una variable de tipo bool que sea False e imprímela por pantalla.
# Crea una variable de tipo float con 2 decimales que exprese la nota que vas a sacar en esta asignatura.

print('Pablo Martín Mayoral')
edad = 20
print('Tengo '+str(edad)+' años')
findeSemana= False
print (findeSemana)
x=9.34
print(x)
print('------------------------------------------------------------------------------------------')

# 2. Crea una variable de tipo tupla, otra de tipo lista, 
# otra de tipo cadena y otra que sea un número con los valores que quieras
# e imprímelos por pantalla siguendo el siguiente orden:
# 1º Lista.
# 2º Tupla.
# 3º Número.
# 4º Cadena.

tupla = (('1','2','3'),('2','4','6'),('3','6','9'))
paises=['España','Francia','Inglaterra']
numero=2022
cadena = 'esto es una cadena'
print(tupla)
print(paises)
print(numero)
print(cadena)
print('------------------------------------------------------------------------------------------')


# 3. Realiza una operación de suma, otra de resta, otra de multiplicación y
# otra de división e imprímelos en el siguiente orden:
# 1º Multiplicación.
# 2º División.
# 3º Suma.
# 4º Resta.
# EXTRA: Calcula el resto de la división 15 entre 2 e imprímelo por pantalla.

#CREO VARIAS FUNCIONES ESTANDAR PARA LAS DIFERENTES OPERACIONES LUEGO EN LOS PRINT LES DOY EL VALOR DE CADA VARIABLE
def multiplicacion(a, b):
    multiplicacion = a * b
    return multiplicacion
print(multiplicacion(10,5))

def division(a, b):
    division = a / b
    return division
print(division(10,5))

def suma(a, b):
    suma = a + b
    return suma
print(suma(10,5))

def resta(a, b):
    resta = a - b
    return resta
print(resta(10,5))

def resto(a, b):
    resto = a % b
    return resto
print(resto(15,2))

print('------------------------------------------------------------------------------------------')

# 4. Crea 5 números en una sola línea de código que tengan el valor 5.
# Incrementa en 1 el valor del 1º de ellos.
# Decrementa en 1 el valor del 2º de ellos.
# Multiplica por 2 valor del 3º de ellos.
# Divide entre 2 valor del 4º de ellos.
# Calcula el módulo 2 del 5º de ellos.
# Imprime todos los números resultantes por pantalla.

x=y=z=t=j = 5
x +=1
y -=1
z *= 2
t /= 2
j %= 2
print(x,y,z,t,j)
print('------------------------------------------------------------------------------------------')

# 5. Escribe las siguientes condiciones e imprime el mensaje por pantalla en cada caso
# (Recuerda que deberás rellenar las variables y en algún caso, crear tú alguna):
#
# Si tu edad es mayor que 19 -> Imprime: "Soy mayor de 19".
#
# Si tu equipo es igual a "Real Madrid" -> Imprime: "Soy madridista".
#
# Si tu número de zapato es mayor que 44 -> Imprime: "Menudo piezaco!".
#
# Si tu ciudad es pozuelo -> Imprime: "Soy de Pozuelo".

edad = 20
if edad > 19:
    print('Soy mayor de 19')
else:
    print('No soy mayor de 19')

equipo_pocho = 'Real Madrid'   
equipazo = 'Atletico de Madrid'

if equipazo == equipo_pocho:
    print('Soy madridista')
else:
    print('Soy colchonero')

tallaPie = 43

if tallaPie > 44:
    print('menudo piezaco!')
else:
    print('buen pie')

ciudadOrigen = 'Madrid'
ciudadPrueba = 'Pozuelo'

if ciudadOrigen == ciudadPrueba:
    print('soy de Pozuelo')
else: 
    print('No soy de Pozuelo')
print('------------------------------------------------------------------------------------------')

# 6. Escribe las siguientes condiciones e imprime el mensaje por pantalla en cada caso
# (Recuerda que deberás rellenar las variables y en algún caso, crear tú alguna)
# (Usa el ejercicio anterior como esquema):
#
# Si tu edad es mayor o igual que 10 -> Imprime: "Soy mayor o igual de 10".
# Si no: Imprime tu edad.
#
# Si tu equipo es igual a "Real Madrid CF" -> Imprime: "Soy madridista".
# Si no: Imprime tu equipo (o si no tienes dilo!).
#
# Si tu número de zapato es mayor que 44 pero menor que 46 -> Imprime: "Tengo un 45".
# Si no: Imprime tu número de zapato.
#
# Si tu ciudad es pozuelo o majadahonda -> Imprime: "Vivo cerca de la uni.
# Si no: Imprime donde vives.
    
if edad >= 10:
    print('Soy mator o igual de 10')

if equipazo == equipo_pocho:
    print('Soy madridista')
else:
    print('Soy colchonero')

if tallaPie > 44 and tallaPie < 46:
    print('tengo un 45')
else:
    print('tengo un '+ str(tallaPie))

if ciudadOrigen == ciudadPrueba:
    print('Vivo cerca de la uni')
else: 
    print('vivo lejos de la uni')
print('------------------------------------------------------------------------------------------')

    

    
