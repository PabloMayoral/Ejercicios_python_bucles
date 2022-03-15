listas = list(range(1,6))
tuplas = tuple(range(1,4))
booleano = True
newDict = {'nombre':'Pablo','Apellidos':'Martin'}
lista = [listas,tuplas,'hola',89,6.8,booleano,newDict]
Dict1 = {}

for i in lista:
    Dict1[type(i)] = i
print(Dict1)
print('------------------------------------')
for k,v in Dict1.items():
    print(k)
    print(v)
print('------------------------------------')
for k,v in Dict1.items():
    if type(v) == str or type(v) == list or type(v) == tuple or type(v)== set :
        for i in v:
            print(i)
    if type(v) == dict:
        for x in v.values():
            for j in x:
                print(j)
print('------------------------------------')


mensaje = 'hola El episodio piloto se estrenó en más de 6 servicios en línea de video bajo demanda el 27 de mayo de 2015. La temporada 1 se estrenó en USA Network el 24 de junio de 2015 y la segunda temporada el 13 de julio de 2016. La tercera temporada, de 10 episodios, se estrenó el 11 de octubre de 2017. En diciembre de 2017 se renovó la cuarta y última temporada de la serie, que fue estrenada el 6 de octubre de 2019.'
mensajeMinusculas = mensaje.lower()
longitudMensaje = len(mensaje)
cuentaNumeros = 0
contadorVocales = 0
suma = 0
w = 0
listadoContador = []
listaNumeros=[]
for i in mensajeMinusculas:
    if i == 'a' or i == 'e'or i == 'i'or i == 'o'or i == 'u'or i == 'á'or i == 'é'or i == 'í'or i == 'ó'or i == 'ú' :
         contadorVocales += 1
    if i == '0' or i =='1' or i =='2' or i =='3' or i =='4' or i =='5' or i =='6' or i =='7' or i =='8' or i =='9':
         cuentaNumeros += 1
         listaNumeros += i 
         for x in listaNumeros:
             if int(x) % 3 == 0:
                 suma = suma + int(x)
    if i == 'h':
        #casteo el str a list le indico que al encontrar un 'h' se cambie por una 'H' y para añadirlo al str uso unn join
       l = list(mensaje)
       l[w] = 'H'
       mensaje = "".join(l)
    w+=1
print('Hay un total de '+ str(contadorVocales) + ' vocales')
print('Hay un total de '+ str(cuentaNumeros) + ' números')  
print(mensaje)
print(suma)

#Falta el mostrar la letra que mas se repite
#abajo es el codigo de como se haria el ejercicoo que me falto
'''frecuencia ={}
for i in mensaje:
    if i == ' ':
        continue
    elif i in frecuencia:
        frecuencia[i] += 1
    else:
        frecuencia = 1
resultado = max(frecuencia,key=frecuencia.get)
print(resultado)'''