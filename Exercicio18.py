'''
O mesmo professor do desafio 17 quer sortear a
ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random

aluno1 = str(input('Qual o nome do primeiro aluno? '))
aluno2 = str(input('Qual o nome do segundo aluno? '))
aluno3 = str(input('Qual o nome do terceiro aluno? '))
aluno4 = str(input('Qual o nome do quarto aluno? '))

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print(f'A ordem ficou o seguinte: {lista}')