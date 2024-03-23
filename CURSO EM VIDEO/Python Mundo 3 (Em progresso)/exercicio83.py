impar = ['Impares']
par = ['Pares']
while True:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = input('Deseja continuar? [S/N] \nR: ').upper()[0]
    while resp != 'S' and resp != 'N':
        print('Erro - Digite uma opção válida!')
        resp = input('Deseja continuar? [S/N] \nR: ').upper()[0]
    if resp == 'N':
        break
completa = impar + par
print(impar, par, completa)