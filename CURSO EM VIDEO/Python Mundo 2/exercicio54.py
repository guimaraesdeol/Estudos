# crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não atingiram a maioridade, e quantas já são +18
maiores = 0
menores = 0
for c in range (1,8):
    idade = int(input("Digite a idade: "))
    if idade > 20:
        maiores += 1
    else:
        menores += 1
print("Das idades citadas, {} pessoas já são maiores de idade, enquanto {} são menores de idade.".format(maiores, menores))