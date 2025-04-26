soma = media = 0
galera = list()
pessoa = dict()
while True:
    pessoa.clear()
    pessoa ['nome'] = str(input('nome: '))
    while True:
        pessoa ['sexo'] = str(input('sexo: [M/F] ')).upper()[0]
        if pessoa ['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F')
    pessoa ['idade'] = int(input('idade: '))
    soma += pessoa ['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N. ')
    if resp == 'N':
        break
print('-='*30)
print(f'ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) a media de idade é de {media:5.2f} anos')
print('C) as mulheres cadastradas foram ',end='')
for p in galera:
    if p ['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) lista das pessoas que estao acima da media: ',end='')
for p in galera:
    if p['idade'] >= media:
        print('     ',end='')
        for k, v in p.items():
            print(f'{k} = {v} ',end='')
        print()
print('<< ENCERRADO >>')


