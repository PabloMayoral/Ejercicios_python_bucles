import random
import time
import os


class dados:
    def __init__(self):
        self.dado = [1,2,3,4,5,6]
    def tiraDado(self):
        numAzar = random.randint(0,5)
        numDado= self.dado[numAzar]
        return numDado
class funcionamiento(dados):
    def __init__(self):
        super().__init__()
        self.acumulaResultados = []
        self.partidaTerminadaUser = True
    def tiraDados(self):
        i=1
        while i < len(self.dado):
            self.acumulaResultados.append(self.tiraDado())
            i+=1
        return self.acumulaResultados
class usuario(funcionamiento,dados):
    def __init__(self):
        super().__init__()
        self.registroPartidaUser = {}
        self.puntosUser = 0
        
    def juegaRondaUser(self):
        aux = 1
        n = 5
        for x in range(0,10):
            listadoUser = self.tiraDados()
        output = [listadoUser[i:i + n ] for i in range(0, len(listadoUser),n)]
        for j in output:
            self.registroPartidaUser['ronda ' + str(aux)]=j
            aux += 1
        return self.registroPartidaUser
    def NumCountUser(self):
        copiaDict = self.registroPartidaUser
        acumulaListaCopia = []
        z = 1
        i =0
        if self.partidaTerminadaUser == False:
            for v in copiaDict.values():
                acumulaListaCopia.append(v)
                while i < len(acumulaListaCopia):
                    for j in self.dado:
                        puntuacion = acumulaListaCopia[i].count(j)
                        if puntuacion == 3:
                            self.puntosUser += 3
                        elif puntuacion == 4:
                            self.puntosUser += 5
                        elif puntuacion == 5:
                            self.puntosUser += 10
                        elif acumulaListaCopia[i] == [1,2,3,4,5] or acumulaListaCopia[i] == [2,3,4,5,6]:
                            self.puntosUser += 5
                    i += 1
                print('Estos son los números que sacaste en la ronda nº '+ str(z) )
                print(v)
                print('Puntos: '+str(self.puntosUser))
                time.sleep(5)
                clear = lambda: os.system('cls')
                clear()
                z +=1       
class maquina(funcionamiento,dados):
    def __init__(self):
        super().__init__()
        self.registroPartidaIA = {}
        self.puntosIA = 0
    def juegarondaIA(self):
        aux = 1
        n = 5
        self.acumulaResultados = []
        for x in range(0,10):
            listado = self.tiraDados()
        output2 = [listado[i:i + n ] for i in range(0, len(listado),n)]
        print(output2)
        for j in output2:
            self.registroPartidaIA['ronda ' + str(aux)]=j
            aux += 1
        return self.registroPartidaIA
    def NumCountIA(self):
        copiaDictIA = self.registroPartidaIA
        acumulaListaCopiaIA = []
        s = 1
        i =0
        
        for r in copiaDictIA.values():
            acumulaListaCopiaIA.append(r)
            while i < len(acumulaListaCopiaIA):
                for j in self.dado:
                    puntuacion = acumulaListaCopiaIA[i].count(j)
                    if puntuacion == 3:
                        self.puntosIA += 3
                    elif puntuacion == 4:
                        self.puntosIA += 5
                    elif puntuacion == 5:
                        self.puntosIA += 10
                    elif acumulaListaCopiaIA[i] == [1,2,3,4,5] or acumulaListaCopiaIA[i] == [2,3,4,5,6]:
                        self.puntosIA += 5
                i += 1
            print('Estos son los números que sacó el adversario en la ronda nº '+ str(s))
            print(r)
            print('Puntos: '+str(self.puntosIA))
            time.sleep(5)
            clear = lambda: os.system('cls')
            clear()
            s +=1
        self.partidaTerminadaUser = True
class partida(usuario,maquina,funcionamiento,dados):
    def __init__(self):
        super().__init__()
        self.x = None
    def obtenerRespuesta(self):
        self.x = input('Escribe start para comenzar a tirar dados: ')
        #self.y = input('¿Quieres jugar de nuevo? Escribe "si" o "no"')
    def comienzaPartida(self):
        self.obtenerRespuesta()
        if self.partidaTerminadaUser == True:
            if self.x == 'start':
                self.partidaTerminadaUser = False
                self.juegaRondaUser()
                print(self.NumCountUser())
                print('Ahora es el turno del adversario...')
                self.juegarondaIA()
                print(self.NumCountIA())
                if self.puntosUser > self.puntosIA:
                    print('Ganaste!!!!')
                elif self.puntosUser < self.puntosIA:
                    print('Perdiste!!!')
                elif self.puntosUser == self.puntosIA:
                    print('Empate!!!!')
            self.y = input('¿Quieres jugar de nuevo? Escribe "si" o "no": ')
            if self.y == 'si':
                self.partidaTerminadaUser = True
                self.comienzaPartida()
            else:
                print('Gracias por jugar')
game = partida()
game.comienzaPartida()




