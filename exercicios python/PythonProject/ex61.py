primeiro = int(input('primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}--'.format(termo),end='')
    termo += razao
    cont += 1
print('fim')
