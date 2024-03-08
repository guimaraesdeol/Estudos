# faça um programa que leia um número inteiro e diga se ele é ou nao um número primo.
# REGRAS:
# Uma divisão com resto zero (e neste caso o número não é primo).
# Uma divisão não exata (resto diferente de zero) e o quociente for menor que o divisor, então o número é primo.
# Uma divisão não exata (resto diferente de zero) e o quociente for igual ao divisor, então o número é primo.
num = int(input("Escreva um número inteiro: "))
tot = 0
for c in range(1,num+1):
    if num%c == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m",end=" ")
    print("{}".format(c), end=" ")
print("\033[m")
print("\ O número {} foi divido {} vezes.".format(num,tot))
if tot == 2:
    print("O número informado é primo!")
else:
    print("O número informado não é primo.")