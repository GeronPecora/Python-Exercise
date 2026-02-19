'''
Neste desafio irei começar a introduzir métodos nos códigos.
Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas e minúsculas.
-Quantas letras ao todo (sem considerar espaços).
-Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...\n')

print(f'Seu nome MAIÚSCULO seria assim: {nome.upper()}')
print(f'Seu nome minúsculo seria assim: {nome.lower()}')
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras.")
print(f"Seu primeiro nome tem {nome.find(' ')} letras.")