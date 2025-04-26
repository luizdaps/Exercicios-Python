n1 = float(input('digite sua primeira nota:'))
n2 = float(input('digite sua segunda nota:'))
m = (n1 + n2)/2
print('sua media foi {:.1f}'.format(m))
if m>= 6.0:
    print('sua media foi muito boa! parabens!')
else:
    print('sua media foi ruim! estude mais!')