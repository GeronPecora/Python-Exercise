'''
Neste desafio irei começar a introduzir métodos nos códigos.
Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas e minúsculas.
-Quantas letras ao todo (sem considerar espaços).
-Quantas letras tem o primeiro nome.
'''

name = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...\n')

print(f'Seu nome MAIÚSCULO seria assim: {name.upper()}')
print(f'Seu nome minúsculo seria assim: {name.lower()}')
print(f"Seu nome tem {len(name) - name.count(' ')} letras.")
print(f"Seu primeiro nome tem {name.find(' ')} letras.")