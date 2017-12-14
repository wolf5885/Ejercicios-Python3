#!/usr/bin/env python3

goOn = "si"

while goOn == "si":
    number1 = int(input("Ingrese numero: "))
    number2 = int(input("Ingrese numero: "))

    print("La suma es: " + str(number1 + number2))

    goOn = input("Continuar? (si/no): ")
