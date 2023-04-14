#include <iostream>
#include <cstring>
#include "piledechar.h"

/**Le but de ce TP est de r�aliser une classe structure de pile traitant des donn�es de type char. La
structure de pile sera implant�e sous forme d�une classe, appel�e PiledeChar*/

#define STACK_SIZE 80

using namespace std;
#define TAILLEMAX_MOT 100

//Fonction recevant en param�tre une pile et qui d�pile les lettres qui y sont contenues en les �crivant � l��cran au fur
void afficheinverse(PiledeChar registre)
{
    int tailleRegistre = registre.CompterElements();
    for (int i=0;i <= tailleRegistre;i++){cout << registre.DesempilerElem() << " ";}
    cout << endl;
}

// Fontion qui re�oit une instance de la classe PiledeChar en param�tre, qui cr�e une nouvelle pile nPile, d�pile les lettres une par
// une pour ensuite les rempiler en majuscule dans nPile.
PiledeChar inversemajuscule(PiledeChar registre)
{
    PiledeChar nPile = registre; //Constructeur par copie

    int taillePile = registre.CompterElements();
    for (int i = 0; i <= taillePile ; i++)
	{
		nPile.EmpilerElem(toupper(registre.DesempilerElem()));
	}
	nPile.AfficherPile();

    return nPile;
}


int main()
{
    cout << "This program lets us work with stacks with their 2 principal operations : Push and Pop ! \n\n";

    //Cr�er une instance de la classe PiledeChar
    //PiledeChar registre(STACK_SIZE);

     //Cr�er une instance de la classe PiledeChar par d�fault
    PiledeChar registre;

    // D�clarer un string
    string mot;

    // demander � l�utilisateur d�entrer un mot au clavier
    cout << "Please enter a word : ";

    // Le programme lit l�entr�e clavier
    getline(cin,mot);

    // D�clarer un tableau de caract�re
    char tabMot[mot.length()];

    // Affichage du mot introduit par l'utilisateur
    cout << "The introduced word : ";
    for (int i =0;i < mot.length();i++){ cout << mot[i];}

    //d�couper la cha�ne de caract�re lettre par lettre
    strcpy(tabMot, mot.c_str());

    // Affichage de la pile avec l'empilement des elements
    registre.AfficherPile();

    //Stocker les place dans la pile.
    cout << "\nStacking the letters one by one.." <<endl;
    for (int i =0;i < mot.length();i++)
    {
			registre.EmpilerElem(tabMot[i]);
			registre.AfficherPile();
    }

    cout << "\nTest of afficheinverse():" << endl;
    afficheinverse(registre);
    cout << "Make sure the originally declared pile is unchanged."<< endl;
    registre.AfficherPile();

    cout << "\nTest of inversemajuscule():" << endl;
    inversemajuscule(registre);

    cout << "Make sure the originally declared pile is unchanged."<< endl;
    registre.AfficherPile();




    return 0;
}
