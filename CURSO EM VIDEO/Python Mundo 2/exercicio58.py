# import random
# na = random.randint (1, 5)
from time import sleep
from random import randint
na = randint(0,10)
cpalpite = 0
print("=-"*15)
print("Pensando em um número entre 0 a 10...")
print("=-"*15)
sleep(0.5)
# print(na) -- check da saida do numero aleatorio
resp = int(input("Qual número eu pensei? R: "))
while resp != na:
    print("Errado! Tente novamente.")
    print("=-"*15)
    cpalpite += 1
    if resp > na:
        print("O número que eu pensei é menor do que {}.".format(resp))
    elif resp < na:
        print("O número que eu pensei é maior do que {}.".format(resp))
    print("=-"*15)
    resp = int(input("Qual número eu pensei? R: "))
print("Parabéns! Você acertou o número em que pensei ({}) com {} palpites.".format(na, cpalpite))




