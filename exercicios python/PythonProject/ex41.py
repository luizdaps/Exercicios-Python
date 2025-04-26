n1 = float(input('digite a primeira nota:'))
n2 = float(input('digite a segunda nota:'))
media = (n1 + n2) / 2
print('tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(n1, n2, media))
if media >=5 and media < 7:
    print('o aluno esta em recuperação')
elif media < 5:
    print('o aluno esta reprovado')
elif media > 7:
    print('o aluno esta aprovado')