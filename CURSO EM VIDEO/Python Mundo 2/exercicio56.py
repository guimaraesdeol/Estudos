# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final mostre: a média de idade do grupo, qual é o nome do homem mais velho, e quantas mulheres tem menos de 20 anos.
midade = 0
maiori = 0
# cad = []
hmv = ''
m20 = 0
for c in range(1,5):
    nome = str(input("Qual é o seu nome? R: "))
    idade = int(input("Qual é a sua idade? R: "))
    midade += idade
    sex = str(input("Qual é o seu sexo? M/F R: "))
    if c == 1 and sex in 'Mn':
        maiori = idade
        hmv = nome
    elif idade > maiori and sex in "Mm":
        maiori = idade
        hmv = nome
    elif idade < 20 and sex == "F" or sex == "f" :
        m20 += 1
    # cad += [nome, idade, sex]
meidade = midade/4 # CALCULA A MEDIA DAS IDADES
print("A média de idade do grupo é {}".format(meidade))
print("O homem mais velho se chama {} e tem {} anos".format(hmv,maiori))
print("Conforme as informações, foram citadas {} mulheres com menos de 20 anos.".format(m20))