#!/usr/bin/env python3

miLista = []

while True:
    miDiccionario  = {}
    miDiccionario["name"] = input("ingrese nombre: ")
    miDiccionario["lastName"] = input("ingrese apellido: ")
    miLista.append(miDiccionario)

    if input("Otro? (s/n)") == "n":
        break

for persona in miLista:
    print(persona["name"] + " " + persona["lastName"])
