#!/usr/bin/env python3

from os import system

number = int(input("\nNumero: "))

system("clear")

print("Tabla del: " + str(number))
print("==== ===")
print()

for i in range(1, 11):
    print(str(number) + " x " + str(i) + " = " +str(number * i))

print()
