

primeiro = int(input('primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}--'.format(termo),end='')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quantos termos vc quer mostrar a mais:'))
print('fim')
print('progreção mostrada com {} termos mostrados'.format(termo))




