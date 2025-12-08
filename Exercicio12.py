dol = 5.35


print('Este programa mostra o seu real convertido em dólar')

real = float(input('Digite quantos reais você quer converter em dólar: '))

converter = real / dol
converter = round(converter, 2)

print(f'Seu real foi convertido em {converter} dólares')