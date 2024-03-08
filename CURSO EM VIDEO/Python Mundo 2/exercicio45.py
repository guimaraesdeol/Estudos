# Crie um programa que consiga jogar jokenpo com você
from random import randint
# lista = [1, 2, 3] # 1 = Pedra, 2 = Papel, 3 = Tesoura
# computadorj = random.sample(lista,1) # --- isso aq deve estar dando b.o
# cmp_str = str(computadorj)[1:-1]
# cmp_str = 1
cmp_str = randint(1,3)
print(cmp_str) #- teste da saida limpa
def lun():
    print("-="*15)
lun()
print("Seja bem vindo ao jokenpô!")
lun()
escolha = int(input('''Selecione uma opção abaixo: 
[1] Pedra
[2] Papel
[3] Tesoura \nR: '''))
if escolha == cmp_str:
    print("Empatou essa merda")
elif escolha == 1 and cmp_str == 2:
    print("Você jogou pedra e a máquina jogou papel! Você perdeu.")
elif escolha == 1 and cmp_str ==3:
    print("Você jogou pedra e a máquina jogou tesoura! Você ganhou.")
elif escolha == 2 and cmp_str == 1:
    print("Você jogou papel e a máquina jogou pedra! Você ganhou.")
elif escolha == 2 and cmp_str == 3:
    print("Você jogou papel e a máquina jogou tesoura! Você perdeu.")
elif escolha == 3 and cmp_str == 1:
    print("Você jogou tesoura e a máquina jogou pedra! Você perdeu.")
elif escolha == 3 and cmp_str == 2:
    print("Você jogou tesoura e a máquina jogou papel! Você ganhou.")
else:
    print("desiste dessa merda")
'''
escolha = str(input("Escolha: Pedra, Papel ou Tesoura! \nR: ")).upper
if escolha == cmp_str:
    print("Empate! Você e a máquina escolheram {}".format(escolha))
elif escolha == "PAPEL" and cmp_str == "PEDRA":
    print("Você ganhou! Você escolheu {} e a máquina escolheu pedra!".format(escolha))
elif escolha == "TESOURA" and cmp_str == "PEDRA":
    print("Você perdeu! Você escolheu {} e a máquina escolheu pedra!".format(escolha))
elif escolha == "PEDRA" and cmp_str == "PAPEL":
    print("Você perdeu! Você escolheu {} e a máquina escolheu papel!".format(escolha))
elif escolha == "TESOURA" and cmp_str == "PAPEL":
    print("Você ganhou! Você escolheu {} e a máquina escolheu papel!".format(escolha))
elif escolha == "PAPEL" and cmp_str == "TESOURA":
    print("Você perdeu! Você escolheu {} e a máquina escolheu tesoura!".format(escolha))
elif escolha == "PEDRA" and cmp_str == "TESOURA":
    print("Você ganhou! Você escolheu {} e a máquina escolheu tesoura!".format(escolha))'''
