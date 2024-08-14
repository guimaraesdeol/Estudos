# include <stdio.h> // exercicio 7
int main()
{
    float metros, decimetros, centimetros, milimetros;
    printf("Escreva o valor em metros: ");
    scanf("%f",&metros);   
    decimetros = metros * 10;
    centimetros = decimetros * 10;
    milimetros = centimetros * 10;
    printf("=====================\n");
    printf("      Resultados     \n");
    printf("=====================\n");
    printf("Valor em decimetros: %.1f\n", decimetros);
    printf("Valor em centimetros: %.1f\n",centimetros);
    printf("Valor em milimetros: %.1f\n", milimetros);
}