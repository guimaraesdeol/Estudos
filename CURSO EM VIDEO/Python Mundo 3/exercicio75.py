tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite outro número: ')))
print(f'O número 9 apareceu {tupla.count(9)} vezes na lista.')
if 3 in tupla:
    print(f'O primero 3 foi encontrado na posição {tupla.index(3)+1}.')
else:
    print('Valor 3 não encontrado.')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')