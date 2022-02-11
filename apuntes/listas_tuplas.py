'''lst_names = ['Ana', 'Pedro', 'Ramon', 'Sara']
lst2 = lst_names.copy()
lst2.append('Kiko')
print(lst_names)
print(lst2)

lst3 = lst_names + lst2
print(lst3)'''



'''j = 0
for x in listaNumeros:
    if x % 2 == 0:
        listaNumeros[j] = 'a'
    else:
        listaNumeros[j] = 'b'
    j += 1
print(listaNumeros)'''

listaNumeros = [1,2,3,5,6,7]     
tuplaNumeros = (2,3,7,8,1,4,0)
estan = []
noEstan = []

for x in tuplaNumeros:
    if x in listaNumeros:
         estan.append(x)
    else:
         noEstan.append(x)

print('los numeros ', estan, 'Estan en la lista de numeros', noEstan,'no estan en la lista')
j = 0
for i in listaNumeros:
    if i not in estan:
        listaNumeros[j] = 12
    j += 1
print(listaNumeros)