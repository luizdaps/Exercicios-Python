from random import randint
from time import sleep

def sorteia(lista):
    print('sorteando 5 valores da lista: ',end='')
    for cont in range (0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ',end='')
        sleep(0.5)
    print('pronto')


def somaPAR (lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os valores pares da lista {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPAR(numeros)



