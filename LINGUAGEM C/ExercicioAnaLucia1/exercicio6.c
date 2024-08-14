#include <stdio.h> //  exercicio numero 6
int main()
{
    float valor, euro, peso, iene;
    printf("Qual o valor em reais (R$) para conversao? \nR: ");
    scanf("%f", &valor);
    euro = (valor/6);
    peso = (valor*171.04);
    iene = (valor*26.91);
    printf("==================\n");
    printf("TABELA CONVERTIDA\n");
    printf("==================\n");
    printf("Valor em euro: $%.2f\n", euro);
    printf("Valor em pesos argentinos: %.2f\n", peso);
    printf("Valor em ienes: %.2f\n", iene);
}