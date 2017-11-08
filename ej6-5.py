# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 6 - EJERCICIO 5
Escribe un programa que permita crear dos listas de palabras y que, a continuación, elimine de la
primera lista los nombres de la segunda lista.
"""
num=input("Dime cuantas palabras tiene la lista: ")
lista1=[]
lista2=[]
contador1= 0
contador2=0
for i in range (num):
    contador1= contador1+1
    palabra1=(raw_input("Introduce una palabra %d: " % (contador1) ))
    lista1.append(palabra1)
print "La lista creada es: ", lista1

num2=input("Introduce un numero de palabras para eliminar: ")
for j in range (num2):
    contador2= contador2+1
    palabra2=(raw_input("Introduce una palabra para eliminar %d: " % (contador2) ))
    lista2.append(palabra2)
    if palabra2 in lista1:
        lista1.remove(palabra2)

print "Las palabras a eliminar son: ", lista2


print "La lista es ahora:", lista1
