i = int(input("Digite o inicio: "))
f = int(input("Digite o fim: "))
p = int(input("Digite o passo: "))
timer = 10
from time import sleep
for timer in range(i,f+1,p):
    print(timer)
    sleep(0.5)
print("fim")