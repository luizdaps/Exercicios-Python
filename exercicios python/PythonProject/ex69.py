tot18 = toth = tot20 = 0
while True:
    idade = int(input('idade:'))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('sexo: [M/F]:')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sex == 'M':
        toth += 1
    if sex == 'F':
        tot20 += 1
    respec = ' '
    while respec not in 'SN':
        respec = str(input('quer continuar ?)) [S/N]')).strip().upper()[0]
    if respec == 'N':
            break
print(f'total de pessoas com mais de 18 anos {tot18}')
print(f'total de todos temos {toth} homens cadastrados')
print(f'e temos {tot20} mulheres com menos de 20 anos ')





