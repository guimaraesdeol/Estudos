# faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0 com a pausa de 1 segundo entre as contagens
def co():
    print("=-"*20)
co()
print("FOGOS DE ARTIFÍCO ESTOURANDO EM...")
c = 10
from time import sleep
for c in range(10,-1,-1):
    if c == 10:
        print("DEZZZZ")
    elif c == 9:
        print("NOVEEE")
    elif c == 8:
        print("OITOOOOO")
    elif c == 7:
        print("SETEEEEE")
    elif c == 6:
        print("SEISSSSSS")
    elif c == 5:
        print("CINCOOOOOO")
    elif c == 4:
        print("QUATROOOOOO")
    elif c == 3:
        print("TRÊÊÊÊSSSSS")
    elif c == 2:
        print("DOISSSSSSS")
    elif c == 1:
        print("UMMMMMMMMM")
    elif c == 0:
        co()
        print("BOOOOOOOOOOOOOM!!!!!!!!!!!!!!!!!")
        co()
    sleep(0.5)