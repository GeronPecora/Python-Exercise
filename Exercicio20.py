'''
Faça um programa que leia um número de 0 a 9999 
e mostre na tela cada um dos dígitos separados.

'''


num = int(input('Digite um número de sua escolha: '))

unit = num // 1 % 10
dozens = num // 10 % 10
hundred = num // 100 % 10
thousand = num // 1000 % 10

print(f'Analisando o número escolhido...\n')

print(f'Unidade: {unit}')
print(f'Dezena: {dozens}')
print(f'Centena: {hundred}')
print(f'Milhar: {thousand}')