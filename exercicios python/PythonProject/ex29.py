v = float(input('qual é a velocidade do carro?:'))
if v>= 80:
    print('multado sua velocidade execedeu o limite permitido que é de  80km/h')
    multa = v * 7 - 80
    print('voce deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('tenha um bom dia dirija com segurança')

