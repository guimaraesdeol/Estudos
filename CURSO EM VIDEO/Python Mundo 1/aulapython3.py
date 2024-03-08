# Crie um programa que leia um número e mostre se ele é par ou impar
n = int(input("Digite um número \nR: "))
r = n%2
if r == 1:
    print("O número {} é impar.".format(n))
else:
    print("O número {} é par.".format(n))
