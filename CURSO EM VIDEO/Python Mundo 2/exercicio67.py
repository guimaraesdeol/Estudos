while True:
    num = int(input("Qual tabuada? \nR: "))
    if num < 0: 
        break
    for c in range(1,11):
        print(f"{num}x{c}={num*c}")
print('Programa finalizado.')