import random

class respuesta:
    def __init__(self,ID,Tema,Respuesta,tipo):
        self.ID = ID
        self.Tema = Tema
        self.Respuesta = Respuesta
        self.tipo = tipo
    def cambiarTipo(self,parametro):
        longitud = len(parametro)
        if longitud == 1:
            self.tipo = 'respuesta corta'
            self.Respuesta = parametro
        elif longitud == 2:
            self.tipo = 'S/N'
            self.Respuesta = parametro
        elif longitud > 2 :
            self.tipo = 'opciones'
            self.Respuesta = parametro
    def quitarOpcion(self, opcion):
        self.Respuesta.remove(opcion)
    def aniadirOpcion(self,opcion, posicion):
        self.Respuesta.insert(opcion,posicion)
    def comprobarTipo(self):
        self.cambiarTipo(self.Respuesta)

###crear una clase pregunta con los siguientes atributos: id(int),tema(texto),puntuacion(float),pregunta(texto)
'''respuesta(objeto clase respuesta) ademas del metodo contructor donde recibira todos los datos, debera tener
'''
class Pregunta:
    def __init__(self,ID,Tema,Puntuacion,Pregunta,Respuesta):
        self.ID = int(ID)
        self.Tema = Tema
        self.Puntuacion = Puntuacion
        self.Pregunta = Pregunta
        self.Respuesta = Respuesta
    def editar(self,texto):
        self.Pregunta = texto
    def addRespuesta(self,objeto_r):
        for i in objeto_r.Respuesta:
            self.Respuesta.Respuesta.append(i)
    def updateTema(self,otro_t):
        self.Tema = otro_t
Respuesta = respuesta(12,'programacion1',['instanciar','append'],'pregunta corta')
pregunta = Pregunta(12,'programacion2',7.8,'¿que es instanciar?',Respuesta)
print(pregunta.Tema)

class examen:
    def __init__(self,ID,banco,lista,fecha):
        self.ID = ID
        self.banco = banco
        self.lista = lista
        self.fecha = fecha
    def createExam(self,d_preguntas):
        p = random.sample(d_preguntas,self.banco.values())
        for i in p:
            self.lista.append(i)
    def showExam(self,boolean):
        for i in self.lista:
            print(i.Pregunta)
            if boolean == True:
                print(i.Respuesta.Respuesta)
    def checkDificultad(self):
        for i in self.lista:
            if len(self.lista)<10:
                print('facil')
            elif len(self.lista) > 10 and pregunta.tipo == 'opciones':
                print('dificil')
            else:
                print('media')
exam = examen(12,dict(pregunta1 = pregunta),['instanciar','append'],'25/04/2022')
exam.checkDificultad()
