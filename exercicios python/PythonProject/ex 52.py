num = int(input('digite um numero:'))
tot = 0
for c in  range (1, num + 1):
    if num % c == 0:
        print('\033[33m',end=' ')
        tot += 1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[m0 numero {} foi dividido {} vezes'.format(num,tot))