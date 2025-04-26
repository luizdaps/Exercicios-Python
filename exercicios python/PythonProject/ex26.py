frase = str(input('digite sua frase:')).upper().strip()
print('a letra a parece {} vezes na frase'.format(frase.count('A')))
print('a primeira letra a aparece na posição {}'.format(frase.find('A')+1))
print('a ultima letra a aparece na posição {}'.format((frase.rfind('A')+1)))