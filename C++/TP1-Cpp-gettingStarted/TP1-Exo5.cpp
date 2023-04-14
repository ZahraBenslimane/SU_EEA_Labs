#include <iostream>
#include <math.h>

/**Exercice 5 : Réalisez une classe Equation2 permettant, comme son nom l’indique, de représenter et de traiter
informatiquement des équations du second degré. La classe devra permettre de saisir et d’afficher les
paramètres d’une équation du second degré ainsi que de calculer les solutions de l’équation.**/

using namespace std;

class Equation2{

    public :
        // Les attributs : equation ecrite sous la forme ax^2 + bx + c
        float a;
        float b;
        float c;

        float x1; // solution 1
        float x2; // solution 2

        // Définition du constructeur : Parametres à saisir par l'utilisateur
        Equation2()
        {
            cout << "Cette equation c'ecrit sous la forme ax^2 + bx + c" << endl;
            cout << "Veuillez introduir le parametre a: ";
            cin  >> a;
            cout << "Veuillez introduir le parametre b: ";
            cin  >> b;
            cout << "Veuillez introduir le parametre c: ";
            cin  >> c;
        }

        Equation2(float aTemp, float bTemp, float cTemp) // parametres du polynome à donner comme arguments
        {
        a = aTemp;
        b = bTemp;
        c = cTemp;
        }

        // Les methodes
        void afficherEquation2()  // Afficher le polynome
        {
           cout << "f(x) = ";
           cout << a <<"*x^2 ";
           if (b < 0){ cout << b <<  "*x";} else { cout << " +"<< b <<  "*x"; }
           if (c < 0){ cout << c << endl; } else { cout << " +"<< c << endl ; }

        }

        void solveEquation2()  // Resoudre l'quation du 2nd degree
        {
            float delta = b*b - 4*a*c; // calcul du descriminant
            cout << "delta = " << delta << endl; // Affichage du descriminant
            if (delta < 0)
            {
                cout << "L'equation ne possede pas de solution dans l'espace reel." << endl << endl;
            }
            else if (delta > 0)
            {
                x1 = (-b-sqrt(delta))/(2*a); // solution 1
                x2 = (-b+sqrt(delta))/(2*a); // solution 2
                cout << "L'equation possède deux solutions reelles : x1 = " << x1 << ", x2 = " << x2 <<endl<< endl;

            }
            else
            {
                // solution doubles
                x1 = -b/(2*a);
                x2 = -b/(2*a);
                cout << "L'equation possède une solution reelles double : x = " << x1  <<endl<< endl;
            }
        }
};

int main()
{

    Equation2 Eq(2,-9,-5);
    Eq.afficherEquation2();
    Eq.solveEquation2();

    Equation2 Eq2(1,1,1);
    Eq2.afficherEquation2();
    Eq2.solveEquation2();

    Equation2 Eq3(1,2,1);
    Eq3.afficherEquation2();
    Eq3.solveEquation2();

    cout << "Try it yourself ! " << endl;
    Equation2 Eq0;  // Overwrite du Constructeur par default // parametres à saisir par l'utilisateur
    Eq0.afficherEquation2();
    Eq0.solveEquation2();


    return 0;
}
