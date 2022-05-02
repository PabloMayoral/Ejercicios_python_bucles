'''class persona:
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellidos = apellido
    def imprimirNombre(self):
        print(self.nombre + ' '+self.apellidos)
pintaNom = persona('Pablo','Mayoral')
pintaNom.imprimirNombre()

class alumno(persona):
   def __init__(self,nombre,apellido):
       super().__init__(nombre,apellido)
pintaAlumn = alumno('Pablo','Mayoral')
pintaAlumn.imprimirNombre()'''


'''class Padre1:
    def Imprimir1(self):
        print('Padre1 llamado')
class Padre2:
    def Imprimir2(self):
        print('Padre2 llamado')
class hija(Padre1,Padre2):
    def imprimir(self):
        self.Imprimir1()
        Padre2().Imprimir2()
    def Imprimir1(self):
        print('Metodo imprimir1 sobreescrito')
    def Imprimir2(self):
        print('Metodo imprimir2 sobreescrito')
llama = hija()
llama.imprimir()
llama.Imprimir1()'''

class padre1:
    def __init__(self,texto):
        self.texto = texto
    def imprimirTexto(self):
        print('El mensaje recibido es: ' + self.texto)
class hija(padre1):
    def __init__(self,texto,caracter):
        super().__init__(texto)
        self.caracter = caracter
    def devolver(self):
        return self.texto.count(self.caracter)
        
c1 = padre1('Crea una clase en python llamada ManipuladoraTexto cuyo objetivo es contener varias funciones para manipular cadenas de texto.')
#c1.imprimirTexto()

h1 = hija('Crea una clase en python llamada ManipuladoraTexto cuyo objetivo es contener varias funciones para manipular cadenas de texto.','a')
h1.imprimirTexto()
#print(h1.devolver())


'''a =1 
print(isinstance(a,int))
b ='hola' 
print(isinstance(b,str))
obj1 = persona('Pablo','Martin')
print(isinstance(obj1, persona))
obj2 = alumno('Pablo','Martin')
print(isinstance(obj2, persona))
'''
class Vehiculo:
    def _init_(self):
        self.peso=0
        self.largo=0
        self.ancho=0
    
    def GetPeso(self):
        return self.peso
    def GetLargo(self):
        return self.largo
    def GetAncho(self):
        return self.ancho
    print("-------------------------------------------------")

#es una clase coche heredada de vehículo, ya puedo poner argumentos
class Coche(Vehiculo):
    #constructor
    def _init_(self,peso,largo,ancho,marca,modelo):
        super()._init_()
        #inicialición de datos
        self.SetPeso(peso)
        self.SetLargo(largo)
        self.SetAncho(ancho)
        self.marca=marca
        self.modelo=modelo
#metodos 
    def SetPeso(self, peso):
        self.peso=peso
    def SetLargo(self,largo):
        self.largo=largo
    def SetAncho(self,ancho):
        self.ancho=ancho
    def GetPeso(self):
        return (str(self.peso)+"kg")
    def GetLargo(self):
        return (str(self.largo)+"metros")
    def GetAncho(self):
        return (str(self.ancho)+"metros")
    def _str_(self): #da info del objeto a mi gusto
        datos="datos del "+self.marca +" "+self.modelo+":"
        datos += "\n -- peso: "+self.GetPeso()
        datos += "\n -- largo: "+self.GetLargo()
        datos += "\n -- ancho: "+self.GetAncho()
        return datos 
coche=Coche(1200,3.20,1.50,"ferrari","california") #nivel de abstracción.
print(coche)

#   NO se puede hacer overload en python
