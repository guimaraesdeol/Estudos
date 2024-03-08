'''desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC  e mostre seu status, de acordo com a tabela abaixo:
abaixo de 18.5: abaixo do peso
entre 18.5 e 24,9: peso ideal
25 até 29,9: sobrepeso
30 até 39,9: obesidade
acima de 40: obesidade mórbida'''
peso = float(input("Quanto você pesa? \nR: "))
altura = float(input("Qual é a sua altura? \nR: "))
imc = peso/(altura * altura)
if imc < 18.5:
    print("Seu imc é de {:.2f} e você está abaixo do peso!".format(imc))
elif imc > 18.5 and imc <= 24.9:
    print("Seu imc é de {:.2f} e você está no peso ideal!".format(imc))
elif imc >= 25 and imc <=29.9:
    print("Seu imc é de {:.2f} e você está em sobrepeso.".format(imc))
elif imc >=30 and imc <= 39.9:
    print("Seu imc é de {:.2f} e você está obeso.".format(imc))
else:
    print("Seu imc é de {:.2f} e você está em obesidade mórbida! Procure um médico urgentemente.".format(imc))