# leia o nome do atleta e mostre sua categoria de acordo com  a idade: ate 9 anos: mirim, ate 14 anos: infantil, ate 19 anos: junior, ate 20 anos: senior, acima: master
from datetime import date
ano = int(input("Em qual ano você nasceu? \nR: "))
idade = (date.today().year) - ano
print(idade)
if idade <= 9:
    print("Você tem {} anos, e se encaixa na categoria mirim.".format(idade))
elif idade > 9 and idade <= 14:
    print("Você tem {} anos, e se encaixa na categoria infantil.".format(idade))
elif idade > 14 and idade <=19:
    print("Você tem {} anos, e se encaixa na categoria junior.".format(idade))
elif idade > 19 and idade <= 20:
    print("Você tem {} anos, e se encaixa na categoria senior.".format(idade))
else:
    print("Você tem {} anos, e se encaixa na categoria master.".format(idade))