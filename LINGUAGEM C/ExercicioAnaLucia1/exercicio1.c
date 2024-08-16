# include <stdio.h> // EXERCICIO NUMERO 1 
int main()
{
    float lquintal, cquintal, lpiscina, cpiscina, areaquintal, areapiscina, arealivre;
    printf("Qual a largua do quintal? \nR: ");
    scanf("%f", &lquintal);
    printf("Qual o comprimento do quintal? \nR: ");
    scanf("%f", &cquintal);
    printf("Qual a largura da piscina? \nR: ");
    scanf("%f", &lpiscina);
    printf("Qual o comprimento da piscina? \nR: ");
    scanf("%f", &cpiscina);

    areaquintal = lquintal * cquintal;
    areapiscina = lpiscina * cpiscina;
    arealivre = areaquintal - areapiscina;

    printf("A area do quintal e %f \n", areaquintal);
    printf("A area da piscina e %f \n", areapiscina);
    printf("A area da livre e %f \n", arealivre );
     // TESTESTESTEWTSA


}