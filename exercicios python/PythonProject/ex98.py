from time import sleep

def contador (i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='')
            sleep(0.5)
            cont += p
        print('fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('fim')



#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('agora é sua vez de personalizar a contagem')
ini = int(input('inicio: '))
fim = int(input('meio:   '))
pas = int(input('fim:     '))
contador(ini, fim, pas)