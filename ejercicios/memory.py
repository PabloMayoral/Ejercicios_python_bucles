import os
import random
import time
#1º parte, crear la lista de numeros randoms para cada ronda
listaNumerosRandoms = []
w = 10
j = 100
for i in range(0,7):
    numeroAleatorio = random.randint(w,j)
    listaNumerosRandoms.append(numeroAleatorio) 
    w *= 10
    j *= 10  


#2º parte, declarar booleans para cada fase

fase1 = True
fase2 = fase3 = fase4 = fase5 = fase6 = fase7 = False

partidaTerminada = False
contador = 0
def juega():
    fase1 = True
    contador =0
    vidas = 2
    if fase1 == True:
        print('Te encuentras en la primera fase del juego!')
        print('Recuerda el siguiente número que aparecerá en pantalla!: '+str(listaNumerosRandoms[0]))
        time.sleep(7)
        clear = lambda: os.system('cls')
        clear()
        print('Te encuentras en la primera fase del juego!')
        my_input = int(input('Introduce el número que apareció en pantalla: '))
        if my_input == listaNumerosRandoms[0]:
            contador += 1
            fase1 = False
            fase2 = True
            print('Enhorabuena, has pasado a la siguiente fase, tu puntuación es de: ' + str(contador) + ' puntos, y tu número de vidas es de: ' + str(vidas))
        else: 
            vidas -= 1
            print('Incorrecto!! Has fallado!, no sumas puntuacion y tus vidas son: ' + str(vidas))
            
    if fase2 == True:
        print('Te encuentras en la segunda fase del juego!')
        print('Recuerda el siguiente número que aparecerá en pantalla!: '+str(listaNumerosRandoms[1]))
        time.sleep(7)
        clear = lambda: os.system('cls')
        clear()
        print('Te encuentras en la segunda fase del juego!')
        my_input = int(input('Introduce el número que apareció en pantalla: '))
        if my_input == listaNumerosRandoms[1]:
            contador += 1
            fase2 = False
            fase3 = True
            print('Enhorabuena, has pasado a la siguiente fase, tu puntuación es de: ' + str(contador) + ' puntos, y tu número de vidas es de: ' + str(vidas))
        else: 
            vidas -= 1
            print('Incorrecto!! Has fallado!, no sumas puntuacion y tus vidas son: ' + str(vidas))
            if vidas == 0:
                partidaTerminada = True
    if fase3 == True:
        print('Te encuentras en la tercera fase del juego!')
        print('Recuerda el siguiente número que aparecerá en pantalla!: '+str(listaNumerosRandoms[2]))
        time.sleep(7)
        clear = lambda: os.system('cls')
        clear()
        print('Te encuentras en la tercera fase del juego!')
        my_input = int(input('Introduce el número que apareció en pantalla: '))
        if my_input == listaNumerosRandoms[2]:
            contador += 1
            fase3 = False
            fase4 = True
            print('Enhorabuena, has pasado a la siguiente fase, tu puntuación es de: ' + str(contador) + ' puntos, y tu número de vidas es de: ' + str(vidas))
        else: 
            vidas -= 1
            print('Incorrecto!! Has fallado!, no sumas puntuacion y tus vidas son: ' + str(vidas))
            if vidas == 0:
                partidaTerminada = True
    if fase4 == True:
        print('Te encuentras en la cuarta fase del juego!')
        print('Recuerda el siguiente número que aparecerá en pantalla!: '+str(listaNumerosRandoms[3]))
        time.sleep(7)
        clear = lambda: os.system('cls')
        clear()
        print('Te encuentras en la cuarta fase del juego!')
        my_input = int(input('Introduce el número que apareció en pantalla: '))
        if my_input == listaNumerosRandoms[3]:
            contador += 1
            fase4 = False
            fase5 = True
            print('Enhorabuena, has pasado a la siguiente fase, tu puntuación es de: ' + str(contador) + ' puntos, y tu número de vidas es de: ' + str(vidas))
        else: 
            vidas -= 1
            print('Incorrecto!! Has fallado!, no sumas puntuacion y tus vidas son: ' + str(vidas))
            if vidas == 0:
                partidaTerminada = True
    if fase5 == True:
        print('Te encuentras en la quinta fase del juego!')
        print('Recuerda el siguiente número que aparecerá en pantalla!: '+str(listaNumerosRandoms[4]))
        time.sleep(7)
        clear = lambda: os.system('cls')
        clear()
        print('Te encuentras en la quinta fase del juego!')
        my_input = int(input('Introduce el número que apareció en pantalla: '))
        if my_input == listaNumerosRandoms[4]:
            contador += 1
            fase5 = False
            fase6 = True
            print('Enhorabuena, has pasado a la siguiente fase, tu puntuación es de: ' + str(contador) + ' puntos, y tu número de vidas es de: ' + str(vidas))
        else: 
            vidas -= 1
            print('Incorrecto!! Has fallado!, no sumas puntuacion y tus vidas son: ' + str(vidas))
            if vidas == 0:
                partidaTerminada = True
    if fase6 == True:
        print('Te encuentras en la sexta fase del juego!')
        print('Recuerda el siguiente número que aparecerá en pantalla!: '+str(listaNumerosRandoms[5]))
        time.sleep(7)
        clear = lambda: os.system('cls')
        clear()
        print('Te encuentras en la sexta fase del juego!')
        my_input = int(input('Introduce el número que apareció en pantalla: '))
        if my_input == listaNumerosRandoms[5]:
            contador += 1
            fase6 = False
            fase7 = True
            print('Enhorabuena, has pasado a la siguiente fase, tu puntuación es de: ' + str(contador) + ' puntos, y tu número de vidas es de: ' + str(vidas))
        else: 
            vidas -= 1
            print('Incorrecto!! Has fallado!, no sumas puntuacion y tus vidas son: ' + str(vidas))
            if vidas == 0:
                partidaTerminada = True
    if fase7 == True:
        print('Te encuentras en la última fase del juego!')
        print('Recuerda el siguiente número que aparecerá en pantalla!: '+str(listaNumerosRandoms[6]))
        time.sleep(7)
        clear = lambda: os.system('cls')
        clear()
        print('Te encuentras en la última fase del juego!')
        my_input = int(input('Introduce el número que apareció en pantalla: '))
        if my_input == listaNumerosRandoms[6]:
            contador += 1
            fase7 = False
            partidaTerminada = True
            print('Enhorabuena, has pasado a la siguiente fase, tu puntuación es de: ' + str(contador) + ' puntos, y tu número de vidas es de: ' + str(vidas))
        else: 
            vidas -= 1
            print('Incorrecto!! Has fallado!, no sumas puntuacion y tus vidas son: ' + str(vidas))
            if vidas == 0:
                partidaTerminada = True
juega()

