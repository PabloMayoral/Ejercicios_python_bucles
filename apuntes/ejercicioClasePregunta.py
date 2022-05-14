# Hecho por Mario del Olmo

# 1. Crear la clase Respuesta, con los siguientes atributos:
#     - ID: int
#     - Tema: texto.
#     - Respuesta: lista
#     - Tipo: texto

# Además del método constructor donde recibirá todos los datos, deberá tener los siguientes métodos:
#     - CambiarTipo: recibirá una estructura avanzada, dependiendo del tamaño hará las siguientes acciones:
#         - Si sólo tiene un elemento, le pondrá como tipo "respuesta corta" y en el atributo Respuesta sólo tendrá ese elemento.
#         - Si sólo tiene dos elementos, le pondrá como tipo "S/N" y en el atributo Respuesta tendrá dos elementos, SI y NO.
#         - Si tiene más de dos elementos, le pondrá como tipo "opciones", el atributo Respuesta tendrá tantos elementos como opciones reciba.
#     - QuitarOpcion: recibirá la opción que se desea eliminar y la eliminará de la respuesta.
#     - AñadirOpcion: recibirá la opción que se desea añadir y la posición y la añadirá en la respuesta.
#     - ComprobarTipo: mirará si el tipo concuerda con las respuestas que tiene, siguiendo las especificaciones mostradas en el método CambiarTipo.

class Respuesta:
    def __init__(self, ID, tema, respuesta, tipo):
        self.ID = int(ID) # Identifica el número de pregunta
        self.tema = str(tema) # Define cual es la temática de la respuesta
        self.respuesta = list(respuesta) # Esto es una lista por que la respuesta puede ser un solo item o varios, por eso el método de CambiarTipo
        self.tipo = str(tipo) # El tipo se define con el método CambiarTipo de esta clase en funcion del número de items tenga la lista de respuesta
    
    def CambiarTipo(self, elemento): # Esto identifica que tipo será la pregunta # !! CAMBIAR LO DE ESTRUCUTAAVANZADA QUE NO SE QUE ES
        self.elemento = elemento # Hago esto por si luego tengo que trabajar con esta variable fuera de este método
        if len(elemento) == 1: # Respuesta tiene una sola opcion, es decir, una palabra como en el examen de BigData
            self.tipo = "respuesta corta" 
            self.respuesta = elemento
        if len(elemento) == 2: # Respuesta tiene dos opciones, es decir, Sí o No
            self.tipo = "S/N"
            self.respuesta = ["SÍ", "NO"]
        if len(elemento) > 2: # Respuesta son varias opciones, es decir, un TEST
            self.tipo = "opciones"
            self.respuesta = elemento
       
    def QuitarOpcion(self, opcion):
        self.opcion = opcion
        self.respuesta.remove(self.opcion)

    def AñadirOpcion(self, posicion, opcion):
        self.posicion, self.opcion = posicion, opcion
        self.respuesta.insert(posicion -1 , opcion) # El -1 es por que el índice de la lista empieza en 0 y si no sería la opcion que queremos más uno.

    def ComprobarTipo(self):
        if len(self.respuesta) == 1 and self.tipo == "respuesta corta":
            print ("Se ha comprobado el tipo y concuerda con el número de respuestas. El tipo es respuesta corta")
        if len(self.respuesta) == 2 and self.tipo == "S/N":
            print ("Se ha comprobado el tipo y concuerda con el número de respuestas. El tipo es S/N")
        if len(self.respuesta) > 2 and self.tipo == "opciones":
            print ("Se ha comprobado el tipo y concuerda con el número de respuestas. El tipo es opciones")
        else:
            print ("Se ha comprobado el tipo y se ha encontrado un error. El número de respuestas es", self.respuesta, "y el tipo es:", self.tipo)

    def GetID(self): # Permite saber un argumento si se le llama desde fuera de la funcion
        return "El ID de la respuesta es:", self.ID

    def GetTema(self):
        return "El tema de la respuesta es:", self.tema

    def GetRespuesta(self):
        return "Las respuestas son:", self.respuesta

    def GetTipo(self):
        return "El tipo de la respuesta es:", self.tipo
    

p1 = Respuesta(1, "Biología", "Retículo endoplasmático LI", "opciones") # ID, tema, respuestas, tipo
p1.CambiarTipo(["Núcleo", "Mitocondría", "Plasma", "Cloroplastos", "Ninguna de las anteriores"]) # Estas son las respuestas de la pregunta en una lista
p1.QuitarOpcion("Mitocondría") # Quiero quitar la opcion de la Mitocondría
p1.AñadirOpcion(2, "Retículo endoplasmático RU") # Quiero añadir Retículo endoplasmático RU como la segunda opcion
p1.ComprobarTipo()

print (p1.GetID()) # Devuelve lo que le hemos pedido en el return del método
print (p1.GetTema())
print (p1.GetRespuesta())
print (p1.GetTipo())

'''
Lo que ha pasado aquí es que al principio teníamos estas respuestas: ["Núcleo", "Mitocondría", "Plasma", "Cloroplastos", "Ninguna de las anteriores"]
Pero con el método QuitarOpcion hemos eliminado la opcion de Mitocondría
Luego en el método AñadirOpcion hemos agregado como segunda opcion el Retículo Endoplasmático RU
Hemos comprobado que el tipo de la respuestas sea opciones sabiendo el número de respuestas que hay.

Finalmente hemos impreso cada atributo con un GetAtributo
'''


# El ejercicio continúa, pero esto es de momento la clase Pregunta que he comprobado que funciona bien