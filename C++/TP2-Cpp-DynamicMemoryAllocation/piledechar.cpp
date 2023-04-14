#include <iostream>
#include "piledechar.h"

using namespace std;


 PiledeChar :: PiledeChar( ) // Constructeur par d�fault
{
    cout << "The default constructor is called.\n";
    mMax = 100;
    mSommet = 0;
    mPile = new char [mMax]; // On alloue une pile de 100 cases
}

PiledeChar :: PiledeChar( unsigned int tailleMax )
{
    cout << "The constructor is called.\n"; // on peut aussi demander � l'utilisateur de saisir la taille maximum
    mMax = tailleMax;
    mSommet = 0;
    mPile = new char [mMax];
}

// Un constructeur par copie est une fonction qui initialise un objet avec un autre objet de meme classe
PiledeChar :: PiledeChar( const PiledeChar &obj)  // copy constructor
{
    // O
    cout << "The Copy constructor is called." << endl;
    mMax = obj.mMax;
    mSommet = obj.mSommet;
    mPile = new char[mMax];
    for (int i = 0; i < mSommet; i++)  // copy the values
	{
		mPile[i] = obj.mPile[i];
	}
}
// Destructeur
PiledeChar :: ~PiledeChar()
{
    cout << "\nFreeing the pile's memory!" << endl;
	delete[] mPile;
}

// M�thode qui retourne un entier positif qui correspond au nombre d��l�ments actuellement pr�sents dans la pile
int PiledeChar :: CompterElements()
{
    return mSommet -1;
}

// M�thode qui affiche entre des �[� et �]� les �l�ments actuellement pr�sents dans la pile
void PiledeChar :: AfficherPile()
{
    for(int i = 0; i< mSommet ;i++)
    {
        cout << "[ " << mPile[i] << "]";
    }
    cout << endl;
}

// Methode qui prend un caract�re en param�tre et le place sur le dessus dela pile.
void PiledeChar :: EmpilerElem(char charactere)
{
    if (mSommet >= mMax) { cout << "The pile if full,you can't stack anymore elements.\n" << endl; }
    else
    {
        mPile[mSommet] = charactere;
        mSommet ++; // Increment the next free memory place
	}
    //cout << "Element" << charactere << "Empil�." << endl;
}

// M�thode qui retourne les �l�ments dans l'orde inverse avec lequels ils on �taient empiler : LIFO (last in, first out)

char PiledeChar :: DesempilerElem()
{
    mSommet -= 1; // Note : pile[mSommet] est vide : on prends la pr�c�dente
    return mPile[mSommet] ;
}


