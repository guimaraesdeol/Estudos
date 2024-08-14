# include <stdio.h> //  ATIVIDADE 2 ANA LUCIA, ALUNO EDUARDO G OLIVEIRA

int main()
{
    int a1, a2, a3, soma;
    printf("Escreva o primeiro numero: ");
    scanf("%d", &a1);
    printf("Escreva o ultimo numero: ");
    scanf("%d", &a2);
    printf("Escreva a quantidade de termos: ");
    scanf("%d", &a3);
    soma = ((a1+a2)*a3)/2;
    printf("\n O resultado eh %d", soma);
}