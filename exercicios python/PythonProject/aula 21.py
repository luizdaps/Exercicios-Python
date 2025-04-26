#parametros opcionais
def somar (a=0, b=0, c=0):
    s = a + b + c
    print(f'a soma dos vale {s}')
somar(3,3,5)




#escopo de variaveis
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')



#retorno de valores
def somar (a=0, b=0, c=0):
    s = a + b + c
    return
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(4)

print(f'o resultados foram {r1}, {r2} e {r3}')


#exemplo
def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f *= c
        return f
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'os resultados são {f1}, {f2}, {f3}')




def par (n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('digite um numero:'))
if par (num):
    print('é par')
else:
    print('nao é par')


