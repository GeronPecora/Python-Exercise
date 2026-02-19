print('Seja bem-vindo ao classificador de herói.\nPara começar me diga o seu nome e a sua experiência atual para determinar sua classificação.\n')

nome = input('Qual o nome do jogador? ')

# LOOP
while True:
    nivel_input = input('Qual o nível de experiência do jogador? ')

    if nivel_input.isdigit():  # valida se contém apenas números
        nivel = int(nivel_input)  # converte para int APÓS validar
        break
    else:
        print("Erro! Digite apenas números para XP.\n")

# CLASSIFICAÇÃO
if nivel < 1000:
    classificacao = 'Ferro'

elif 1000 <= nivel < 2000:
    classificacao = 'Bronze'

elif 2000 <= nivel < 5000:
    classificacao = 'Prata'

elif 5000 <= nivel < 7000:
    classificacao = 'Ouro'

elif 7000 <= nivel < 8000:
    classificacao = 'Platina'

elif 8000 <= nivel < 9000:
    classificacao = 'Ascendente' 

elif 9000 <= nivel < 10000:
    classificacao = 'Imortal'

else:
    classificacao = 'Radiante'

print(f'\nO Herói {nome} está no nível de {classificacao}!')
