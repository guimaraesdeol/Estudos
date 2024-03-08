'''crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida: <5 = reprovado, entre 5 e 6.9 = recuperação, media 7> = aprovado'''
n1 = float(input("Digite sua nota 1: "))
n2 = float(input("Digite sua nota 2: "))
m = (n1+n2)/2
if m < 5:
    print("Você foi reprovado. Sua média foi de {}".format(m))
elif m <7:
    print("Você está de recuperação. Sua média foi de {}".format(m))
else:
    print("Você foi aprovado. Sua média foi de {}".format(m))