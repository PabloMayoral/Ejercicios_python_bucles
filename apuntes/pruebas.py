


def tipos(lista):
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
tipos([11,['a','b'],(1,2),{'nombre':'Pablo','Apellidos':'Martin'},'texto',87.2,[1,2]])