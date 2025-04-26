numeros = list()
while True:
    n = int(input('digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado! não vou adicionar...')
    r = str(input('quer continuar ? [S/N]'))
    if r in 'Nn':
        break
    numeros.sort()
    print(f'voce digitou os valores {numeros}')


