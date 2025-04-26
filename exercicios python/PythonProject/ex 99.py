from time import sleep

def maior (*num):
    cont = maior = 0
    print('-=' * 30)
    print('\nAnalisando os valores...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram informados {cont} valores')
    print(f'o maior valor informado foi {maior}')


# programa principal
maior (2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()