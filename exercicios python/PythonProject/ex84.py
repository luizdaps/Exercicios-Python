temp = list ()
princ = list()
maior = menor = 0
while True:
    temp.append(str(input('nome:' )))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        maior = menor = temp = 1
    else:
        if temp [1] > maior:
            maior = temp[1]
            if temp [1] < menor:
                menor = temp [1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
print(f'ao todo vc cadastrou {len(princ)} pessoas')
print(f'o maior peso foi de {maior}Kg. peso de,',end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]',end='')
print()
print(f'o menor foi de men {menor}Kg. peso de ',end='')
for p in princ:
    if p[1] == menor:
        print(f'[{0}]', end='')





