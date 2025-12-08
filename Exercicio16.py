'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela 
a sua porção Inteira.

Começo do uso de bibliotecas em programas!
'''
import random

num1 = random.randint(1, 10)

print(num1)

# outro modelo

import math
import random

num1 = random.uniform(1, 10)

print(math.ceil(num1))