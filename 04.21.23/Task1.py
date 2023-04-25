# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

import random

def prompt(msg):
    a = int(input(msg))
    return a

def dissident(jorney):
    for i in range(len(jorney)):
        if jorney[i] >= 4:
            jorney[i] = random.randint(1,2)
    return jorney

maximal

jorney = [random.randint(minn,maxx) for i in range(5,20)]
print(jorney)
new_jorney = dissident(jorney)
print(jorney)