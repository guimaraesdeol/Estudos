num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte',)
pessoa = int(input('Digite um número entre 0 e 20: '))
while (pessoa > 20) or (pessoa < 0):
    pessoa = int(input('Digite um número entre 0 e 20: '))
print(f'O número {pessoa} em extenso é {num[pessoa]}')
