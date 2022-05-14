import random
'''1. (1,5 punto) Crear la clase Personaje con los siguientes atributos: 

- ID: int.

- Nombre: texto.

- Peso: float.

- Edad: int.

- Tipo: texto.

- Ataque: int.

- Defensa: int.

 

Deberá tener los siguientes métodos: 

- Constructor: recibirá todos los datos menos el ID que se generará llamando al método CrearID.

- CrearID: no recibirá nada y devolverá un ID generado con el siguiente patrón: tipo, guion medio, dos iniciales

del nombre, guion medio y un numero aleatorio del 1 al 100. 

- ModificarAtaque: recibirá un numero y aumentará o disminuirá el ataque del personaje. El ataque no puede pasar de 10 ni bajar de 0. 

- ModificarDefensa: recibirá un numero y aumentará o disminuirá la defensa del personaje. La defensa no puede pasar de 10 ni bajar de 0.

- Método adecuado para mostrar su información. '''
class personaje:
    def __init__(self,nombre,peso,edad,tipo,ataque, defensa):
        self.dni = None
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa
    def crearID(self):
        numRandom = random.randint(1,101)
        return self.tipo+'-'+self.nombre[:2]+'-'+ str(numRandom)
    def modificarAtaque(self,num):
        if self.ataque + num > 10:
            self.ataque = 10
        elif self.ataque + num < 0:
            self.ataque = 0
        else:
            self.ataque = self.ataque + num
        
    def modificarDefensa(self,num):
        if self.defensa + num > 10:
            self.defensa = 10
        elif self.defensa + num < 0:
            self.defensa = 0
        else:
            self.defensa = self.defensa + num
    def __str__(self): #da info del objeto a mi gusto
        datos="datos del personaje con ID "+self.crearID() +" y con nombre: "+self.nombre+":"
        datos += "\n -- peso: "+str(self.peso)
        datos += "\n -- edad: "+str(self.edad)
        datos += "\n -- tipo: "+self.tipo
        datos += "\n -- ataque: "+str(self.ataque)
        datos += "\n -- defensa: "+str(self.defensa)
        return datos  
    
pj = personaje('pikachu',19.5,40,'electrico',6,3)
pj2 = personaje('raichu',67.2,32,'electrico',9,6)
pj3 = personaje('charmander',23.4,12,'fuego',4,3)
print(pj)
print('------------------------------------------------------------')

'''2. (2 puntos) Crear la clase Equipo con los siguientes atributos:

- Nombre: texto. 

- ListaPersonajes: list de objetos tipo Personaje.

 

Además del método constructor donde recibirá el nombre y la lista de personajes (al menos 3), deberá implementar los siguientes métodos:

- AddPersonaje: recibirá un objeto de tipo personaje y deberá añadirlo a la lista del equipo si no existe ya. Deberá buscar si el Nombre está en la lista.

- DelPersonaje: recibirá el nombre de un personaje y deberá eliminarlo de la lista si existe. 

- Entrenamiento: no recibirá nada y aumentará en 2 el ataque de todos los personajes del equipo, 

pero disminuirá en 1 la defensa de todos.  

- Método adecuado para mostrar la información del equipo. '''

class equipo:
    def __init__(self,nombreEquipo,listaPersonajes):
        self.nombre = nombreEquipo
        self.listaPersonajes = listaPersonajes
    def addPersonaje(self,personajes):
        encontrado = False
        for i in self.listaPersonajes:
            if personajes.nombre != i.nombre:
                encontrado = True
        if encontrado == True:
            print('aaa')
            self.listaPersonajes.append(personajes)
    def delPersonaje(self,personajes):
        encontrado = False
        for i in self.listaPersonajes:
            if personajes.nombre == i.nombre:
                encontrado = True
        if encontrado == True:
            print('bbb')
            self.listaPersonajes.remove(i)
#las operativas de los metodos addPersonaje y delPersonaje deberian estar bien segun lo que me dijiste en clase
#durante el examen, asi que te lo comento por aqui.
    def entrenamiento(self):
        for i in self.listaPersonajes:
            i.modificarAtaque(2) 
            i.modificarDefensa(-1) 
        
    def __str__(self): #da info del objeto a mi gusto
       
        datos = ''
        for i in self.listaPersonajes:
            datos += str(i) + '\n' 
        return datos
        
team = equipo('pokemon',[pj,pj2,pj3])

pj4 = personaje('bulbasur',34,7,'planta',5,2)
team.addPersonaje(pj4)
team.delPersonaje(pj)
team.entrenamiento()
print(team)


class combate:
    def __init__(self, id,equipo1,equipo2):
        self.id = id
        self.equipo1 = equipo1
        self.equipo2 = equipo2
    