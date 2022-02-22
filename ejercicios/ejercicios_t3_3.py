# 1. Crea una lista con las asiganturas que tienes este cuatrimestre (al menos 3).
#    Recorre la lista y todas las asignaturas que tengan la letra o, debes eliminarla de la lista.
#    Muetra las asignaturas resultantes por pantalla por separado. 
asignaturas = ['programación','matematicas','organizacion de empresas','Big data','introduccion estudios universitarios']
asignaturas_new = asignaturas.copy()
w = 0
for x in asignaturas_new:
    #print(x)
    if  'o' in x :
            asignaturas_new.pop(w)
            print('asignatura a borrar -> '+ str(w) + ' es: ' + x )
    w += 1

print(asignaturas_new)
print('--------------------------------------------------------')

# 2. Crea una lista con 7 numeros.  
#    Haz una copia de la lista, recorre la lista y añade la suma del numero actual 
#    y el anterior a continuación de la posición actual, si es el primer numero se suma contra 0. 
#    Ejemplo: [1,2,3,4,5,6,7,8] 
#    - Cuando estoy en el 1, debe añadir 1 + 0 a la lista --> [1,1,2,3,4,5,6,7,8]
#    - Cuando estoy en el 2, debe añadir 2 + 1 a la lisa --> [1,1,2,3,3,4,5,6,7,8]
#  Muestra por pantalla la lista resultante.
numeros = [1,2,3,4,5,6,7,8] 
copia_numeros = numeros.copy()
suma_numeros = []
for i in copia_numeros: 
    #print(i)
    suma_numeros +=i,i + (i-1)
print(suma_numeros) 
print('--------------------------------------------------------')
# 3. Crea una lista que contenga 5 nombres: 
#    - Imprime por pantalla todos los elementos menos el primero y el último. 
#    - Añade la operativa para que borre los 3 últimos.

nombres = ['Pablo','Paco','Pedro','Maria','Ramona']
print(nombres[1:4])
copia_nombre = nombres.copy()
del copia_nombre[2:]
print(copia_nombre)
print('--------------------------------------------------------')
# 5. Crea una lista con los numeros del 0 al 10. 
# Recorre la lista y genera una nueva lista que en cada posición tenga la lista de 
# la tabla de multiplicar de ese número.

list_numeros = [0,1,2,3,4,5,6,7,8,9,10]

multiplica = [[],[],[],[],[],[],[],[],[],[],[]] 
for i in list_numeros:
    multiplica[i] += [i * 0]
    multiplica[i] += [i * 1]
    multiplica[i] += [i * 2]
    multiplica[i] += [i * 3]
    multiplica[i] += [i * 4]
    multiplica[i] += [i * 5]
    multiplica[i] += [i * 6]
    multiplica[i] += [i * 7]
    multiplica[i] += [i * 8]
    multiplica[i] += [i * 9]
    multiplica[i] += [i * 10]
print(multiplica)

