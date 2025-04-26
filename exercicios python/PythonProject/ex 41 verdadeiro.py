from datetime import date
atual = date.today().year
nascimento = int(input('ano do nascimento:'))
idade =  atual - nascimento
print('atleta tem {} anos'.format(idade))
if idade <= 9:
    print('é um atleta mirim')
elif idade <=14:
    print('é um atleta infantil ')
elif idade <=19:
    print('atleta junior')
elif idade <=25:
    print('é um atleta senior')
else:
    print('atleta master')




