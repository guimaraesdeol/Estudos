//Crie um programa que contenha uma sub-rotina para validar a entrada de caracteres. Somente as letras “A”, “a”, “P” ou “p” são permitidas. Caso o usuário informe um caractere diferente, a função deve retornar falso e solicitar uma nova entrada. Informe ao usuário se o caractere foi aceito ou não.

#include <iostream>
using namespace std;

bool validaCaractere(char caractere);

int main(){ 
    char caractere;
    cout << "Digite um caractere: ";
    cin >> caractere;
    validaCaractere(caractere);
    while(true){
        if(validaCaractere(caractere)){
            cout << "Caractere aceito.";
            break;
        }else{
            cout << "Caractere invalido" << endl;
            cout << "Digite um caractere: ";
            cin >> caractere;
        }
    }



    return 0;
}

bool validaCaractere(char caractere){
    return(caractere == 'A' || caractere == 'a' || caractere == 'P' || caractere == 'p');
}