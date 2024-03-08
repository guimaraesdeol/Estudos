# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite
v = int(input("Quantos km/h você andou? \nR: "))
if v>80:
    l = (v - 80)
    m = l*7
    print("Você andou {} km/h acima do limite!".format(l))
    print("Você foi multado em {} reais!".format(m))
else:
    print("Você não foi multado")