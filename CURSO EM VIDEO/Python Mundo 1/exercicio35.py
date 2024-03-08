def a():
    print("-="*13)
a()
print("ANALISADOR DE TRINANGULOS")
a()
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
# r1 tem que ser menor do que a soma de r2 e r3
if r1<(r2+r3) and r2<(r1+r3) and r3<(r2+r1):
    print("O triângulo pode ser formado.")
else:
    print("O triângulo não pode ser formado")

    