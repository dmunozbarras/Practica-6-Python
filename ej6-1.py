# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 5 - EJERCICIO 1
Escribe un programa que permita crear una lista de palabras. Para ello, el programa tiene que
pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el
programa tiene que escribir la lista.
"""
num=input("Introduce un numero ")
lista=[]
contador=0
for i in range (num):
    contador= contador+1
    palabra=(raw_input("Introduce la palabra %d " % (contador)))
    lista.append(palabra)
print "La lista creada es: ", lista
