# desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. se o falor digitado for impar, desconsidere-o
print("VALORES IMPARES SERÃO DESCONSIDERADOS")
c = 0
for z in range(0,6):
    p = int(input("Digite um número: "))
    if p%2 == 0:
        c += p
print(c)