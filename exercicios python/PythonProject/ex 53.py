from os.path import split
nome = str(input('digite uma frase:')).strip().upper()
palavras = nome.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palindromo')










'''for c in range (len(junto) -1, -1,-1 ):
    inverso += junto [c]
print(junto, inverso)
if inverso == junto:
    print('temos um palindromo')
else:
    print(' a frase digitada n é um palindromo')''''''
