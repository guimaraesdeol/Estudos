p = 's' 
soma = quant = media = 0
while p in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if  quant == 1:
        maior =  menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    p = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, media)) 
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
