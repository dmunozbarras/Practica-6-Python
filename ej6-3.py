# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 6 - EJERCICIO 3
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida dos
palabras y sustituya la primera por la segunda en la lista.
"""

num=input("Introduce un numero ")
lista=[]
contador= 0

for i in range (num):
    contador= contador+1
    palabra=(raw_input("Introduce una palabra %d " % (contador) ))
    lista.append(palabra)
print "La lista creada es: ", lista

sustituir=(raw_input("Sustituir la palabra ") )
nuevo=(raw_input("por la palabra ") )
while sustituir in lista:
    indice=lista.index(sustituir)
    lista.insert(indice, (nuevo))
    del lista[indice +  1]

print lista
