núm = cont = soma = 0
núm = int(input('digitou um numero [999 para parar]:'))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('digitou um numero [999 para parar:'))
print('vc digitou {} numeros e a soma entre eles foram {}'.format(cont, soma))

