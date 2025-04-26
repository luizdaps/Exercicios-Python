pre = float(input('preço das compras:'))
print('''FORMAS DE PAGAMENTO'
[ 1 ] á vista dinheiro/cheque
[ 2 ]á vista cartão
[ 3 ]2x no cartão
[ 4 ]3x ou mais no cartão''')
op1 = float(input('qual é a opção? '))
if op1 == 1:
    total = pre - (pre * 10 / 100)
elif op1 == 2:
    total = pre - (pre * 5 / 100)
    print('sua compra de R${:.2f} vai custar R${:.2f}'.format(pre ,total))
elif op1 == 3:
    total = pre
    parcela = pre / 2
    print('sua compra vai ser parcelada em 2x de {:.2f}R$'.format(parcela))
elif op1 == 4:
    total = pre +(pre * 20 /100)
    totparc = int(input('quantas parcelas? '))
    totparcela = total / totparc
    print('sua compra vai ser parcelada em {}x de {:.2f}R$'.format(totparc, totparcela))
    print('sua compra de {:.2f}R$. vai custar R${:.2f} no final'.format(pre, total ))
else:
    print('erro tente novamente')







