#include <iostream>

/** Exercice 01:
D�finir un pointeur sur un entier, nomm� p, un pointeur sur un entier constant, nomm� q, un pointeur
constant sur un entier, nomm� r. Faites des allocations avec l�op�rateur new. Que constatez-vous ?
D�finir un tableau de dix pointeurs sur des entiers. Faites une allocation de l�ensemble et une d�sallocation.
V�rifiez l��tat de la m�moire. D�finir une r�f�rence sur un entier, nomm�e s. Essayez toutes les
affectations entre p, q, r et s et expliquez les r�sultats obtenus.*/

using namespace std;

int main()
{
    // D�finir un pointeur sur un entier, nomm� p
    int pVal = 10;
    int* p =&pVal;

    // D�finir un pointeur sur un entier constant, nomm� q
    int const qVal = 20;
    //int  *q = &qVal;

    /**  NOTE : On ne peut pas d�finir un pointeur de type *int sur une variable de type int const */

    // D�finir un pointeur constant sur un entier, nomm� r
    int rVal = 30;
    int const *r =&rVal;

    cout << "La valeure : pVal = "<< pVal << "est dans l\'adresse memoire :" << p << endl;
    cout << "La valeure : rVal = "<< rVal << "est dans l\'adresse memoire :" << r << endl;

    // Allocation dynamique en m�moire d'un tableau de int avec l'op�rateur "new"
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

    // D�salocation en m�moire du tableau
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

    /** Note : On remarque que les pointeur en memoire pointe vers une variable utilis�e ailleurs*/


    // Set a reference to an integer, named s. Try all the assignments between p, q, r and s and explain the results obtained
    int sVal = 5;
    int &s = sVal;

    cout << "\nAvant changement : sVal = " << sVal << endl;
    s = 6;
    cout << "Apres changement : sVal = " << sVal << endl;


    //s = r;  // reference sur un pointeur constant : IMPOSSIBLE
    //p = s;  // pointer vers une r�f�rence  : IMPOSSIBLE
    //s = p;  // stocker un pointeur dans une r�f�rence : IMPOSSIBLE
    //s = *p;  // stocker le contenue d'un pointeur dans une r�f�rence : OK


    return 0;
}
