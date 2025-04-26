a = int(input('primeiro numero:'))
b = int(input('segundo numero:'))
c = int(input('terneiro numero:'))
#verifique quem é menor
menor = a
if b<a and b<c:
     menor = b
if c<a and c<b:
    menor = c
#verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))



