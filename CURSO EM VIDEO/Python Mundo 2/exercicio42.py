# refaça o desafio 35 dos triÂngulos acrescentando o recurso de mostrar que tipo de triangulo será formado: Equilátero: Todos os lados iguais, Isósceles: dois lados iguais, Escaleno: Todos os lados diferentes
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
# r1 tem que ser menor do que a soma de r2 e r3
if r1<(r2+r3) and r2<(r1+r3) and r3<(r2+r1):
    print("O triângulo pode ser formado.")
    if r1 == r2 and r1 == r3:
        print("O triângulo formado é equilátero (todos os lados iguais).")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("O triângulo é isóceles (possui dois lados iguais).")
    else:
        print("O triângulo é escaleno (possui todos os lados diferentes).")
else:
    print("O triângulo não pode ser formado")

    