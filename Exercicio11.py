# Tabuada
print('Este programa vai mostrar a tabuada do número que deseja.')

valor = int(input('Digite um número: '))

print(f"\nTabuada do {valor}\n" + "-"*15)

for i in range(1, 11):
    print(f'{valor} x {i} = {valor * i}')

print("-"*15)