cont = soma = 0
while True:
    num = int(input('Digite um número: (999 Para parar) '))
    if num == 999:
        break
    cont  += 1
    soma += num
print(f'Foram digitados {cont} números e a soma resultante em {soma}.')
              