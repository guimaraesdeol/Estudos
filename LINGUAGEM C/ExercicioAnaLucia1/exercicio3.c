# include <stdio.h> //  ATIVIDADE 3 

int main()
{
    float fixo, vendas, comissao, salariof;
    printf("Digite o salario fixo: ");
    scanf("%f", &fixo);
    printf("Digite o valor das vendas: ");
    scanf("%f", &vendas);
    comissao = (vendas * 4/100);
    salariof = fixo + comissao;
    printf("================================= \n");  
    printf("A comissao eh R$%.2f \n", comissao);
    printf("O salario final eh R$%.2f \n", salariof);
    printf("=================================");
}