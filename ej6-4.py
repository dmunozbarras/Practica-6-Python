# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 6 - EJERCICIO 4
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y elimine esa palabra de la lista
"""
num=input("Dime cuantas palabras tiene la lista: ")
lista=[]
contador= 0

for i in range (num):
    contador= contador+1
    palabra=(raw_input("Introduce una palabra %d: " % (contador) ))
    lista.append(palabra)
print "La lista creada es: ", lista
eliminar=(raw_input("Eliminar la palabra: ") )
while eliminar in lista:
    lista.remove(eliminar)

print"La lista es ahora: ", lista
