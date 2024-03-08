'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
a vista dinheiro/cheque: 10% de desconto
a vista no cartao: 5% de desconto
em até 2x no cartao: preço normal
3x ou mais no cartao: 20% de juros.'''
def fil():
    print("-="*20)
pproduto = float(input("Qual é o valor do produto em reais? \nR: "))
fil()
fpgm = int(input(''' - Qual será a forma de pagamento?
[1] A vista no dinheiro/cheque
[2] A vista no cartão
[3] Parcelado no cartão
[4] Sair do sistema \n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \nR: '''))

if fpgm == 1:
    desc = pproduto*10/100
    valtotal = pproduto - desc
    fil()
    print("Método selecionado: Pagamento a vista no dinheiro/cheque")
    print("O valor total a ser pago será de R${:.2f}".format(valtotal))
    fil()
elif fpgm == 2:
    desc = pproduto*5/100
    valtotal = pproduto - desc
    fil()
    print("Método selecionado: A vista no cartão")
    print("O valor total a ser pago será de R${:.2f}".format(valtotal))
    fil()
elif fpgm == 3:
    fil()
    print("Método selecionado: Parcelamento no cartão")
    qvezes = int(input("Em quantas vezes você deseja parcelar esse valor? \nR: "))
    if qvezes <= 2:
        print("O valora total a ser pago será de R${:.2f}".format(pproduto))
    else:
        juros = pproduto*20/100
        valtotal = pproduto + juros
        print("O valor total a ser pago será de R${:.2f}".format(valtotal))

    fil()
elif fpgm == 4:
    fil()
    print("Obrigado por utilizar nosso sistema! :)")
    fil()
else:
    print("Erro.")