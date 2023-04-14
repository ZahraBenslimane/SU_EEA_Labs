#include <iostream>
#include <cstring>

#include "Personne.h"
#include "Etudiant.h"

#define N 6

using namespace std;

ostream& operator<<(ostream& flux,Personne const& p)
{
    p.afficher(flux);
    return flux;
}

ostream& operator<<(ostream& flux,Etudiant const& etu)
{
    etu.afficher(flux);
    return flux;
}

int main()
{
    cout << " ** Note ** : In this Lab, I chosed to assign All the values,\nand not give the user the ability to assign them in order to be more practical." << endl;
    cout << "----------------------------------------------------\n" << " ****  Personne's Default Constructor  ****\n" << endl;

    Personne None;
    cout << None;

    cout << "\n----------------------------------------------------\n" << " ****  Personne's  parametrized constructor ****\n" << endl;
    Personne nobody("Benslimane","Zahra",22);
    cout << nobody << endl;

    cout << "\n----------------------------------------------------\n" << " ****  Test Array of Personne  *****\n" << endl;
    cout << "----- Before creating tabPersonne ----" << endl;
    // allocating dynamic array of Size N using new keyword
    Personne* tabPersonne = new Personne[N];
    cout << "----- After creating tabPersonne  ----" << endl;

    char* names[] = {"Din","Fett","Skywalker"};
    char* firstNames[] = {"Djarin","Boba","Luke"};
    unsigned int ages [] = {35,55,25};

    cout << "\nInstanciating different objetcs with parameters or Leaving them as default: " << endl;
    int cpt = 0;
    // calling constructor for each or other index of array
    for (int i = 0; i < N; i++) {
            if(i%2 == 0){                                // if the index is even i instanciate a known object otherwise leave it as default
                tabPersonne[i].setNom(names[cpt]);
                tabPersonne[i].setPrenom(firstNames[cpt]);
                tabPersonne[i].setAge(ages[cpt]);
                cpt +=1;
        }
    }

    // printing contents of array
    for (int i = 0; i < N; i++) { cout << tabPersonne[i]; }
    cout << "\n-----------------------------------------------------------\n" <<  " ******  Destruction of Array of Personne ******\n" << endl;
    // Destructor of the array
    delete [] tabPersonne;

    cout << "\n-----------------------------------------------------------\n"  << " ******  Test Copy Constructor   ******\n" << endl;
    Personne moi(nobody);
    cout << nobody << endl;

    cout << "\n-----------------------------------------------------------\n"  << " ******  Test OVERLOADING operator= ******\n" << endl;
    Personne obj;
    obj = moi;
    cout << moi << endl;
    cout << "\n-----------------------------------------------------------\n"  << " ******  Test class ETUDIANT ******\n" << endl;

    float notes[] = {1,2,3,4,5};
    //  Constructor
    Etudiant grogu("Baby", "grogu",22 , notes);
    cout << grogu;

    cout << "\n-----------------------------------------------------------\n"  << " ******  Test Tableau ETUDIANT ******\n" << endl;
    Etudiant* tabEtudiant = new Etudiant[3];
    float myNotesTab[3][5] = {{1,1,1,1,1},{2,2,2,2,2},{3,3,3,3,3}};
    for (int i = 0; i < 3; i++)
    {
        tabEtudiant[i].setNom(names[i]);
        tabEtudiant[i].setPrenom(firstNames[i]);
        tabEtudiant[i].setAge(ages[i]);
        tabEtudiant[i].setAllNotes(myNotesTab[i]);
    }
    // Printing the Etudiant array
    for (int i = 0; i < 3; i++) { cout << tabEtudiant[i]; }
    cout << "\n-----------------------------------------------------------\n"  << " ******  Test methode Moyenne ******\n" << endl;
    for (int i = 0; i < 3; i++)
    {
        tabEtudiant[i].afficheMoyenne();
    }
    cout << "\n-----------------------------------------------------------\n"  << " ******  Test getNote & setNote ******\n" << endl;
    cout << "Let's take Boba fett as an exemple.\n He got a +10 bonus in C++, so lets change it\n";
    cout << "\nBoba fett before calling getNote & setNote " << endl;
    cout <<  tabEtudiant[1];
    // getting his C++ score
    float note1 = tabEtudiant[1].getNote(CPP);
    // Setting his new cpp score
    tabEtudiant[1].setNote(note1+10,CPP);
    cout << "\nBoba fett After changing his score." << endl;
    cout <<  tabEtudiant[1];
    tabEtudiant[1].afficheMoyenne();


    cout << "\n-----------------------------------------------------------\n"  << " ******  Destruction of Array of Etudiant's objects ******\n" << endl;
    delete [] tabEtudiant;
    cout << "\n-----------------------------------------------------------\n"  <<  endl;

    return 0;
}
