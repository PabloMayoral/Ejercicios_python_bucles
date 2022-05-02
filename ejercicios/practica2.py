import random
acumulaResultados = []
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
        self.puntosIA = 0
        
    def tiraDados(self):
        i=1
        while i < len(self.dado):
            acumulaResultados.append(self.tiraDado())
            i+=1
        return acumulaResultados
    def NumCount(self):
        aux = 0
        acumulaResultados.sort()
        copia = acumulaResultados.copy()
        for i in copia:
            if acumulaResultados[aux]==acumulaResultados[aux+1]:
                copia.pop(aux)
            aux +=1
        return (copia)
class usuario(funcionamiento,dados):
    def __init__(self):
        super().__init__()
        self.registroPartidaUser = {}

    def contadores(self):
        puntosUser = 0
        for i in self.NumCount():
            if acumulaResultados.count(i) == 3:
                puntosUser += 3
            elif acumulaResultados.count(i) == 4:
                puntosUser += 6
            elif acumulaResultados.count(i) == 5:
                puntosUser += 10
            elif acumulaResultados.count(i) < 3:
                puntosUser += 0
        return puntosUser
    def juegarondaUser(self):
        aux = 1
        n = 5
        for x in range(0,10):
            listadoUser = self.tiraDados()
        output = [listadoUser[i:i + n ] for i in range(0, len(listadoUser),n)]
        for j in output:
            self.registroPartidaUser['ronda ' + str(aux)]=j
            aux += 1
        return self.registroPartidaUser
        
class maquina(funcionamiento,dados):
    def __init__(self):
        super().__init__()
        self.registroPartidaIA = {}
    def contadores(self):
        puntosIA = 0
        for i in self.NumCount():
            if acumulaResultados.count(i) == 3:
                    puntosIA += 3
            elif acumulaResultados.count(i) == 4:
                puntosIA += 4
            elif acumulaResultados.count(i) == 5:
                puntosIA += 10
            elif acumulaResultados.count(i) < 3:
                puntosIA += 0
        return puntosIA
    def juegarondaIA(self):
        aux = 1
        n = 5
        for x in range(0,10):
            listado = self.tiraDados()
        output2 = [listado[i:i + n ] for i in range(0, len(listado),n)]
        print(output2)
        for j in output2:
            self.registroPartidaIA['ronda ' + str(aux)]=j
            aux += 1
        return self.registroPartidaIA



user = usuario()
print(user.contadores())
print(user.juegarondaUser())

'''d = dados()
d.tiraDado()
pintaDados = funcionamiento()
#print(pintaDados.tiraDados())
print(pintaDados.NumCount())

ia = maquina()
print(ia.contadores())'''
'''pintadado = dados()
print(pintadado.tiraDado())'''