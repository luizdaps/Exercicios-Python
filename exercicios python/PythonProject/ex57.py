s = str(input('digite seu sexo : [M/F]')).strip().upper()[0]
while s not in 'MmfF:':
    s = str(input('dados invalidos. por favor informe seu sexo:')).strip().upper()
print('sexo {} registrado com sucesso'.format(s))

