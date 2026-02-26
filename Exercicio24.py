'''
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
'''

name = str(input('Digite seu nome completo: ')).strip()
nickname = name.split()

print(f'Seu primeiro nome é: {nickname[0]}')
print(f'Seu último nome é: {nickname[len(nickname)-1]}')