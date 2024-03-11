valores = []
for cont in range(0,5):
     valores.append(int(input(f'Digite um valor na posição {cont}: ')))
# for c in range(0,len(valores)):
#      if c % 2 == 0:
#           print(valores[c], end = ' ')
print(valores)
print(f'O maior valor digitado foi {max(valores)}, na posição {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)}, na posição {valores.index(min(valores))}')
