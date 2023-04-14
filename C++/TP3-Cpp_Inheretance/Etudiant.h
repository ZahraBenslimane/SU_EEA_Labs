#ifndef Etudiant_h
#define Etudiant_h

#include "Personne.h"

#define NB_UES 5

// Définition des UE
#define CPP 0
#define ML 1
#define TI 2
#define AUTO 3
#define AUDIO 4

class Etudiant : public Personne{  // crée une classe Etudiant qui hérite de la class personne;
    float* notes{nullptr};
    public:
        // Constructors
        Etudiant();
        Etudiant(char* nom, char* prenom, unsigned   age, float* notes);
        // Destructors
        ~Etudiant();
        // Setters
        void setNote(float note, int UE);
        void setAllNotes(float* notes_param);
        // Getters
        float* getAllNotes();
        float getNote(int  UE);
        // Methods
        float moyenne();
        void afficheMoyenne();
        void afficher(ostream &flux) const;

};






#endif // Etudiant_h
