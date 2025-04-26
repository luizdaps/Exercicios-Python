casa = float(input('qual valor da casa: R$'))
recebo = float(input('sálario do comprador:R$'))
anos = int(input('quantos anos de financiamento:'))
presta = casa / (anos * 12)
minimo = recebo * 30 / 100
print('para pegar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(presta))
if presta <= minimo:
    print('emprestimo pode ser consedido')
else:
    print('emprestimo negado')


