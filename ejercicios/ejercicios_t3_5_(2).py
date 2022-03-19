import random

'''#1. Crear una función que reciba una lista de elementos de diferentes tipos (al 
menos 5), 
#deberá contabilizar el numero de elementos que hay de cada tipo, mostrar por 
pantalla cada uno de los elementos
#de los que sean de tipo avanzado y devolver un diccionario con e tipo (clave) y el
numero de veces que aparece ese tipo en la lista '''
def tipos(lista):
    copylista = lista.copy() 
    dict1 = {}
    resultado = 1
    for i in lista:
        for j in copylista:
            if type(i) == type(j):
               dict1[type(i)] =resultado + 1
            else:
                dict1[type(i)] = resultado
    return dict1
print(tipos([11,['a','b'],(1,2),{'nombre':'Pablo','Apellidos':'Martin'},'texto',87.2,[1,2]]))
print('________________________________________________________________________')
#2. Definir una variable de tipo texto con varios párrafos. 
#Hacer una función que reciba ese texto definido previamente y una operación que 
#podrá ser: 
# - "CES" --> contará cuantas "c" o "C" hay en el texto y devolverá el numero. 
# - "ESPACIOS" --> contará cuantos espacios en blanco hay y devolverá el número. 
# - "VUELTA" --> devolverá el texto al revés. 

parrafos = '''Contrary to popular belief, Lorem Ipsum is not simply random text.
              It has roots in a piece of classical Latin literature from 45 BC, 
              making it over 2000 years old. Richard McClintock, a Latin professor
              at Hampden-Sydney College in Virginia, looked up one of the more obscure
              Latin words, consectetur, from a Lorem Ipsum passage, and going through
              the cites of the word in classical literature, discovered the undoubtable source.
              
              Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum"
              (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on 
              the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum,
              "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
    
              The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those 
              interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero
              are also reproduced in their exact original form, accompanied by English versions from the
              1914 translation by H. Rackham.

              There are many variations of passages of Lorem Ipsum available, but the majority have 
              suffered alteration in some form, by injected humour, or randomised words which don't look 
              even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be 
              sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum
              generators on the Internet tend to repeat predefined chunks as necessary, making this the 
              first true generator on the Internet. It uses a dictionary of over 200 Latin words, 
              combined with a handful of model sentence structures, to generate Lorem Ipsum which looks 
              reasonable. The generated Lorem Ipsum is therefore always free from repetition, 
              injected humour, or non-characteristic words etc.'''

def contadores(texto):
    cuentaC = 0
    cuentaEspacios = 0
    resultado = {}
    for x in texto:
        if x == 'c' or x == 'C':
            cuentaC += 1
        elif x == ' ':
            cuentaEspacios += 1
    invertido = ''.join(reversed(texto))
    resultado['cuentaC'] = cuentaC
    resultado['cuentaEspacios'] = cuentaEspacios
    resultado['texto invertido'] = invertido
    return resultado
print(contadores(parrafos))
print('________________________________________________________________________')

#3. Definir una función que reciba una serie de parámetros indeterminados de tipo 
#clave-valor y un elemento que por defecto será 
#un numero aleatorio. La función deberá comprobar si el número está entre los 
#valores recibidos, si es así mostrará "Encotrado" y si
#no mostrará "No Encontrado".

def buscaNum(**elementos):
    casteoDict = list(elementos.values())
    if casteoDict[-1] in casteoDict[:-1]:
        print('Encontrado')
    else:
        print('No encontrado')
buscaNum(a = 1,b =3,c=2 ,d = 3)

print('________________________________________________________________________')

#4. Definir una función que reciba una lista de notas y calcule la media simple.
#Para calcular la media simple se debe realizar el sumatorio de cada una de las 
#notas y dividirlo entre en numero total de notas 
#que hay. 

def media(listaNotas):
    sumatorio = 0
    for i in listaNotas:
        sumatorio = sumatorio + i
    return sumatorio/len(listaNotas)
print(media([10,4,7,5.5,3]))
print('________________________________________________________________________')

#5. Definir una función que reciba una lista de numeros enteros y devuelva esa 
#lista ordenada, no será posible usar sort. 

#Para hacer este ejercicio he usado el algoritmo de ordenacion por burbuja.
def ordenacionBurbuja(numeros):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(numeros)-1):
            if numeros[i] > numeros[i+1]:
                numeros[i],numeros[i+1] = numeros[i+1],numeros[i]
                intercambio=True
lista = [5,2,6,8,22,1,23,21,45,0]
ordenacionBurbuja(lista)       
print(lista) 
        
