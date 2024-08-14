# include <stdio.h> //  ATIVIDADE 4 ANA LUCIA, ALUNO EDUARDO G OLIVEIRA

int main()
{
    float tempo, velocidade, distancia, litros;
    printf("Qual sera o tempo em horas gasto na viagem? \nR: ");
    scanf("%f", &tempo);
    printf("Qual sera a velocidade KM/H durante a viagem? \nR: ");
    scanf("%f", &velocidade);
    distancia = (tempo * velocidade);
    litros = (distancia/12);
    printf("A distancia da viagem sera de %.1f km. \n", distancia);
    printf("Voce precisara de %.2f litros de combustivel. \n", litros);
}