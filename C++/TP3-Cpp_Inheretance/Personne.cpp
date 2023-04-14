#include <iostream>
#include <cstring>
#include "Personne.h"

#define SIZE_MAX 100

using namespace std;

Personne :: Personne()
{
    cout << "Personne's default constructor is called." << endl;
    nom     = new char[SIZE_MAX];
    prenom  = new char[SIZE_MAX];
    age     = new unsigned int(0);

    strcpy(nom,"NONE");
    strcpy(prenom, "none");

}

Personne :: Personne(char *nom_param, char *prenom_param, unsigned int age_param)
{
    cout << "Personne's Constructor is called for " << nom_param <<  endl;
    // Dynamically allocate space for each attribute on the Heep
    nom     = new char[strlen(nom_param)];
    prenom  = new char[strlen(prenom_param)];
    age     = new unsigned int(age_param);

    // Assign the constructor parameters to the attributes
    strcpy(nom,nom_param);
    strcpy(prenom, prenom_param);
}

// Constructeur par copie
Personne :: Personne( const Personne& obj)
{
    cout << "The Copy Constructor is called." << endl;
    nom     = new char[strlen(obj.nom)];
    prenom  = new char[strlen(obj.prenom)];
    age     = new unsigned int (*obj.age);

    strcpy(nom ,obj.nom);
    strcpy(prenom,obj.prenom);

}

// Deconstructor
Personne :: ~Personne()
{
    cout << "Personnes's deconstructor is called for " << prenom <<" " <<   nom << "....";
    delete []nom;     nom    = nullptr;
    delete []prenom;  prenom = nullptr;
    delete  age;      age    = nullptr;
    cout << "Destruction is done." <<endl;

}

// Setters
void Personne :: setNom(char* nom_param){strcpy(nom,nom_param);}
void Personne :: setPrenom(char* prenom_param){strcpy(prenom,prenom_param);}
void Personne :: setAge(unsigned int age_param){ *(this->age) = age_param;}

// Getters
char const* Personne :: getNom()const {return nom;}
char const* Personne :: getPrenom() const {return prenom;}
unsigned int Personne :: getAge() const {return *age;}


// Overloading operator=
Personne& Personne::operator= (const Personne& someoneElse)
{
	// self-assignment check  : self-assignment causes each member to be assigned to itself
	if (this == &someoneElse)
		return *this;

    *age = someoneElse.getAge();

    strcpy(nom,someoneElse.getNom());
    strcpy(prenom,someoneElse.getPrenom());

	// return the existing object so we can chain this operator    // as f1 = f2 = f3; // chained assignment
	return *this;
}

void Personne :: afficher(ostream &flux) const
{
    cout << "------------------------" << endl;
    cout << "Last Name  : "<< nom << endl;
    cout << "First Name : "<< prenom <<  endl;
    cout << "Age        : "<< *age << endl;
}



