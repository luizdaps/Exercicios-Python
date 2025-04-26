def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com{idade} anos : não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: voto opcional'
    else:
        return f'com {idade} anos: voto obricatorio'

nasc = int(input("em que ano vc nasceu ?"))
print(voto(nasc))
