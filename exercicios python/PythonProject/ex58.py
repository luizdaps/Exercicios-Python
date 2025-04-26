from random import randint
computador = randint(0, 10)
print('sou seu computador...acabei de pensar em um numero entre 0 e 10')
print('será que vc consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('qual seu palpite?:'))
    palpite += 1
    if jogador == computador:
        acertou = True
    if jogador < computador:
        print('mais... tente mais uma vez')
    elif jogador > computador:
        print('menos... tente mais uma vez')
print('acertou com {} palpites'.format(palpite))
