#ESTRUTURA WHILE
sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip() [0]
while sexo != 'M' and sexo != 'F':
    print('''Insira uma informação válida!
[M] Para masculino
[F] Para feminino''')
    sexo = str(input("Digite seu sexo [M/F]: "))
if sexo == 'F':
    print("Sexo Feminino!")
elif sexo == 'M':
    print("Sexo Masculino!")