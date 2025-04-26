km = float(input('qual a distancia da sua viagem ?'))
if km <= 200:
    bonus = km * 0.50
else:
    bonus = km * 0.45
    print('vc estra preste de fazer uma viagem de {}km'.format(km))
    print('e o preço da sua passagem será R${:.2f}'.format(bonus))
2


