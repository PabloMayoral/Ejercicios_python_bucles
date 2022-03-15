#1. Crea una función que reciba como parámetros 2 números y devuelva si son múltiplos.
def multiplo(a,b):
    return a % b == 0
print(multiplo(10,3))
#2. Crea una función que reciba una lista y una variable, debe indicar si el 
#elemento que hay en la variable está en la lista y en que posición.
def buscaElemento(lista,variable):
    j = 0
    for i in lista:
        if i == variable:
            print('La variable = '+variable+' está en la posición: '+str(j))
        j += 1
buscaElemento(['mensaje','prueba',1,'mensaje','mensaje'],'mensaje')

#3. Crea una función que admita un numero indeterminado de numeros, deberá calcular
#la media de los numeros (el total de números divididos entre el numero total de 
#números).

def media(*numeros):
    cantidadNum = len(numeros)
    suma = 0
    for i in numeros:
        suma = suma + int(i)
    return suma/cantidadNum
print(media(1,2,3,4))
#4. Crea una función que reciba un texto, deberá devolver ese mismo texto pero con 
#un espacio adicional tras cada letra.

def espacios(texto):
    casteo = list(texto)
    w = 0
    for i in casteo:
        casteo[w]= i+ ' '
        texto = "".join(casteo)
        w += 1
    print(texto)
espacios('Un renovación sumamente importante dentro del evolución del hombre moderno')

#5. Crea una función que reciba una lista de números como parámetro y un valor 
#booleano que por defecto será True. 
# Deberá devolver el máximo valor si ese valor booleano es True de todos los 
#números de la lista, y el mínimo si el valor booleano es False.
def maxMin(lista,booleano):
    lista.sort()
    if booleano == True:
        print(lista[-1])
    else:
        print(lista[0])
maxMin(list(range(0,11)),True)

        

       
