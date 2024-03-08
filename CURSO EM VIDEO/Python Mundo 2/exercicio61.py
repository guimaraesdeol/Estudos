pter = int(input("Qual o primeiro termo? R: "))
raz = int(input("Qual é a razão? R: ")) # A RAZÃO EM PA É A SOMA CONTINUA
z = 0
while z < 10:
    pter += raz
    z += 1
    if z < 10:
        print(pter, end=" -> ")
    else:
        print(pter)