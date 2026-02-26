'''
Crie um programa que leia o nome de uma cidade 
diga se ela começa ou não com o nome “Santo”.
'''

city = str(input('Em qual cidade você nasceu? ')).strip()

print(city.capitalize().startswith('Santo'))