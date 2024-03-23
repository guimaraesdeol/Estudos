lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = input("Deseja continuar? [S/N]").upper()[0]
    while resp != 'S' and resp !='N':
        print("Digite uma opção válida!", end=' ')
        resp = input('Quer continuar? [S/N] \nR: ').upper()[0]
    if resp == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números.')
print(f'Valores na ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista.')