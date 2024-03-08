# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Precisa do input = valor da casa, salario do comprador, e em quantos anos ele vai pagar, 
# Deve calcular o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from time import sleep
vcasa = int(input("Qual é o valor da casa? \nR: "))
vsalario = int(input("Quanto você ganha mensalmente? \nR: "))
qano = int(input("Em quantos anos você deseja pagar o imóvel? \nR: "))
qmes = qano*12
print("Analisando informações...")
sleep(1)
pmensal = vcasa / qmes # valor da mensalidade
maxemprestimo = (vsalario * 30)/100 # valor máximo dos 30%
print("O valor mensal sera de: R${:.2f}. ".format(pmensal))
rsp = "o"
rsp = input("Deseja continuar? S/N \nR: ")
if rsp == "S" or "s" or "sim":
    if pmensal <= maxemprestimo:
        print("Seu empréstimo foi aprovado")
    else:
        print("Empréstimo negado")
else:
    print("Programa cancelado.")


# corrigido:
# casa = int(input("Valor da casa: "))
# salario = float(input("Salário do comprador: R$"))
# anos = int(input("Em quantos anos?"))
# prestação = casa/(anos*12)
# minimo = salario*30/100
# print("Para pagar uma casa de {:.2f} em {} anos, a prestação será de R${:.2f}".format(casa, anos, prestação))
# if prestação <= minimo:
#     print("Empréstimo aprovado!")
# else:
#     print("Empréstimo negado!")
