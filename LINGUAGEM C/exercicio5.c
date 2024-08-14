# include <stdio.h>

int main()
{
    float qlatas, valor, lparede, aparede, area; // area = largura x altura
    // cada lata de tinta pinta 10 metros quadrados e custa 50 reais.
    printf("Qual a largura da parede? \nR: ");  \
    scanf("%f", &lparede);
    printf("Qual a altura da parede? \nR: ");
    scanf("%f", &aparede);
    area = lparede * aparede;
    qlatas = area / 10;
    valor = qlatas * 50;
    printf("Voce precisara de %.2f latas de tinta e o valor total sera de %.2f reais. \n", qlatas, valor);

}