print('Este programa irá te exibir um produto que deseja com 5% de desconto')

valor = float(input('Digite o valor do produto que deseja: '))

desc = valor * 0.05
resultado = valor - desc


print(f'Este é o valor com o desconto de 5% \nR${resultado}')