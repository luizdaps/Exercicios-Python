from tokenize import endpats

n1 = int(input('outr valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
print( 'A soma é {}, o prduto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira é {} e a potencia é {}'.format(di, e))