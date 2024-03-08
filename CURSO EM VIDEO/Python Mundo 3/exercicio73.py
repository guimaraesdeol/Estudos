# BRASILEIRAO
times = ('Atletico-MG', 'Vasco Gama', 'Flamengo', 'Fluminense',
         'Botafogo', 'CA Paranaense', 'Cuiabá', 'Bragantino',
         'Corinthians', 'Internacional', 'Criciúma', 'Bahia',
         'AC Goianense', 'Fortaleza CE', 'Gremio', 'Palmeiras',
         'São Paulo', 'Cruzeiro', 'Vitória', 'Juventude')
# print(len(times))
print(f'Os 5 primeiros colocados foram: ', end='')
for pos, c in enumerate(times[:5]):
    if pos < 4:
        print(c, end=', ')
    else:
        print(c, end='.')
print("")
print(f'Os últimos 4 colocados foram: ', end='')
for pos, c in enumerate(times[-4:]):
    if pos < 3:
        print(c, end=', ')
    else:
        print(c, end='.')
        print('')
print(sorted(times))
print(f'O time {times[-7]} está na posição {times.index("Fortaleza CE")+1} da tabela.')
