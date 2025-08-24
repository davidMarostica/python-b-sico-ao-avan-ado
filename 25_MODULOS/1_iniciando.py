# Aula 1 - O que são modulos
import meu_modulo

print (meu_modulo.saudacao("David"))

import math

print(math.sqrt(16))

# aula 2 - modulos padrão / core modules
print(math.pi)

print(math.cos(math.radians(60)))

import random

print(random.randint(1, 10))

lista = ["a", "b", "c", "d"]

print(random.choice(lista))

import datetime

print(datetime.datetime.now())

print(datetime.date.today())

import os # operational system

print(os.getenv("PATH"))


