totg = caro = mb = 0
maisbarato = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o preço do produto: '))
    totg += preco
    if preco > 1000:
        caro += 1
    elif mb > preco:
        maisbarato = nome
        mb = preco
    elif mb == 0:
        mb = preco
        maisbarato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] \nR: ')).upper().strip()
    if resp == 'N':
        print('Programa Encerrado.')
        break
print(f'Foram citados {caro} produtos acima de 1000 reais, totalizando {totg} reais em total gasto. O protudo mais barato custou {mb} reais e se chama {maisbarato}')
