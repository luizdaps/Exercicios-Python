from math import hypot
co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjecente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

