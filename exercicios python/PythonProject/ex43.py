peso = float(input('qual seu peso? (kg):'))
M = float(input('qual sua altura? (m):'))
imc = peso / (M*M)
print('o imc dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('imc esta abaixo do peso')
elif imc <= 25 :
    print('voce esta no peso ideal')
elif imc <= 30:
    print('voce esta com sobrepeso')
elif imc <= 40:
    print(' voce esta com obesidade')
else:
    print('voce esta com obesidade morbida')

