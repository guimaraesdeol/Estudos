while True:
    tab = int(input("Qual tabuada? \nR: "))
    if tab < 0:
        break
    c = 0
    for c in range(0,11):
        c+1
        z = tab*c
        print("{}x{}={}".format(tab,c,z))