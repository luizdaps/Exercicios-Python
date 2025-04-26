salario = float(input('qual é o salário do funcionário?:'))
if salario >= 1250.00:
    no = salario * 10 / 100 + salario
    print('quem ganhava R${} passa a ganhar R${:.2f} '.format(salario, no))
else:
    novo = salario * 15 / 100 + salario
    print('quem ganhava R${} passa a ganhar R${:.2F}'.format(salario, novo))