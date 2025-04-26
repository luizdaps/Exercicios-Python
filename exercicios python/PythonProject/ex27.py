from os.path import split

nome = str(input('diga seu nome:')).upper().strip(' ')
n = nome.split()
print('seu primeiro nome é {}'.format(n[0]))
print('seu ultimo nome é {}'.format(n[len(n)-1]))
