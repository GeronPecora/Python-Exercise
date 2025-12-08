print('Este programa vai mostrar metros em centímetros e milímetros.')

valor = float(input('Qual o valor em metros? '))

cen = valor * 100
mil = valor * 1000

print(f'{valor}m é igual a {cen}cm')
print(f'{valor}m é igual a {mil}mm')