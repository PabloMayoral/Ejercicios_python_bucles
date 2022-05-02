import random
from colorama import init, Fore

diccionario_Palabras=["rusia","camas","intel","comer","carta"]
y=len(diccionario_Palabras)
x=random.randint(0,y-1)
palabra=diccionario_Palabras[x]
introducir=str(input("Ponga una palabra : "))
print(palabra)
print(introducir)
lista1=[]
lista2=[]
def funcionamiento():
    for x in introducir:
        lista1.append(x)
    for x in palabra:
        lista2.append(x) 
    if lista1[0]==lista2[0]:
        print(Fore.GREEN + str(lista1[0]))
    else:
        print(Fore.BLACK + lista1[0])
    if lista1[1]==lista2[1]:
        print(Fore.GREEN + str(lista1[1]))
    else:
        print(Fore.BLACK + lista1[1])
    if lista1[2]==lista2[2]:
        print(Fore.GREEN + str(lista1[2]))
    else:
        print(Fore.BLACK + lista1[2])
    if lista1[3]==lista2[3]:
        print(Fore.GREEN + str(lista1[3]))
    else:
        print(Fore.BLACK + lista1[3])
    if lista1[4]==lista2[4]:
        print(Fore.GREEN + str(lista1[4]))
    else:
        print(Fore.BLACK + lista1[4])
funcionamiento()