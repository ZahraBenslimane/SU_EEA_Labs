#include <iostream>

/** Exercice 01:
Définir un pointeur sur un entier, nommé p, un pointeur sur un entier constant, nommé q, un pointeur
constant sur un entier, nommé r. Faites des allocations avec l’opérateur new. Que constatez-vous ?
Définir un tableau de dix pointeurs sur des entiers. Faites une allocation de l’ensemble et une désallocation.
Vérifiez l’état de la mémoire. Définir une référence sur un entier, nommée s. Essayez toutes les
affectations entre p, q, r et s et expliquez les résultats obtenus.*/

using namespace std;

int main()
{
    // Définir un pointeur sur un entier, nommé p
    int pVal = 10;
    int* p =&pVal;

    // Définir un pointeur sur un entier constant, nommé q
    int const qVal = 20;
    //int  *q = &qVal;

    /**  NOTE : On ne peut pas définir un pointeur de type *int sur une variable de type int const */

    // Définir un pointeur constant sur un entier, nommé r
    int rVal = 30;
    int const *r =&rVal;

    cout << "La valeure : pVal = "<< pVal << "est dans l\'adresse memoire :" << p << endl;
    cout << "La valeure : rVal = "<< rVal << "est dans l\'adresse memoire :" << r << endl;

    // Allocation dynamique en mémoire d'un tableau de int avec l'opérateur "new"
    int *tabInt = new int [4];
    cout << "\nVeuillez introduire 5 variables entieres" << endl;
    for (int i=0;i<5;i++){
            cout << "Entier numero " << i << " : ";
            cin >> tabInt[i];
    }
    cout << "Le tableau introduit : ";
    for (int i=0;i<5;i++){
            cout << tabInt[i] << " ";
    }

    // Désalocation en mémoire du tableau
      delete [] tabInt ;


    // Define an array of ten pointers to integers
    int *var = new int [10];

    for (int i = 0; i < 10; i++) {
      var[i] = i;
    }
    cout << "\ntableau de dix pointeurs sur des entiers : " ;
    for (int i = 0; i < 10; i++) {
      cout << var[i] << " " ;
    }

    cout << "\n\nvariable a interieur du pointeur premiere case avant supression "  << var[0] << endl;
    delete [] var;
    cout << "variable a interieur du pointeur premiere case apres supression " << var[0] << endl;

    /** Note : On remarque que les pointeur en memoire pointe vers une variable utilisée ailleurs*/


    // Set a reference to an integer, named s. Try all the assignments between p, q, r and s and explain the results obtained
    int sVal = 5;
    int &s = sVal;

    cout << "\nAvant changement : sVal = " << sVal << endl;
    s = 6;
    cout << "Apres changement : sVal = " << sVal << endl;


    //s = r;  // reference sur un pointeur constant : IMPOSSIBLE
    //p = s;  // pointer vers une référence  : IMPOSSIBLE
    //s = p;  // stocker un pointeur dans une référence : IMPOSSIBLE
    //s = *p;  // stocker le contenue d'un pointeur dans une référence : OK


    return 0;
}
