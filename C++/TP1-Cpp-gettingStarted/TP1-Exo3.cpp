#include <iostream>

/** Exercice 03 : On déclare trois nombres réels a, b, c (float) dans le main(), et on leur attribue des valeurs arbitraires,
par exemple a=10.5, b=-5.3 et c=-0.2. On désire écrire une fonction ordonnetrois (à définir) qui puisse manipuler ces trois
variables passées en paramètre et les ordonner par ordre croissant en permutant leurs valeurs.
Afin de simplifier le problème, on décide d’écrire d’abord une fonction ech2paradresse() qui effectue le tri sur seulement deux paramètres
à la fois, et dont on se sert pour ensuite écrire ordonnetrois(). Dans cet exercice, vous utiliserez lorsque c’est nécessaire un passage
de paramètres par adresse. On reprend la même question mais on décide d’utiliser des passages par
référence.**/

using namespace std;


// Passage par adresse
void ech2paradresse(float *a,float *b){
    float spare = *a;  // on suppose que a est le plus petit
    if(*a > *b){
        *a = *b;
        *b = spare;
    }
}

// Passage par référence
void ech2paradresse(float &a, float &b){
    float spare = a;  // on suppose que a est le plus petit
    if(a > b){
        a = b;
        b = spare;
    }
}

// Passage par adresse
void orderthree (float *a, float *b, float *c){
    if( *a > *c ){
        ech2paradresse(a,c);
    }
    if( *a > *b ){
        ech2paradresse(a,b);
    }
    if( *b > *c ){
        ech2paradresse(b,c);
    }
}

// Passage par référence
void orderthree (float &a, float &b, float &c){
    if( a > c ){
        ech2paradresse(a,c);
    }
    if( a > b ){
        ech2paradresse(a,b);
    }
    if( b > c ){
        ech2paradresse(b,c);
    }
}


int main()
{
    float a = 10.5;
    float b = -5.3;
    float c = -0.2;

    float a2 = 10.5;
    float b2 = -5.3;
    float c2 = -0.2;

    float &ra = a2;
    float &rb = b2;
    float &rc = c2;


    cout << "Appel par adresse : " << endl;
    cout << "Avant appel de la fonction : " << "a = " << a << ",b = " << b << ",c = " << c << endl;
    orderthree ( &a, &b, &c);
    cout << "Apres appel de la fonction : " << "a = " << a << ",b = " << b << ",c = " << c << endl;


    cout << "\nAppel par reference : " << endl;
    cout << "Avant appel de la fonction : " << "a = " << a2 << ",b = " << b2 << ",c = " << c2 << endl;
    orderthree ( ra, rb, rc);
    cout << "Apres appel de la fonction : " << "a = " << a << ",b = " << b << ",c = " << c << endl;


    /** Remarque : Nous pouvons  confirmer que le passage par référence est efficace  car tout en ayant les
                   mêmes avantages que le passage d'un pointeur nous conservons la syntaxe du passage par valeur
                   Ce qui peut nous faciliter les choses quand les fonctions changent de signatures et que nous voullions pas
                   forcement changer tout le code **/


    return 0;
}
