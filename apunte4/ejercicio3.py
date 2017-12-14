#!/usr/bin/env python3

while True:
     character = input("Ingrese un caracter: ")

    if len(character) == 1:
        break

if character in ["a", "e", "i", "o", "u"]:
    print("su caracter es una vocal")
elif character in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
    print("su caracter es un digito")
else:
    print("su caracter es una consonante"
