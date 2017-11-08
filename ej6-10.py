# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 6 - EJERCICIO 10
Escribe un programa que pida un número y a continuación escriba la lista de todos
los divisores del número (incluidos el uno y él mismo).
"""
numero = int(input("Introduce un numero : "))
lista= []

for i in range (1, numero):
    if (numero%i == 0):
        "%d tiene divisores" % (numero),
        lista.append(i)
lista.append (numero)
cantidad= len (lista)
print "%d tiene %d divisores: " % (numero, cantidad), (lista)
