#ifndef Personne_h
#define Personne_h


using namespace std;


class Personne{

    private:
        char *nom{nullptr};
        char *prenom{nullptr};
        unsigned int* age;
    public:
        // Constructors
        Personne();
        Personne(char* nom,char* prenom,unsigned int age);
        Personne( const Personne& obj);
        // Destructor
        ~Personne();
        // Setters
        void setAge(unsigned int age);
        void setNom(char* nom);
        void setPrenom(char* prenom);
        // Getters
        char const*  getNom()const;
        char const* getPrenom()const;
        unsigned int getAge() const;
        // Overloaded
        Personne& operator= (const Personne& someoneElse);
        // Méthode d'affichage
        void afficher(ostream &flux) const;

};

#endif // Personne_h
