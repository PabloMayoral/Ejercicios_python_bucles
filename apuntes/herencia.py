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
pintaAlumn.imprimirNombre()
'''

class Padre1:
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
llama.Imprimir1()
