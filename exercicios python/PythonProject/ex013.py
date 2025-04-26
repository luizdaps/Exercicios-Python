au = float(input('qual valor sálarial do funcionario? R$:'))
no = au + (au / 100) * 15
print('um funcionario que ganhava R${}, com 15% de aumento, passa a receber {:.2f}'.format(au, no))