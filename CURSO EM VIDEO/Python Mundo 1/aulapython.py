# Escreva um programa que faça um computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
from time import sleep
print("-="*12)
print("JOGO NÚMERO ALEATÓRIO")
print("-="*12)
n = int(input("Escreva um número para tentar acertar entre 1 e 5 \nR: "))
na = random.randint (1, 5)
print("Carregando...")
sleep(2)
if n == na:
    print("Parabéns! Você acertou o número.")
else:
    print("Número incorreto.")
    print("O número era: ", na)