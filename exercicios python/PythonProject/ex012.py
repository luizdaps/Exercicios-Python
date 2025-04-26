pre = float(input('qual é o preço do produto? R$:'))
des = pre - (pre / 100 * 5)
print('o pruduto custava R${}, na promoção com desconto de 5% vai custar {:.2f}'.format(pre, des))
