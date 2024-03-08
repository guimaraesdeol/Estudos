'''faça um prorgama que leia o ano de nascimento de um jovem 
e informe, de acordo com a sua idade: se ele ainda vai se alistar 
ao serviço militar, se é a hora de se alistar ou se ja passou do tempo de alistamento.
O programa também deve mostrar o tempo que falta ou o tempo que já passou do prazo'''
from datetime import date
def fil():
    print("-="*25)
fil()
print("SEJA BEM VINDO AO SISTEMA DE ALISTAMENTO MILITAR")
fil()
idade = int(input("Informe seu ano de nascimento: ")) # Necessário transformar em tempo restante ou excedid
anoatual = date.today().year
from time import sleep
print("Carregando sistema...")
sleep(1)
if anoatual - idade == 18:
    print("Você deve se alistar neste ano!")
elif anoatual - idade < 18:
    anof = (anoatual - idade) - 18
    from operator import neg
    anof = neg(anof)
    print("Falta(m) {} ano(s) para seu alistamento.".format(anof))
elif anoatual - idade > 18:
    anoe = (anoatual - idade) - 18
    print("Você está como refratário, com {} ano(s) pendente(s) para o alistamento.".format(anoe))