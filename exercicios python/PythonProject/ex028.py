from random import randint
from time import sleep
computador = randint(0, 5) #faz computador ''pensar''
print( '-=- '*20 )
print('vou pensar em um número entre 0 e 5. tente advinhar...')
print( '-=-'*20 )
jogador = int(input('em que numero eu pensei? ')) # jogador tenta adivinhar
print('processando...')
sleep(3)
if jogador == computador:
    print('parabens! vc conseguiu me vencer')
else:
    print('ganhei! eu pensei no numero {} e não no {}'.format(computador, jogador))
