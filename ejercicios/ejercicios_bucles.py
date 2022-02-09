from xmlrpc.client import Boolean


colores = ['Azul','Rojo','Verde']
numeros = (1,2,3)
i=0
longitud = len(colores)

while i < longitud:
   
   print('el elemento '+ str(i+1) +' es: '+ colores[i])
   i += 1
print('------------------------------------')
j=0  
for j in range(longitud):
   print('el elemento '+ str(j+1) +' es: '+ colores[j])
print('------------------------------------')
#SEGUNDO EJERCICIO NENO 
msg = 'hola'
decimal = 8,5
booleano = True
arrayList =[colores,numeros,booleano,decimal,msg]
#print(arrayList)
#print(arrayList[0][0])
#longitud_array = len(arrayList)
#print(longitud_array)
#for j in range(longitud_array):
 #  if type(j) == list:
  # print(arrayList[j])
  #    z=0
   #   for z in range(len(arrayList[j])):
    #   print(arrayList[j][z])

for i in arrayList:
   if type(i) == list:
      for x in i:
         print(x)
print('------------------------------------')

#TERCER EJERCICIO
z =0
for x in range(10):
         z += x
print ('el resultado es ' + str(z))    
               