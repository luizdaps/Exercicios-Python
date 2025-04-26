def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro valido. \033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuario preferiu não digitar esse numero. \033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favaor, digite um numero real valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n

n1 = leiaint('digite um valor: ')
n2 = leiafloat('digite um real: ')
print(f'o valor digitado foi: {n1} e o real foi {n2}')