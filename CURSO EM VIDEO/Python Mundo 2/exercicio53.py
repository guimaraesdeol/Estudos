frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
tdjunto = "".join(palavras) # IMPORTANTE PARA O IF DE VERIFICAR IGUALDADE
inverso = ""
for letra in range(len(tdjunto) -1, -1, -1):
    inverso += tdjunto[letra]
if tdjunto == inverso:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")

# print(tdjunto, inverso)