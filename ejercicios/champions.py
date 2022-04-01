import random


def enfrentamientosAleatorios():
    #se crea la lista de los equipos que pasaron a cuartos de final de la champions league y un diccionario 
    #vacio donde almacenaremos los efrentamientos
    listaEquipos = ['RMA','CHE','ATM','MNC','VIL','BAY','LIV','BEN']
    resultado = {}
    
    #para el primer emparejamiento declaro una variable que será una lista vacía y un numero random para cada 
    #seleccion alatoria de equipo para sacar un numero aleatorio diferente cada vez y que no sea el mismo todo el rato
    emparejamiento1 = []
    numeroRandom = random.randint(0,len(listaEquipos)-1)
    #añadimos un equipo dentro de la lista y lo eliminamos de la lista original para que no se repita
    emparejamiento1.append(listaEquipos[numeroRandom])
    listaEquipos.pop(numeroRandom)
    #volvemos a generar un nuevo numero random y añadimos otro equipo aleatorio dentro y lo borramos del original
    numeroRandom = random.randint(0,len(listaEquipos)-1)
    emparejamiento1.append(listaEquipos[numeroRandom])
    listaEquipos.pop(numeroRandom)
    #añado la lista de emparejamiento1 dentro del diccionario vacío y para el resto de emparejamientos se repite
    resultado['primer enfrentamiento'] = emparejamiento1

    emparejamiento2 = []
    numeroRandom = random.randint(0,len(listaEquipos)-1)
    
    emparejamiento2.append(listaEquipos[numeroRandom])
    listaEquipos.pop(numeroRandom)
    numeroRandom = random.randint(0,len(listaEquipos)-1)
    emparejamiento2.append(listaEquipos[numeroRandom])
    listaEquipos.pop(numeroRandom)
    resultado['segundo enfrentamiento'] = emparejamiento2

    emparejamiento3 = []
    numeroRandom = random.randint(0,len(listaEquipos)-1)
    emparejamiento3.append(listaEquipos[numeroRandom])
    listaEquipos.pop(numeroRandom)
    numeroRandom = random.randint(0,len(listaEquipos)-1)
    emparejamiento3.append(listaEquipos[numeroRandom])
    listaEquipos.pop(numeroRandom)
    resultado['tercer enfrentamiento'] = emparejamiento3

    resultado['cuarto enfrentamiento'] = listaEquipos
    
    print(resultado)
   


enfrentamientosAleatorios()
