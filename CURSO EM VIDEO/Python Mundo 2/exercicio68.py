from random import randint
v = 0
while True:
    n = int(input('Digite um número: '))
    computador = randint(0,11)
    total = n + computador
    tipo = ' '
    tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {computador}. Total de {total}.', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {v} vezes.')
