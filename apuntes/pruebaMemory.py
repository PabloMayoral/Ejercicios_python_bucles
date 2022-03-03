import os
import random
import time
#Empiezo creando una vqariable tipo lista donde voy a almacenar todos los numeros random que se vayan generando
listaNumerosRandoms = []
#declaro dos variables tipo int para marcar el rango de los números aleatorios
w = 10
j = 100
#hago un bucle for con tantas repeticiones como rondas va a tener
for i in range(0,7):
    #declaro una variable que contendrá el numero aleatorio que se genere dentro del rango segun el valor de las variables 'w' y 'j'
    numeroAleatorio = random.randint(w,j)
    #Añado el numero aleatorio dentro de la lista con esto se añadirá a la lista 7 numeros aleatorios
    listaNumerosRandoms.append(numeroAleatorio) 
    #multiplico por 10 las dos variables para ampliar el rango y que haya un digito mas progresivamente
    w *= 10
    j *= 10  

puntuacion = 0
vidas = 2
i = 0
partidaTerminada = False
longitudNumRandom = len(listaNumerosRandoms)-1
try:    
#hago un bucle while que se repita tantas veces como elementos haya en la lista, asi en caso de añadir mas rondas el codigo no se ve afectado
#en la variable de la longitudNumRandom al len le resto 1 para que este dentro del rango
    while i < longitudNumRandom:
        fase = i+1
    #hago un if para ver si la partida esta terminada, si no esta terminada hace el bucle
        if partidaTerminada == False:
            #hago un print para que saque por consola el numero de la lista con un breve texto
            print('Recuerda el siguiente número que aparecerá en pantalla!: '+str(listaNumerosRandoms[i]))
            #uso la libreria time y os para que tras 7 segundos se borre la consola
            time.sleep(7)
            clear = lambda: os.system('cls')
            clear()
            #con el print de abajo indico en todo momento en que ronda se encuentra
            print('Te encuentras en la ' + str(fase) +'ª fase del juego!')
            #creo un input para que el usuario introduxca el numero que sale por consola
            my_input = int(input('Introduce el número que apareció en pantalla: '))
            #Si el numero que introduce el usuario es igual que el de la lista se le suma 1 la puntuacion y fase
            if my_input == listaNumerosRandoms[i]:
                puntuacion += 1
                fase = i+1
                i +=1
                #el siguiente print tiene como funcion informar de la puntuacion del usuario tras la ronda
                print('Enhorabuena, has pasado a la siguiente fase, tu puntuación es de: ' + str(puntuacion) + ' puntos, y tu número de vidas es de: ' + str(vidas))
            else:
                #Si el numero que se ha introducido es incorrecto se resta una vida y si el numero de vidas llega a cero la partida se termina
                vidas -= 1
                fase = i+1
                i +=1
                if vidas == 0:
                    partidaTerminada = True
        else:
            clear()
            #En este else debo meter un break para romper el bucle y evitar un bucle infinito de los prints de este else
            print('Te quedaste sin vidas, fin del juego...')
            print('Tu puntuación final es de: '+ str(puntuacion) + ' puntos')
            i = longitudNumRandom
            if partidaTerminada == True:
                 inputPlayAgain = input('Escribe start si quieres jugar otra vez: ')
                 if inputPlayAgain == 'start':
                     partidaTerminada == False
                     
except:
    print('error')            
            

