#!/usr/bin/env python3

from functionLibrary6 import *
from os import system

while True:
    result = 0
    system("clear")

    number1 = float(input("numero: "))

    operation = ""
    while operation not in ["s", "r", "m", "d", "p"]:
        operation = input("Operación (s, r, m, d, p): ")

    number2 = float(input("numero: "))

    if operation == "s":
        result = add(number1, number2)
    elif operation == "r":
        result = substract(number1, number2)
    elif operation == "m":
        result = multiply(number1, number2)
    elif operation == "d":
        result = divide(number1, number2)
    elif operation == "p":
        result = custompow(number1, number2)
    else:
        print("Operacion Incorrecta")

    print()
    print("Resultado: " + str(result))
    print()

    repeat = ""
    while repeat != "s" and repeat != "n":
        repeat = input("Realizar otro calculo? (s/n): ")

    if repeat == "n":
        break
