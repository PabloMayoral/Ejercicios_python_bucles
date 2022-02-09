'''lst_names = ['Ana', 'Pedro', 'Ramon', 'Sara']
lst2 = lst_names.copy()
lst2.append('Kiko')
print(lst_names)
print(lst2)

lst3 = lst_names + lst2
print(lst3)'''

listaNumeros = [1,2,3,4]
j = 0
for x in listaNumeros:
    if x % 2 == 0:
        listaNumeros[j] = 'a'
    else:
        listaNumeros[j] = 'b'
    j += 1
print(listaNumeros)
       
