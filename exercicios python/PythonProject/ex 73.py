times = ('corinthias', 'palmeiras', 'santos', 'gremio',
         'cruzeiro', 'flamengo', 'vasco', 'chapecoense',
         'sao paulo', 'fluminense', 'sport recife',
         'ec vitoria', 'coritiba', 'avai', 'ponte preta',
         'atletico-go')
print(f'lista de times do brasileirao{times}')
print(f'os primeiros times são{times[0:5]}')
print(f'os ultimos times são {times[-4:]}')
print(f'os time em ordem alfabetica: {sorted(times)}')
print(f'f chapecoense esta {times.index("chapecoense")+1} posição')
