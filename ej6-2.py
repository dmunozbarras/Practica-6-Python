# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 6 - EJERCICIO 2
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y diga cuántas veces aparece esa palabra en la lista.
"""
num=input("Introduce un numero ")
lista=[]
contador= 0
veces= 0

for i in range (num):
    contador= contador+1
    palabra=(raw_input("Introduce una palabra %d " % (contador) ))
    lista.append(palabra)
print "La lista creada es: ", lista
palabra=(raw_input("Dime una palabra "))
for i in lista:
    if palabra == (i):
        veces+= 1
print "La palabra %s sale %s veces" % (palabra, veces)
