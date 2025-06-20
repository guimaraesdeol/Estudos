//Faça um programa que tenha uma sub-rotina que receba dois números inteiros. A sub-rotina deve calcular e exibir a soma dos dois números, além da subtração e da divisão do maior pelo menor. Certifique-se de que os números informados não sejam iguais.

#include <iostream>
using namespace std;

float calcular(int num1, int num2);

int main(){
    int num1, num2;
    while(true){
        cout<<"Digite o primeiro numero inteiro: ";
        cin>>num1;
        cout<<"Digite o segundo numero inteiro: ";
        cin>>num2; 
        if(num1 != num2){
            break;
        }else{
            cout<< "Os numeros nao podem ser iguais." << endl;
        }
    }
    calcular(num1, num2);



}

float calcular(int num1, int num2){
    //Soma
    cout << "Soma: " << num1+num2 << endl;
    cout << "Subtracao: " << num1-num2 << endl;
    if(num1>num2){
        cout << "Divisao: " << num1/num2 << endl;
    }else{
        cout << "Divisao: " << num2/num1 << endl; 
    }
    return 0;
}