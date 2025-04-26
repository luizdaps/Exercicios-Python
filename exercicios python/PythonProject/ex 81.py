valores = []
while True:
    valores.append(int(input('digite um valor ')))
    res = str(input('quer continuar? [S/N]:'))
    if res in 'Nn':
        break
print(f'voce digitou {[len(valores)]}')
valores.sort(reverse=True)
print(f'os valores em orde decrescente são {valores}')
if 5 in valores:
    print('o valor de 5 faz parte da lista')
else:
    print('o 5 n foi encontrado na lista ')