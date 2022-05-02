class Mueble:
    def __init__(self,ref,desc,stock):
        self.altura = 0.0
        self.peso = 0.0
        self.ancho = 0.0
        self.ref = ref
        self.desc = desc
        self.stock = stock
    def cambiaStock(self, numStock):
        if numStock < 0:
            if numStock > (self.stock)*-1:
                raise Exception ('Error, no hay stock')
        self.stock += numStock
class muebleBaño(Mueble):
    def __init__(self, ref,desc,stock,alt,anchos,pesos,restHumedad):
        super().__init__(ref,desc,stock)
        self.altura = alt
        self.ancho = anchos
        self.peso = pesos
        self.restHumedad = restHumedad
    
        