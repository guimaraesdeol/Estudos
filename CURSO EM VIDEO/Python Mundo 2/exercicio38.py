# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O *primeiro valor* é maior, O *Segundo valor* é maior ou Nao existe valor maior (=)
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número : "))
if n1 > n2:
    print("O número {} é o maior entre os dois.".format(n1))
elif n2 > n1:
    print("O número {} é o maior entre os dois.".format(n2))
elif n1 == n2:
    print("Os números fornecidos são iguais!")