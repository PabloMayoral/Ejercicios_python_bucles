class animal:
    def __init__(self,tipo,patas,habitat):
        self.tipo = tipo
        self.patas = patas
        self.habitat = habitat
    def hablar(self,sonidos = None):
        return sonidos
    def getPatas(self):
        return self.patas
    def getTipo(self):
        return self.tipo
class perro(animal):
    def __init__(self,habitat,tipo,patas,tipos,numPatas=4):
        super().__init__(tipo,patas,habitat)
        self.tipo = tipos
        self.patas = numPatas
    def hablar(self,sonidos):
        return sonidos
class cat(animal):
    def __init__(self,habitat,tipo,patas,tipos,numPatas=4):
        super().__init__(tipo,patas,habitat)
        self.tipo = tipos
        self.patas = numPatas
    def hablar(self,sonidos):
        return sonidos
class elefante(animal):
    def __init__(self,habitat,tipo,patas,tipos,numPatas=4):
        super().__init__(tipo,patas,habitat)
        self.tipo = tipos
        self.patas = numPatas
    def hablar(self,sonidos):
        return sonidos
class fish(animal):
    def __init__(self,habitat,tipo,patas,tipos,numPatas=0):
        super().__init__(tipo,patas,habitat)
        self.tipo = tipos
        self.patas = numPatas
    def hablar(self,sonidos):
        return sonidos

print('-------------------------------------------------')
dogs = perro('cualquiera','mamifero',4,'mamiferos')
print(dogs.hablar('Guau'))
print(dogs.getPatas())
print(dogs.getTipo())
print('-------------------------------------------------')
gato = cat('cualquiera','mamifero',4,'mamiferos')
print(gato.getPatas())
print(gato.getTipo())
print(gato.hablar('miau miau!'))
print('-------------------------------------------------')
elefant = elefante('Selva','mamifero',4,'mamiferos')
print(elefant.getPatas())
print(elefant.getTipo())
print(elefant.hablar('*sonido que emite un elefante*'))
print('-------------------------------------------------')
pez = fish('Mar','mamifero',4,'pez')
print(pez.hablar('Glu glu'))
print(pez.getPatas())
print(pez.getTipo())