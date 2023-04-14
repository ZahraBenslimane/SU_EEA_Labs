#ifndef CBasePile_h
#define CBasePile_h
#include <iostream>

// Commun:  afficharge - empilement - constructeur par copie ?

#define TAILLE_PILE 10

using namespace std;

class CBasePile
{

    int* pile{nullptr};
    int mMax;
	int mSommet;

    public:
        CBasePile(int n = TAILLE_PILE);
        ~CBasePile();
        void EmpilerElem(int a);

        CBasePile& operator< (const CBasePile& element);
        void operator>( int& stock);

        // Méthode d'affichage
        CBasePile& operator<<(const CBasePile& obj);
        void afficher(ostream &flux) const;

};

#endif // !1
