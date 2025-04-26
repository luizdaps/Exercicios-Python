from random import randint
while True:
    c = 0
    v = int(input('diga um valor:'))
    comp = randint (0,11 )
    total = v + comp
    m = ' '
    while m not in 'PI':
        m = str(input('par ou impa? [P/I]:')).strip().upper()[0]
    print(f'vc jogou {v} e o computador {comp}. total {total}')
    print('DEU PAR' if total % 2 == 0 else 'deu impa')
    if m == 'P':
        if total % 2 == 0:
            print('vc venceu')
            c += 1
        else:
            print('vc perdeu')
            break
    elif m == 'I':
        if total % 2 == 1:
            print('vc ganhou')
            c += 1
        else:
            print('vc perdeu')
            break
    print('vamos jogar nomavente')
print(f'game over! vc venceu {c} vezez')
