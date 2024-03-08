sal = int(input("Qual é o seu salário atual? "))
aum = sal/10
if sal>1250:
    saln = sal + aum
    print("Seu novo salário é de {} com {} de acréscimo!".format(saln,aum))
else:
    aum2 = aum/2
    aub = aum + aum2
    saln = sal + aub
    print("Seu novo salário é de {} com {} de acréscimo!".format(saln, aub))