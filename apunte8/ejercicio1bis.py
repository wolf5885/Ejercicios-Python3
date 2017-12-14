#!/usr/bin/env python3

def getDividers(number):
    dividers = []

    for i in range(1, number + 1):
        if number % i == 0:
            dividers.append(i)

            return dividers

number1 = int(input("Numero: "))

dividers1 = getDividers(number1)

for i in dividers1:
    print(str(i))
