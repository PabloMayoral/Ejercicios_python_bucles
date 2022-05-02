import random

acumulaResultados = []
puntos = 0
contadorDict = {}
def tiraDado(dado = [1,2,3,4,5,6]):
        numAzar = random.randint(0,5)
        numDado= dado[numAzar]
        return numDado
def tiraDados(dado = [1,2,3,4,5,6]):
        i=1
        while i < len(dado)+1:
            acumulaResultados.append(tiraDado())
            i+=1
        return acumulaResultados
def NumCount():
        aux = 0
        for i in acumulaResultados:
            contador = acumulaResultados.count(i)
            contadorDict[i]=contador
        return contadorDict
def deleteRepeteat():
    for k in NumCount():
        for key in NumCount():
            print()
print(tiraDado())
print(tiraDados())
print(NumCount())