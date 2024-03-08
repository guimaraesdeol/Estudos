q = 0
z = 0
pter = int(input("Qual o primeiro termo? R: "))
raz = int(input("Qual é a razão? R: ")) # A RAZÃO EM PA É A SOMA CONTINUA
while z < 10:
    pter += raz
    z += 1
    if z < 10:
        print(pter, end=" -> ")
    else:
        print(pter)
while q == 0:
    print("Quer mais termos? [1] Para sim , [0] Para encerrar o programa.")
    r = int(input("R: "))
    if r == 0:
        q = 1
    elif r == 1:
        p = z+10
        while z < p:
            pter += raz
            z += 1
            if z < 10:
                print(pter, end=" -> ")
            else:
                print(pter)
print("Programa encerrado!")
