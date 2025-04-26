dia = float(input('quantos dias alugados?:'))
km = float(input('quantos km rodados?:'))
total = dia * 60 + km * 0.15
print('o total a pagar é {:.2f}'.format(total))
