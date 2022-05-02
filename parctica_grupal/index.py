from operator import contains
import random
from colorama import init, Fore
bancoPalabras = five_letter_words = [
    'aback',
    'abase',
    'abate',
    'abaya',
    'abbey',
    'abbot',
    'abets',
    'abhor',
    'abide',
    'abled',
    'abode',
    'abort',
    'about',
    'above',
    'abuse',
    'abuts',
    'abyss',
    'ached',
    'aches',
    'acids',
    'acing',
    'ackee',
    'acorn',
    'acres',
    'acrid',
    'acted',
    'actin',
    'actor',
    'acute',
    'adage',
    'adapt',
    'added',
    'adder',
    'addle',
    'adept',
    'adieu',
    'adios',
    'adits',
    'adman',
    'admin',
    'admit',
    'adobe',
    'adobo',
    'adopt',
    'adore',
    'adorn']

palabraOculta = bancoPalabras[random.randint(0,45)]

#longitudPalabra = len(palabraOculta)
verde = False 
amarillo = False
gris = False
def compruebaLetras():
    my_input = input('Introduce una palabra de 5 letras: ')
    for i in palabraOculta:
        for j in my_input:
            if i == j:
                verde = True
                print(Fore.GREEN + i)
            if j in palabraOculta:
                amarillo = True
                print(Fore.YELLOW + i)



compruebaLetras()