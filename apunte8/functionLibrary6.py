#!/usr/bin/env python3

from sys import exit

add = lambda number1, number2: number1 + number2

substract = lambda number1, number2: number1 - number2

multiply = lambda number1, number2: number1 * number2

def divide(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        print("ERROR! no se puede dividir por cero")
        exit(1)

def custompow(number1, number2):
    result = number1

    for i in range(int(number2)):
        result *= number1

        return result
