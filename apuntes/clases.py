from logging import raiseExceptions
import random


class saludo:
    def __init__(self,nombre):
        
        self.texto = 'hola'
        self.nombre = nombre

    def saludar(self):
        print(self.texto + ' ' + self.nombre + '!!!')
    def setNombre(self,newNombre):
        self.nombre = newNombre
    def despedirse(self):
        print('Adios '+ self.nombre)
    
p1 = saludo('Clase')
p1.setNombre('Esteban')
'''p1.saludar()
print(dir(p1))'''


#EJERCICIOS
class calculadora:
    def __init__(self):
        self.op1 = 0
        self.op2 = 0
        self.__cod_op = random.randint(0,1000)
    def __suma(self,op1,op2):
        return str(op1 +op2) + ':'+str(self.__cod_op)
    def operar(self,op1,op2,op3):
        self.__cod_op = random.randint(0,1000)
        if op3 == '+':
            return self.__suma(op1,op2)
        else:
            raiseExceptions('error')
class1 = calculadora()
#print(class1.__suma(3,4))
#print(p1.__cod_op)


class ejemploClase:
    def __init__(self):
        self.num = 0
        self.lista = None
    def recibeNum(self):
        while True:
            try:
                self.my_input = int(input('Introduce un número: '))
                break
            except:
                print('Introduce un numero')
    def existeNum(self,listaNum):
        if self.my_input in listaNum:
            return True
        return False
    def addNum(self,*listaNum):
        self.lista = list(listaNum)
        if not self.existeNum(self.lista):
            self.lista.append(self.my_input)
        return self.lista
    
        
check = ejemploClase()
check.recibeNum()
#print(check.existeNum([1,2,3,7,8,6,6,44])) 
print(check.addNum((1,2,3,7,8,6,6,44)))


