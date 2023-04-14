#include <iostream>
#include <cstring>

using namespace std;

#include "Etudiant.h"


Etudiant :: Etudiant() : Personne()
{
    cout << "Etudiant's default constructor is called." <<endl;
    notes     = new float[NB_UES];
}

Etudiant :: Etudiant(char* nom_param, char* prenom_param, unsigned int age_param, float* notes_param) : Personne(nom_param,prenom_param,age_param)
{
    cout << "Etudiant's constructor is called for " << nom_param << "."<< endl;
    notes     = new float[NB_UES];
    // Affecter les notes une par une
    for(int i=0;i<NB_UES;i++) { notes[i] = notes_param[i]; }
}

// Destructor
Etudiant :: ~Etudiant()
{
    cout << "Etudiant's deconstructor is called for the derived object " << this->getNom() <<" " << this->getPrenom() << "." <<endl;
    delete [] notes; notes = nullptr;
    // The base class (personne) dectructor is called implecitly
}

// Getter and setter of all scores
float* Etudiant :: getAllNotes(){return this->notes;}
void Etudiant :: setAllNotes(float* notes_param)
{
    for(int i=0;i<NB_UES;i++){notes[i] = notes_param[i];}
}

// Getter and setter of a unique score
float Etudiant :: getNote(int UE){return notes[UE];}
void  Etudiant :: setNote(float note, int UE){notes[UE] = note;}

// Methode who computes the average score  of a student
float Etudiant :: moyenne()
{
    float somme = 0;
    for (int i =0;i<NB_UES; i++)
    {
        somme += notes[i];
    }
    return somme/NB_UES;
}

void Etudiant :: afficher(ostream &flux) const
{
    cout << "--------------------------------------" << endl;
    cout << "Last Name  : "<< this->getNom() << endl;
    cout << "First Name : "<< this->getPrenom() <<  endl;
    cout << "Age        : "<< this->getAge() << endl;
    cout << "Notes      : [ ";
    for (int i =0; i< NB_UES; i++ ){
            cout << "{" << notes[i] << "} "; }
    cout <<"]" << endl;

}

void Etudiant :: afficheMoyenne()
{
    cout << this->getPrenom() << " "<< this->getNom() << " has an average score of : "  << this->moyenne() << endl;
}


