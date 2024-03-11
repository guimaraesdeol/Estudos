valores = []
while True:
    num=int(input('Digite um valor: '))
    if num in valores:
        print('O número já existe na lista... Não adicionado!')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    resp = input('Quer continuar? [S/N] \nR: ').upper()[0]
    if resp == 'N':
        break
print(valores)