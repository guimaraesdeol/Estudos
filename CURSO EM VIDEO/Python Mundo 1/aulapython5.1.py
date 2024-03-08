# Faça um programa que leia um ano inserido e diga se ele é um ano bissexto
from datetime import date
n = int(input("Digite um número \nR: "))
if n == 0:
    n = date.today().year
if n%4 == 0 and n%100 !=0 or n%400==0:
    print("O ano {} é bissexto.".format(n))
else:
    print("O ano {} não é bissexto.".format(n))