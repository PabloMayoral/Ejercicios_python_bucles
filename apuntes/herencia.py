class persona:
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellidos = apellido
    def imprimirNombre(self):
        print(self.nombre + ' '+self.apellidos)
pintaNom = persona('Pablo','Mayoral')
pintaNom.imprimirNombre()

class alumno(persona):
   pass
pintaAlumn = alumno('Pablo','Mayoral')
pintaAlumn.imprimirNombre()
