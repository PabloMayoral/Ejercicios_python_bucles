#Apuntesd e los ejercicios de los diccionarios
diccionario ={'Fecha nacimiento': '14/04/1990', 'nombre':'Pedro','Apellidos':'Gonzalez','color de pelo':'castaño','color de ojos':'verdes','DIN':'51320584C','Peso':65}

diccionario['Peso'] += 0.5  
print(diccionario['Peso'])

for k in diccionario.keys():
    print(k)
for v in diccionario.values():
    print(v)

for key,value in diccionario.items():
    print(key+': '+str(value))

