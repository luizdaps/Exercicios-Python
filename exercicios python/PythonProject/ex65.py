resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    núm = int(input('digite um numero: '))
    soma += núm
    quant +=1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('voce digitou {} numeros e a media foi {}'.format(quant, media))
print('o maior valor foi {} e o menor foi {} '.format(maior, menor))