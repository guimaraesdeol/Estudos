toth = tot18 = totm = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 = tot18 + 1
    if sexo == 'M':
        totm = totm + 1
    if sexo == 'F' and idade < 20:
        toth = toth + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totm} homens cadastrados')
print(f'E temos {toth} mulheres com menos de 20 anos')