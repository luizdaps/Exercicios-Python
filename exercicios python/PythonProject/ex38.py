from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK

num = int(input('digite um numero inteiro:'))
print('''escolha uma das bases para conversção:
[ 1 ] converter para binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
op = int(input('sua opção:'))
if op == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção invalidada tente novamente')










