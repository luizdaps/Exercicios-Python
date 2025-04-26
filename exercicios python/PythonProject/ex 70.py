total = totmil = menor = cont = 0
while True:
    produto = str(input('nome do produto:'))
    prec = float(input('preço: R$'))
    cont +=1
    total += prec
    if prec < 1000:
        totmil += 1
    if cont ==1:
        menor = prec
        baroto = produto
    else:
        if prec < menor:
            menor = prec
            baroto = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar ? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('fim do programa')
print(f'o valor total da compra foi {total:.2f}')
print(f'temos {totmil} produtos custando mais de R$1000,00')
print(f'o produto mais barato foi {baroto} custa R${menor:.2f}')
