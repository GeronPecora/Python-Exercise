# Solicita o nome do usuário e armazena na variável 'nome'
nome = str(input('Qual o seu nome? '))

print(f'Bem-vindo {nome}!')


# Solicita a idade do usuário e converte apenas para números inteiro
idade = int(input('Que bom ter você aqui conosco! Quantos anos você tem? '))

# Verifica se o usuário é maior de 18 anos
if idade > 18:
    print(f'Wow! {idade}? então esse jogo é para você mesmo.')

# Caso tenha exatamente 18 anos, exibe uma mensagem específica
elif idade == 18:
    print('Eita, quase que você não passa pelo teste de idade! Aliás bem-vindo(a) a vida adulta!')

# Se for menor de idade, encerra o programa
else:
    print('Você está em fase de testes para esse jogo, cresça mais e volte aqui.')
    exit()

# Loop principal para perguntar se o usuário quer continuar ou não
while True:

    resposta = input(f'Então vamos lá {nome}, você vai querer continuar o jogo? s/n? ').strip().lower() # strip remove espaços, lower deixa tudo minusculo
    
    # Caso a resposta seja 'sim' ou 's', inicia o jogo
    if resposta in ['sim', 's', 'si']:
        print('3...')
        print('2...')
        print('1...')
        print('Começando o jogo...')
        break # Encerra o programa após iniciar (simula início do jogo)
    
    
    elif resposta in ['nao', 'n', 'no']:
        print('Obrigado pela atenção, até mais!')
        break

    # Caso o usuário digite algo inválido, pede uma nova resposta   
    else:
        print('Resposta inválida. Digite apenas s/n')
    