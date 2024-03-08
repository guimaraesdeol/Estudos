# faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior peso e o menor peso lidos.
maiorpeso = 0
menorpeso = 9999999
for c in range(0,5):
    peso = float(input("Digite seu peso: "))
    if peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
print("O maior peso foi {}kg e o menor peso foi de {}kg.".format(maiorpeso, menorpeso))
