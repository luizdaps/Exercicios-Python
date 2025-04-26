print('-='*20)
print('analisador de triangulos')
print('-='*20)
a = float(input('seguimento a:'))
b = float(input('seguimento b:'))
c = float(input('seguimento c:'))
if a < b + c and b < a+c and c < a + b:
    print('os seguimentos a cima formam um triangulo')
    if a == b == c:
        print('equilatero')
    elif a != b != c:
        print('escaleno')
    else:
        print('isoceles')
else:
    print('os seguimentos a cima n formam um triangulo')