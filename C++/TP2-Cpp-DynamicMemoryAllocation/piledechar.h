#ifndef piledechar_h
#define piledechar_h


class PiledeChar{

    private:

        unsigned int mMax;   // mMax contient la taille de la pile cr��e
        unsigned int mSommet;   // La donn�e membre mSommet indique le num�ro de la case vide dans laquelle on pourra empiler le prochain caract�re
        char *mPile;  // Le tableau de caract�res, allou� dynamiquement

    public:
        PiledeChar();// Default constructor
        PiledeChar( unsigned int tailleMax );
        PiledeChar( const PiledeChar &obj);  // copy constructor
        int get_mSommet(); //Getter
        ~PiledeChar(); // Desctructeur
        int CompterElements(); // retourne Nb �l�ments dans la pile
        void AfficherPile();   // Affiche notre pile
        void EmpilerElem(char charactere); //stack des caract�res
        char DesempilerElem(); // retourne les caract�res

};

#endif // piledechar_h
