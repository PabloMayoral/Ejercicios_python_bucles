#Apuntesd e los ejercicios de los diccionarios
diccionario ={'Fecha nacimiento': '14/04/1990', 'nombre':'Pedro','Apellidos':'Gonzalez','color de pelo':'castaño','color de ojos':'verdes','DIN':'51320584C','Peso':65}

#metodo para modificar un valor de una clave, si la clave especificada no existe creara una nueva clave en el diccionario
#y ppondrá como valor el texto o valor especificado en la linea de codigo.
#Al no ser ordenado no existe la posibilidad de elegir la posicion de la nueva clave/valor
diccionario['Peso'] += 0.5  
print(diccionario['Peso'])
#metodo para sacar unicamente las claves del diccionario
for k in diccionario.keys():
    print(k)
#metodo para sacar unicamente los valores de un diccionario
for v in diccionario.values():
    print(v)
#metodo para sacar las claves y sus respectivos valores de un diccionario
for key,value in diccionario.items():
    #para sacar en la cadena de texto los valores enteros casteamos la variable de los valores
    print(key+': '+str(value))
#para borrar claves o valores se usa el .pop())(elimina el elemento especificado) o el .popitem()(elimina el utimo elemento)
#para borrar todo el diccionario se usa el .del() o el .clear() (remondedado para borrar un elemento el .pop())

#variable para copiar una lista:
diccionario2 = diccionario.copy()


