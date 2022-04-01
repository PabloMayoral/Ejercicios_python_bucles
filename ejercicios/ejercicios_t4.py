# 1. Crea una clase llamada CalculadoraAreas cuyo objetivo es el de calcular
# el área de las siguientes figuras geométricas:
#   - Cuadrado
#   - Rectángulo
#   - Triángulo
#   - Pentágono
#   - Circunferencia
# Cada área se calculará en una función propia. Los parámetros de entrada
# serán los datos necesarios para el cálculo.
# No te olvides del constructor.
# Haz una prueba de cada método.
class calculadoraAreas:
    def __init__(self):
        self.pi = 3.14
    def areaTriangulo(self, base,altura):
        return (base*altura)/2
    def areaCuadrado(self,lado):
        return lado^2
    def areaRectangulo(self,base,altura):
        return base * altura
    def areaCirculo(self,radio):
        return  float(radio^2) * self.pi 
    def areaPentagono(self,lados,apotema):
        return (5*lados*apotema)/2
areas = calculadoraAreas()
print(areas.areaCirculo(5))
print(areas.areaTriangulo(5,7))
print(areas.areaRectangulo(3,4))
print(areas.areaCuadrado(8))
print(areas.areaPentagono(6,4))
print('____________________________________________________________________')
# 2. Crea una clase en python llamada ManipuladoraTexto cuyo objetivo es
# contener varias funciones para manipular cadenas de texto. Los métodos que
# tiene son:
#   - AlReves: Dada una cadena, la función devuelve la misma cadena pero dada la vuelta.
#       EJ: cadena -> anedac
#   - Reemplazar: Dada una cadena y 2 letras, la función devuelve la misma cadena pero
#       cambiando todas las veces que aparece la primera letra por la segunda.
#   - QuitaBlancos: Dada una cadena, la función devuelve la misma cadena pero sin espacios 
#       en blanco.
# No te olvides del constructor.
# Haz una prueba de cada método.

class manipuladoraTexto:
    def __init__(self):
        pass
    def alReves(self,texto):
        invertido = ''.join(reversed(texto))
        return invertido
    def quitaBlancos(self,texto):
        w = 0
        casteoLista = list(texto)
        for i in casteoLista:
            if i == ' ':
                casteoLista.pop(w)
            w +=1
        texto = "".join(casteoLista)
        return texto
    def remplaza(self, letra1,letra2,texto):
        w = 0
        castLista = list(texto)
        for i in castLista:
            if i == letra1:
                castLista[w] = letra2
            w += 1
        texto = "".join(castLista)
        return texto
modText = manipuladoraTexto()
print(modText.alReves('Crea una clase en python llamada ManipuladoraTexto cuyo objetivo es contener varias funciones para manipular cadenas de texto.'))
print(modText.quitaBlancos('Crea una clase en python llamada ManipuladoraTexto cuyo objetivo es contener varias funciones para manipular cadenas de texto.'))
print(modText.remplaza('a','s','Crea una clase en python llamada ManipuladoraTexto cuyo objetivo es contener varias funciones para manipular cadenas de texto.'))
print('_________________________________________________________________________________________________')

# 3. Haz una clase en python que se llame ControladorLista.
# Esta clase tiene un constructor que recibe una lista la cual usa para
# inicializar el atributo de clase Lista.
# La función tiene las siguientes funciones:
#   Anyadir: recibe una variable como parámetro y sirve para añadir un elemento al final de la lista.
#   Anyadir: recibe 2 variables como parámetro y sirve para añadir un elemento en una posición concreta.
#   Eliminar: recibe una variable como parámetro y sirve para eliminar el valor de la lista (si es que está en la lista).

class controladorLista():
    def __init__(self,lista):
        self.lista = lista
    def anyadir(self,variable):
        self.lista.append(variable)
        return self.lista
    def anyadir(self,variable1,variable2):
        pass
    def delete(self, variable):
        j = 0
        for i in self.lista:
            if i == variable:
                self.lista.pop(j)
            j += 1
        return self.lista
modList = controladorLista(list(range(0,20)))
modList.anyadir(80)
modList.anyadir(67,'hola')
modList.delete(6)
print('_________________________________________________________________________________________________')

# 4. Haz una clase en python que se llame DireccionPostal.
# Esta clase tiene un constructor que recibe los siguientes datos:
#   - TipoVia (calle, plaza, avenida, etc.)
#   - NombreCalle
#   - Numero
#   - Puerta
#   - Piso
#   - CP
#   - Ciudad
#   - Provincia
#   Se deben implmentar métodos para cambiar cualquiera de estos datos.
#   Además se debe implementar un método que muestre la dirección postal completa con el siguiente formato:
#       TipoVia NombreCalle, Numero, Puerta, Piso
#       CP Cuidad
#       Provincia

class direccionPostal:
    def __init__(self,tipoVia,nombreCalle,numero,puerta,piso,cp,ciudad,provincia):
        self.tipoVia = tipoVia
        self.nombreCalle = nombreCalle
        self.numero = numero
        self.puerta = puerta
        self.piso = piso
        self.cp = cp
        self.ciudad = ciudad
        self.provincia = provincia
    def cambiaDatos(self):
        pass