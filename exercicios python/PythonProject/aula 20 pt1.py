def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'a soma de A + B {s}')


#programa principal
soma(4, 5)






def contador (*num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)






def contador (*num):
    for valor in num:
        print(f'{valor} ',end='')
        print('FIM!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)






def contador (*num):
    tam = len(num)
    print(f'recebi o valor de {num} e são todos {tam} numeros')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)






def dobra (lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
