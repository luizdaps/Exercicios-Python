palavaras = ('aprender', 'programar', 'linguagem', 'python',
             'curso', 'grais', 'estudar', 'praticar',
             'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavaras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')