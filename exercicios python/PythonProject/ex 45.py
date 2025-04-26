from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint (0,2)
print('''suas opções: 
[ 0 ] pedra 
[ 1 ] papel
[ 2 ] tesoura''')
joga = int(input('qual a sua jogada ?:'))
print('JO')
(sleep(1))
print('KEN')
(sleep(1))
print('PO')
(sleep(1))
print('-='*11)
print('o computador escolheu {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[joga]))
print('-='*11)
if computador == 0:
    if joga == 0:
        print('empate')
    elif joga == 1:
        print('jogador vence')
    elif joga == 2:
        print('computador vence')
    else:
        print('jogada invalida')
elif computador ==1:
    if joga == 0:
        print('computador vence')
    elif joga == 1:
        print('empate')
    elif joga == 2:
        print('jogador vence')
    else:
        print('jogada invalida')
elif computador == 2:
    if joga == 0:
        print('jogador vence')
    elif joga == 1:
        print('computador vence')
    elif joga == 2:
        print('empate')
    else:print('jogada invalida')




