#!/usr/bin/env python3

maximum = int(input("Ingrese numero: "))
middle = int(input("Ingrese numero: "))

if middle > maximum:
    auxiliar = maximum
    maximum = middle
    middle = auxiliar

minimum = int(input("Ingrese numero: "))

if minimum > maximum:
    auxiliar = maximum
    maximum = minimum
    minimum = middle
    middle = auxiliar
elif minimum > middle:
    auxiliar = middle
    middle = minimum
    minimum = auxiliar

print(str(minimum) + " " + str(middle) + " " + str(maximum))
