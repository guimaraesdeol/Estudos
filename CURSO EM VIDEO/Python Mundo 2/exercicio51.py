# desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# p = 0
pter = int(input("Qual o primeiro termo? R: "))
raz = int(input("Qual é a razão? R: ")) # A RAZÃO EM PA É A SOMA CONTINUA
for z in range(0,10):
    pter += raz
    print(pter, end=" -> ")

# EXERCICIO FINALIZADO