#!/usr/bin/env python3

def getDividers(number):
    dividers = 0

    for i in range(1, number +1):
        if number % i == 0:
            dividers += 1

            return dividers

number1 = int(input("numero: "))

dividers1 = getDividers(number1)

print(str(number1) + " tiene " + str(dividers1) + " divisores")
