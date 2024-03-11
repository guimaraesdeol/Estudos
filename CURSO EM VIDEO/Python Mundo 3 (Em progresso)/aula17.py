# lista.append(item) Adiciona item no final da lista
# lista.insert(pos, item)  Adiciona item no lugar que quiser na lista
# del lista[] Deleta um item da lista por indice
# lista.pop() deleta o ultimo item da lista, ou vc especifica qual vc quer deletar. vc tem q indicar o indice
#lista.remove() Deleta um item pelo nome/valor do item

# Possibilidade de erro ao remover item que nao existe de uma lista:
# if 'item' in lista:
#    lista.remove()
# valores = list(range(x,y))
# valores.sort() - ordena em ordem crescente todos os valores
# valores.sort(reverse=True) - ordem decrescente
# len(valores) - mostra quantos elementos tem, lembrando que começa do 0
# PARA COPIAR VALORES DE DUAS LISTAS: b = a[:]

# PARTE PRÁTICA

# EXEMPLO 1:
# num = [2,5,9,1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2,2)
# if 5 in num:
#     num.remove(5)
# else:
#     print('Não achei o número 5')
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# EXEMPLO 2:
# valores = []
# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}')

a = []