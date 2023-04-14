#include <iostream>

/**Exercice 2 :
On souhaite donner le même nom à trois fonctions. La première additionne deux entiers (type int), la
deuxième deux réels (type float) et la troisième deux tableaux de dix entiers. Ecrivez ces fonctions.
Montrer que les appels sont correctement réalisés. Question subsidiaire : Que se passe-t-il lorsqu’un
appel est fait avec comme arguments deux short. Pourquoi ?
**/

using namespace std;

int myAdder(int a, int b){ // additionne deux entiers (type int)
    return a+b;
}

float myAdder(float a, float b){ // additionne deux réels (type float)
    return a+b;
}

int* myAdder(int tabA[], int tabB[]){ // additionne deux tableaux de dix entiers
    int *tabRes = new int [10];
    for (int i=0;i<10;i++){
        tabRes[i] = tabA[i]+tabB[i]; // addition terme à terme
    }
    return tabRes;
}

int main()
{

    // à modifié
    int aInt = 1;
    int bInt = 2;

    float aFloat = 1.1;
    float bFloat = 2.2;

    int aTab[] = {1,1,1,1,1,1,1,1,1,1};
    int bTab[] = {2,2,2,2,2,2,2,2,2,2};
    int *tabRes;  // initialisation du tableau résulatant

    cout <<"First case  : addition of two entegers " << aInt  << " + " << bInt << " = " << myAdder (aInt, bInt) << endl;
    cout <<"Second case : addition of two floats "<< aFloat  << " + " << bFloat << " = " << myAdder (aFloat, bFloat) << endl;

    tabRes = myAdder(aTab, bTab);
    cout <<"Third case  : addition of two enteger arrays " << endl;
    cout << "[" ; for (int i =0; i<10; i++){ cout << aTab[i] << " ";} cout << "] "; cout << " + ";
    cout << "[" ; for (int i =0; i<10; i++){ cout << bTab[i] << " ";} cout << "]  = ";
    cout << "[" ; for (int i =0; i<10; i++){ cout << tabRes[i] << " ";} cout << "] " << endl;
    delete [] tabRes;

    short aShort = 1;
    short bShort = 2;
    /**L'adittion de deux shorts marche correctement car les shorts sont considérer des integers**/
    cout <<"Forth case  : addition of two shorts " << aInt  << " + " << bInt << " = " << myAdder (aShort, bShort) << endl;

    cout << "NOTE : The addition of the two shorts works correctly cbecause they are considered as integers." << endl;



    return 0;
}
