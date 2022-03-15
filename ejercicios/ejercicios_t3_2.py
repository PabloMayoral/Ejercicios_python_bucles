# 1. Crea una lista con las asiganturas que tienes este cuatrimestre (al menos 3).
#    Muestra por pantalla las asignaturas que están en índices impares. 
#  Muestra todas las asignaturas menos las dos primeras. 

#declaro las variables de la arraylist de las asignaturas, la longitud de la arraylist
asignaturas = ['programación','matematicas','organizacion de empresas','fuentes de datos','introduccion estudios universitarios']
longitud = len(asignaturas)
x = 0
#creo un bucle while que se recoorra con la condición de que se repita hasta llegar al final de la extension de
#de la arraylist, dentro del bucle while introduzco un if para especificar que si el resto es = 0 sabremos que 
#el indice del elemento será par e incremento la i para continuar el bucle.
while x < longitud:
    if x % 2 == 1:
        print(asignaturas[x]) 
    x += 1
print('------------------------------------')
#Inicializo una nueva variable de control para que no se cree conflicto con el bucle anterior y a la condicion le
#le resto a la longitud lo necesario para que no muestre los 2 últimos elementos
j = 0
for  j in range(2,longitud) :
    print(asignaturas[j]) 
    j += 1

print('------------------------------------')

# 2. Crea una tupla con al menos 5 elementos. 
#   Muestra por pantalla el tamaño de la lista. 
#  Muestra por pantalla cada uno de los valores

#creo la variable de la tupla, ademas del tamaño de esta usando el len() y la muestro por consola
tuplas = ('elemento 1','elemento 2','elemento 3','elemento 4','elemento 5')

tamaño_tupla = len(tuplas)
p=0
while p < tamaño_tupla:
        print(tuplas[p])
        p += 1

print('------------------------------------')
# 3. Crea una lista que contenga: 
#    - Una tupla de cadenas de texto (al menos 3).
#    - Una lista de numeros decimales (al menos 3).
#    - Un boleano. 
#    - Dos cadenas de texto. 
#  Imprime por pantalla los elementos de la tupla y de la lista por separado y 
#con el siguiente formato para la tupla:
#     "Elemento numero 1: Pedro"
#     "Elemento numero 2: Paco"
#    Para la lista deberá mostrar:
#      "Nota del alumno 0: 5.6"
#      "Nota del alumno 1: 1.5"
#    Ademas debe mostrar un texto indicando de que es cada tipo de la lista 

#creo diferentes variables para luego juntarlas todas en una sola
#para que quede todo mucho más ordenado
cadena_tupla = ('Pedro','Ramón','Pablo')
cadena_lista = ['9.5','5.2','7.3']
cadena_booleana = True
msg1 = 'mensaje 1'
msg2 = 'mensaje 2'
arrayList = [cadena_tupla,cadena_lista,cadena_booleana,msg1,msg2]


#creo un bucle for que recorra la lista, dentro le pongo un if que tenga la condicion de si el elemento que esta 
#recorriendo es de tipo tupla realice un bucle for que recorra esa tupla y muestre su contenido, esto lo haré 2 veces
#ya que tambien me piden mostrar el elemento que sea una lista y recorrerlo por dentro, además añado una variable llamada 'w'
#que funcionará como un contador.
for i in arrayList:
    w = 1
    
    if type(i) == tuple:
        for y in i:
            print('Elemento numero '+str(w)+': '+y)
            w += 1
            print(type(i))
    
    if type(i) == list:
            for x in i:
                print('Nota del alumno '+str(w)+': '+x)
                w += 1
                print(type(i))
    
print('------------------------------------')

# 4. Crea una lista con juegos (al menos 4). 
#    Imprime el contenido de la lista con los distintos tipos de bucles que hemos
#    visto (cada juego en una línea).

juegos = ['Fifa 2022','Minecraft','League of Legends','Dark Souls III']
listLength = len(juegos)
s=0

