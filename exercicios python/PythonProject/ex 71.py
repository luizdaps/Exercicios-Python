valor = int(input('que o valor voce quer sacar? R$'))
total = valor
ced = 50
torced = 0
while True:
    if total >= ced:
        total -= ced
        torced += 1
    else:
        if torced > 0:
            print(f'total de {torced} celulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        torced = 0
        if total == 0:
            break
print('volte sempre  ao banco CEV tenha um bom dia ')
