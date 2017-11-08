# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 6 - EJERCICIO 8
Escribe un programa que permita crear una lista de palabras y que, a
continuación, ordene la lista por orden alfabético.
"""
num=input("Dime cuantas palabras tiene la lista: ")
lista1=[]
contador1= 0
for i in range (num):
    contador1= contador1+1
    palabra1=(raw_input("Introduce una palabra %d: " % (contador1) ))
    lista1.append(palabra1)
print "La lista creada es: ", lista1

lista1.sort()
print "La lista por orden alfabetico es: ", lista1