while s < listLength:
       
   print('el juego nº '+ str(s+1) +' es: '+ juegos[s])
   s += 1
print('------------------------------------')
j=0  
for j in range(listLength):
   print('el juego nº '+ str(j+1) +' es: '+ juegos[j])
print('------------------------------------')

# 5. Crea un bucle for que vaya desde 5 a 51 y que imprima si el numero es 
# divisible entre 2 o si lo es entre 5, 
# en caso contrario indicará que no es divisible entre 2 ni 5.

#creo un bucle for y le especifico el rango que debe repetirse, me debe mostrar del 5 al 51, si especifico un in range(5,51)
#no me mostrará el 51 por lo que el rango deberá ser range(5,52)
#dentro del bucle uso el metodo usado en el primer ejercicio que es el modulo (%) para saber si es divisible o no entre 2 o 5


for i in range(5,52):
    if i % 2 == 0 or i % 5 == 0:
        print('El número '+ str(i) +' es divisible entre 2 o 5')
    else:
        print('El número ' + str(i) + ' no es divisible entre 2 o 5')

print('------------------------------------')

# 6. Crea una variable de tipo cadena con el texto 
#  "El episodio piloto se estrenó en más de 6 servicios en línea de video bajo demanda el 27 de mayo de 2015. 
#  La temporada 1 se estrenó en USA Network el 24 de junio de 2015 y la segunda temporada el 13 de julio de 2016. 
#  La tercera temporada, de 10 episodios, se estrenó el 11 de octubre de 2017. 
#  En diciembre de 2017 se renovó la cuarta y última temporada de la serie, que fue estrenada el 6 de octubre de 2019."
#  
#  Muestra por pantalla cuantos números aparecen en el texto. 
#  Muestra por pantalla cuantas aes aparecen en el texto.
#  Muestra por pantalla el numero total de letras que hay en el texto. 
 
#creo la variable mensaje que contendrá el string con el que vamos a trabajar, para evitarnos añadir más condiciones en el if
#usaré el metodo .lower() para que el texto esté todo en minusculas
#creo 3 tipos de contadores, uno para las aes, otro para los numeros y otro para los espacios en blanco y signos de puntuación
#creo un bucle for que me recorra el string y dentro especifico las condiciones con un 3 if, cada uno fuera del otro
# por ultimo en los print indico que se muestre los contadores y en el ultimo print al querer contar las letras
# cogeremos la extension del string y le restare la cantidad de nuemros y la cantidad de espacios en blanco y signos de puntuación. 
mensaje = 'El episodio piloto se estrenó en más de 6 servicios en línea de video bajo demanda el 27 de mayo de 2015. La temporada 1 se estrenó en USA Network el 24 de junio de 2015 y la segunda temporada el 13 de julio de 2016. La tercera temporada, de 10 episodios, se estrenó el 11 de octubre de 2017. En diciembre de 2017 se renovó la cuarta y última temporada de la serie, que fue estrenada el 6 de octubre de 2019.'
mensajeMinusculas = mensaje.lower()

longitudMensaje = len(mensaje)
cuentaNumeros = 0
contadorDeAes = 0
cuentaEspaciosVacios= 0
for i in mensajeMinusculas:
    if i == 'a' or i == 'á':
         contadorDeAes += 1
    if i == '0' or i =='1' or i =='2' or i =='3' or i =='4' or i =='5' or i =='6' or i =='7' or i =='8' or i =='9':
         cuentaNumeros += 1
    if  i == ' ' or i == '.' or i == ',' or i == ';' or i == ':' :
         cuentaEspaciosVacios += 1
print('Hay un total de '+ str(contadorDeAes) + ' Aes')
print('Hay un total de '+ str(cuentaNumeros) + ' números')  
print('Hay un total de '+ str(longitudMensaje-cuentaNumeros-cuentaEspaciosVacios) + ' letras')  
#para ahorrarme condiciones se puede hacer con if i.lower() in [a,e,i,o,u]
   
