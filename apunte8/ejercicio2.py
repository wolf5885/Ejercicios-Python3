#!/usr/bin/env python3

def areMultiples(number1, number2):
    if number1 % number2 == 0 or number2 % number1 == 0:
        return True
    else:
        return False

number1 = int(input("Ingrese numero: "))
number2 = int(input("Ingrese numero: "))

if areMultiples(number1, number2):
    print("Son multiplos")
else:
    print("No son multiplos")
