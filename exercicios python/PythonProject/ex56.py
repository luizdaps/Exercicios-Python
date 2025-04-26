somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher = 0
for p in range (1, 5):
    print('-------{} PESSOA--------'.format(p))
    nome = str(input('nome:')).strip()
    idade = int(input('idade:'))
    sexo = str(input('sexo [M/F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20 :
        totmulher += 1
mediaidade = somaidade / 4
print('a media de idade do grupo é {} anos'.format(mediaidade))
print('o homem mais velho tem {} e se chama {}'.format(maioridade, nomevelho))
print('ao todo são {} mulheres com menos de 20 anos'.format(totmulher))

