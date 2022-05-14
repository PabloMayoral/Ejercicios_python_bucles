lista = [2,5,3,1,5]
lista.sort()
print(lista)

def NumCount(self):
        aux = 0
        acumulaResultados.sort()
        copia = acumulaResultados.copy()
        for i in copia:
            if acumulaResultados[aux]==acumulaResultados[aux+1]:
                copia.pop(aux)
            aux +=1
        return (copia)




















'''def tipos(lista):
    copylista = lista.copy() 
    dict = {}
    resultado = 1
    for i in lista:
        for j in copylista:
            if type(i) == type(j):
               dict[type(i)] =resultado + 1
            else:
                dict[type(i)] = resultado
    print(dict)
tipos([11,['a','b'],(1,2),{'nombre':'Pablo','Apellidos':'Martin'},'texto',87.2,[1,2]])'''



'''lista = [1]
print(len(lista))
lista.insert(4,5)
print(lista)

dni = '46456575'
print(dni[-3:])'''