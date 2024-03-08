from random import randint
anum = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(anum)
print(f'Os valores sorteados foram {anum}')
print(f'O maior valor sorteado foi {max(anum)}')
print(f'O menor valor sorteado foi {min(anum)}')
