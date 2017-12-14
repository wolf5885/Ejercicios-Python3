#!/usr/bin/env python3

vector = []

for i in range(1, 101):
    if i % 2 != 0:
        vector.append(i)

for i in range(len(vector)):
    print(str(vector[i]))
