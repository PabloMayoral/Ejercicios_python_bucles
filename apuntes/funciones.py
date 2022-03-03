import os


def funcion1 (a,b):
    return a+ b
print(funcion1(10,5))
     

def helloWorldFunc():
    print('Hello World Function!!')
helloWorldFunc()

def helloWorldFunc2(frase = 'Hello World Function!!' ):
    print(frase)
helloWorldFunc2('Hola Pablo')
helloWorldFunc2()

def suma (lista):
    contador = 0
    for i in lista:
        contador = contador + i
    return contador
print(suma(list(range(0,11))))

def division(dividendo,divisor):
    try:
        return dividendo/divisor
    except:
        print('No se puede dividir entre 0')
division(2,0)
clear = lambda: os.system('cls')
clear()

def texto(palabra1, palabra2 = 'hola'):
    contador = 0
    
    if palabra2 in palabra1:
        print(True)
    else:
        print(False)
    return palabra1.count(palabra2)
print(texto('hola mundo hola mundo '))
print(texto('hola mundo hola mundo mundo','mundo'))