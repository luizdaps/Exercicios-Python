from math import radians, sin, cos, tan
angulo = float(input('digite o angulo que vc deseja:'))
seno = sin(radians(angulo))
print('o angulo de {} tem SENO de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('o angulo de {} tem COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('o angulo de {} tem TANGENTE de {:.2f}'.format(angulo,tangente))

