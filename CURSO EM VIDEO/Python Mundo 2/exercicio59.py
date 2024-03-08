# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
# [1] SOMAR [2] MULTIPLICAR [3] MAIOR [4] NOVOS NUMEROS [5] SAIR
condi = 0
def col():
    print("=-"*15)
col()
print("Seja bem-vindo ao nosso sistema!")
col()
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
while condi != 5:
    col()
    print('''Escolha uma opção abaixo: 
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR''')
    col()
    condi = int(input("R: "))
    if condi == 1:
        r = n1 + n2
        print("A soma entre {} e {} resulta em {}.".format(n1,n2,r))
    elif condi == 2:
        r = n1*n2
        print("A multiplicação entre {} e {} resulta em {}.".format(n1,n2,r))
    elif condi == 3:
        if n1 > n2:
            print("O maior número é {}.".format(n1))
        else:
            print("O maior número é {}.".format(n2))
    elif condi == 4:
        n1 = float(input("Digite o novo primeiro número: "))
        n2 = float(input("Digite o novo segundo número: "))
    elif condi > 5:
        print("Digite uma opção válida! [1-5]")
col()
print("Obrigado por utilizar nosso sistema!")
col()