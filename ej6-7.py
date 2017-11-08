# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 6 - EJERCICIO 7
Escribe un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):
• Lista de palabras que aparecen en las dos listas
• Lista de palabras que aparecen en la primera lista, pero no en la segunda
• Lista de palabras que aparecen en la segunda lista, pero no en la primera
• Lista de palabras que aparecen en ambas listas
"""
num1=input("Dime cuantas palabras tiene la lista 1: ")
lista1= []
lista2= []
lista3= []
lista4= []
lista5= []
lista6= []
contador1= 0
contador2=0
for i in range (num1):
    contador1= contador1+1
    palabra1=(raw_input("Introduce una palabra %d: " % (contador1) ))
    lista1.append(palabra1)

print "La primera lista es: ", lista1

num2=input("Dime cuantas palabras tiene la lista 2: ")
for j in range (num2):
    contador2= contador2+1
    palabra2=(raw_input("Introduce una palabra %d: " % (contador2) ))
    lista2.append(palabra2)

print "La segunda lista es: ", lista2

for k in range (len(lista1)):
    if lista1[k] in lista2:
        lista3.append(lista1[k])
print "Palabras que aparecen en las dos listas: ", lista3

for l in range (len(lista1)):
    if lista1[l] not in lista2:
        lista4.append(lista1[l])
print "Palabras que solo aparecen en la primera lista: ", lista4

for m in range (len(lista2)):
    if lista2[m] not in lista1:
        lista5.append(lista2[m])
print "Palabras que solo aparecen en la segunda lista: ", lista5


for n in range (len(lista1)):
    lista6.append(lista1[n])
for o in range (len(lista2)):
    if lista2[o] not in lista6:
        lista6.append(lista2[o])
print "Todas las palabras que hay en las dos listas: ", lista6












"""if palabra2 in lista4:
    lista4.remove(palabra2)

if palabra1 in lista5:
    lista5.remove(palabra1)
"""

"""



"""
