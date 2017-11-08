# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 6 - EJERCICIO 9
Escribe un programa que permita crear una lista de palabras y que, a continuación,
cree una segunda lista con las palabras de la primera, pero sin palabras repetidas
(el orden de las palabras en la segunda lista no es importante).
"""
num=input("Dime cuantas palabras tiene la lista: ")
lista1=[]
lista2=[]
contador1= 0

for i in range (num):
    contador1= contador1+1
    palabra1=(raw_input("Introduce una palabra %d: " % (contador1) ))
    lista1.append(palabra1)
print "La lista creada es: ", lista1

for i in lista1:
    if i not in lista2:
        lista2.append(i)

print "La lista sin repeticiones es:", lista2
