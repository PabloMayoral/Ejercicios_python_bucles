#Reutilizo una variable creada anteriormente en ejercicios pasados
diccionario ={'Fecha nacimiento': '14/04/1990', 'nombre':'Pedro','Apellidos':'Gonzalez','color de pelo':'castaño','color de ojos':'verdes','DNI':'51320584C','Peso':'65'}
#hago una copia de la variable anterior y la renombro como 'persona'
persona = diccionario.copy()
#creo otra nueva variable diccionario con los mismos elementos que el primer diccionario
persona2 = {'Fecha nacimiento': '1/08/1990', 'nombre':'Luis','Apellidos':'Perez','color de pelo':'rubio','color de ojos':'azul','DNI':'588205444C','Peso':'84'}
#combino los 2 diccionarios anteriores en un solo diccionario
personas = {'dict1':persona , 'dict2':persona2}
#creo una variable copia del diccionario compuesto 'personas' para evitar problemas añadiendo elementos al diccionario
copia_personas = personas.copy()

#creo un bucle for que recorra las claves y los valores, en este for si se hiciera un print de k,v devorvería la k
#'dict1' y 'dict2' y la v devolveria las claves de los dos diccionarios, un ejemplo seria que devolveria 'nombre','apellidos'...
for k,v in copia_personas.items():
    #la siguiente linea de codigo la uso para añadir un elemento nuevo al diccionario con un valor por defecto de 0, lo meto dentro 
    #del bucle para que se añada tanto en el diccionario 'persona' y en 'persona2'
    k,v.setdefault('edad',0)
    #vuelvo a crear un bucle que recorra las claves-valor de los diccionarios 'persona' y 'persona2'
    for w,x in v.items():
        #En los siguientes if especifico como condicion que si la 'w' que este caso 'w' sera la clave del diccionario
        #si es igual a nombre o DNI me devuelva/pinte su respectivo valor 
        if w == 'nombre':
            print(w+': '+x)
        elif w == 'DNI':
            print(w+': '+x)
        #Este if simplemente es para realizar el punto 7 de mostrar todas las modificaciones que hace el codigo y se pueda comprobar
        #que se añadió perfectamente el nuevo elemento
        if w == 'edad':
               print(w+': '+str(x))
        #Estos ultimos if sirven para si cumplen la condicion cambien el valor del color de ojos al especificado
        if w == 'color de ojos'and x == 'verdes' :
             x =   'azules'
             print(w+': '+x)
        elif w  == 'color de ojos'and x == 'marrones' :
                    x = 'verdes'
                    print(w+': '+x)
        elif w  == 'color de ojos'and x == 'azul' :
                    x = 'marrones'
                    print(w+': '+x)
        else:
                    x = 'negros'
#Todas estas modificaciones se han realizado dentro de la variable copia del diccionario para no modificar el diccionario 
#original

                