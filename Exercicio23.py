'''
Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que 
posição ela aparece a última vez.
'''

phrase = str(input('Digite qualquer frase: ')).upper().strip()

print(f"A letra A aparece no total de {phrase.count('A')} na sua frase.")
print(f"A primeira letra A aparece na posição: {phrase.find('A')+1}")
print(f"A última letra A aparece na posição: {phrase.rfind('A')+1}")