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