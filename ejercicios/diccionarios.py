
''' 1. Crea un diccionario con 5 parejas clave-valor. Tiene que haber:
        - Una lista.
        - Una variable de tipo float.
        - Una tupla.
        - Dos variables de tipo texto.'''

lista = list(range(0,11))
decimal = 7.5
tupla = tuple(range(0,11))
msg1 = 'mensaje 1'
msg2 = 'mensaje 2'
diccionario = {'lista':lista,'decimal':decimal,'tupla':tupla,'msg1':msg1,'msg2':msg2}

'''2. Imprime el contenido de la variable de tipo float que has creado dentro del 
diccionario.'''

for i in diccionario.values():
    if type(i)== float:
        print(i)
print('---------------------------------------')

'''3. Mediante un bucle for, imprime cada uno de los elementos de la lista que has
creado dentro del diccionario.
        Haz lo mismo con un bucle while.'''
for i in diccionario.values():
    if type(i)==list:
        for x in i:
            print(x)
print('---------------------------------------')

j =0
z =0 
casteo = list(diccionario.values())
longitudValores = len(casteo)

while j < longitudValores:
    elementoLista = casteo[j]
    if type(elementoLista) == list:
        while z < len(elementoLista):
            print(elementoLista[z])
            z +=1
    j += 1
print('--------------------------------------------------')


#'''4. Añade un nuevo elemento a la lista que has creado dentro del diccionario e 
#imprime la lista.'''

for i in diccionario.values():
    if type(i)==list:
        listaDict = list(i)
        listaDict.append('nuevo elemento')
        print(listaDict)
print('-----------------------------------------------')
'''5. Modifica el valor de una de las variables de tipo texto que has creado 
dentro del diccionario e imprime su nuevo valor por pantalla. '''

for k,v in diccionario.items():
    if k == 'msg1':
        diccionario[k] = 'mensaje nuevo'
        print(v)
print('------------------------------------------------')
#6. Imprime el último valor de la tupla que has creado dentro del diccionario.

for i in diccionario.values():
    if type(i)==tuple:
        tuplaDict = tuple(i)
        longitudTupla = len(tuplaDict)
        print(tuplaDict[longitudTupla-1])
        #para introducir el ultimo elemento pongo como parametro la longitud de la tupla y para no salirme del rango
        #le resto 1 con esto aunque se le añada nuevos elementos siempre sacará el ultimo elemento.
print('-------------------------------------------')

'''7. Mediante un bucle for imprime todas las parejas clave-valor del diccionario.
        Ejemplo de la salida esperada de una pareja de clave valor -> La clave 
'Apellido1' tiene el valor 'Carreras'.
        RESPETAD ESTE EJEMPLO.'''

for k,v in diccionario.items():
    print('La clave ' + k + ' tiene el valor ' + str(v))
print('-----------------------------------------')
'''8. Añade una nueva pareja clave-valor de tipo entero y elimina completamente la
tupla que ya existía en el diccionario.'''
#tengo que hacer una copia del diccionario ya que me si recorria el diccionario original me daba un fallo 
#de que se estaba modificando el diccionario mientras se recorria.
diccionario['enteros'] = 45
copiaDict = diccionario.copy()

for k,v in copiaDict.items():
    if type(k) == tuple:
        diccionario.pop(k)
print(diccionario)
print('-----------------------------------------------')

'''9. Crea una copia del diccionario y modifica el valor de 2 parejas clave-valor.
Imprime el nuevo diccionario y el original.'''
#la copia del diccionario la tengo hecha en el ejercicio anterior.
copiaDict2 = diccionario.copy()
for k,v in copiaDict2.items():
    if k == 'decimal' :
        copiaDict2[k] = 98.3
    if k == 'msg2':
        copiaDict2[k] = 'mensaje ejercicio 9'
print(copiaDict2)
print(diccionario)
print('-------------------------------------------------')
'''10. En el nuevo diccionario, añade dentro de él otro diccionario con al menos 2
parejas clave-valor.
        Imprime por pantalla el diccionario que tiene otro diccionario dentro, 
mediante un bucle for.'''


newDict = {'nombre':'Pablo','Apellidos':'Martin'}
diccionario['newDict'] = newDict
for k,v in diccionario.items():
    if k == 'newDict':
            print(k,v)
    