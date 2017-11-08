# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 6 - EJERCICIO 6
Escribe un programa que permita crear una lista de palabras y que, a continuación,
cree una segunda lista igual a la primera, pero al revés (no se trata de escribir
la lista al revés, sino de crear una lista distinta).
"""
num=input("Dime cuantas palabras tiene la lista: ")
lista1=[]

contador= 0

for i in range (num):
    contador= contador+1
    palabra=(raw_input("Introduce una palabra %d: " % (contador) ))
    lista1.append(palabra)
print "La lista creada es: ", (lista1)
lista2= (lista1)
lista2.reverse ()
print "La lista inversa es: ", (lista2)
