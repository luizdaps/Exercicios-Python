ficha = list
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota 1 : '))
    nota2 = float(input('nota 1 :'))
    media = nota1 + nota2 / 2
    ficha.append([nota1, nota2, media])
    resp = str(input('quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(ficha)
print(f'{"NO":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate (ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('mostrar as notas de qual aluno ? (999 interrompe): '))
    if opc == 999:
        print('finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'notas de {ficha[opc] [0]} sao {ficha[opc] [1]}')
print('<<<VOLTE SEMPRE>>>')



