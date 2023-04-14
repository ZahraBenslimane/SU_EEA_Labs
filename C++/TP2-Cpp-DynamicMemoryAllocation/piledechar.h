#ifndef piledechar_h
#define piledechar_h


class PiledeChar{

    private:

        unsigned int mMax;   // mMax contient la taille de la pile créée
        unsigned int mSommet;   // La donnée membre mSommet indique le numéro de la case vide dans laquelle on pourra empiler le prochain caractère
        char *mPile;  // Le tableau de caractères, alloué dynamiquement

    public:
        PiledeChar();// Default constructor
        PiledeChar( unsigned int tailleMax );
        PiledeChar( const PiledeChar &obj);  // copy constructor
        int get_mSommet(); //Getter
        ~PiledeChar(); // Desctructeur
        int CompterElements(); // retourne Nb éléments dans la pile
        void AfficherPile();   // Affiche notre pile
        void EmpilerElem(char charactere); //stack des caractères
        char DesempilerElem(); // retourne les caractères

};

#endif // piledechar_h
