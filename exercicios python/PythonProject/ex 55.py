maior = 0
menor = 0

for p in range (1, 6 ):
    peso = float(input('peso da {} pessoa:'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > menor:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior preso lido foi de {}kg'.format(maior))
print('o menor peso lido foi de {}kg'.format(menor))



