# desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas
d = int(input("Qual a distância da sua viagem em km? \nR: "))
if d <= 200:
    p = d*0.50
    print(p)
    print("Sua viagem custará {} reais.".format(p))
else:
    p = d*0.45
    print("Sua viagem custará {} reais.".format(p))