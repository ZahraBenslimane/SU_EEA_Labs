#include <iostream>

/**Exercice 4 : Créer une classe Tableau. Le programme devra demander à l’utilisateur combien de valeurs sont à
traiter, il mémorise ensuite chaque valeur (ce seront des réels simple précision : float). La classe
comprend mis à part les constructeurs une méthode moyenne() pour calculer la moyenne de ces valeurs
et l’afficher. Le programme propose ensuite de supprimer une des valeurs du tableau. L’utilisateur tape
une valeur numérique qui est transmise à une méthode enleveelement() qui supprime du tableau la
première occurrence de cette valeur rencontrée dans le tableau.
On considère qu’ici "supprimer" consiste à décaler les éléments suivants du tableau d’un cran. Ainsi,
la valeur disparaît du tableau. Si la fonction parvient à trouver la valeur indiquée par l’utilisateur (et
donc à l’enlever), elle renvoie la valeur booléenne true et sinon la valeur false. En fonction du résultat
de la fonction, soit on recalcule la nouvelle moyenne une fois la valeur supprimée, soit on affiche un
message signalant que la valeur ne faisait pas partie des échantillons et que la moyenne n’a donc pas
changée.*/

using namespace std;

class Tableau{

    public :
        // Les attributs
        int tailleTab;  //Taille du tableau
        float *tab; // Le tableau

        // Définition du constructeur Tableau
        Tableau( int taille)
        {
            tailleTab = taille;
            tab = new float[tailleTab];  // alouee dynamiquement un teableau de taille sasie par l'utilisateur
            cout <<"Creation d'un tableau de " << tailleTab << " cases...."<<endl;
            for (int i = 0;i <tailleTab; i++)
            {
                    cout << "Veuillez saisir la valeure de la case " << i << " : " ;  // Remplissage du tableau case par case
                    cin >> tab[i];
            }
        }

        // Les methodes
        void afficherTableau(); // Méthode surchargée

        float moyenne() //calculer la moyenne de ces valeurs et l’afficher
        {
            float somme = 0;  // Initialiser la somme à zero

            for(int i = 0;i <tailleTab ; i ++)
            {
                somme += tab[i];
            }
            // Afficher la moyenne si on le souhaite : Je prèfere pas
            //cout << "La moyenne du tableau est egal a " << somme/tailleTab <<endl;
            return somme/tailleTab;
        }

        bool enleveelement(float element) // argument : l'element que l'utilisateur souhaite supprimer du tableau
        {
            bool isInTab = false;

            for(int i=0;i< tailleTab; i++)
            {
                if (tab[i] == element && isInTab!= true ) // si l'element est trouve pour la premiere fois
                {
                    isInTab = true;  // on renvoie true
                    tailleTab -= 1;  // on modifie la valeur de l'attribut taille
                }
                if(isInTab == true ) // si l'elment est trouvee, on decale les valeur du tabelau d'un cran ; on recopie les valeurs suivantes
                {
                    tab[i]=tab[i+1];
                }
            }
            return isInTab;  // on indique si l'element est trouve ou pas
        }
};

void Tableau :: afficherTableau() // préciser dans quel scope (Tableau) notre  fonction afficherTabelau se trouve.
{
    cout << "[ ";
    for (int i=0;i<tailleTab; i++){cout << tab[i] <<" ";}
    cout << "]" << endl;
}


int main()
{
    int tailleTableau = 4; // à modifié
    Tableau Tab(tailleTableau); // on cree un objet de type Tableau de taille tailleTableau

    float element2strip;  // L'element que l'utilisateur souhaite supprimer
    bool isStiped;   // Le flag qui indique si l'element est supprimer ou pas

    cout << "Affichage du tableau : ";
    Tab.afficherTableau();
    cout << "La moyenne du tableau est egal a : moyenne =  " << Tab.moyenne() << endl;   // affichage de la moyenne
    cout << "Veuillez inserer la valeur numerique que vous souhaitez supprimer : ";
    cin >> element2strip;

    isStiped = Tab.enleveelement(element2strip);
    if (isStiped)   // si l'element à été trouve et supprimé
    {
        cout << "Affichage du tableau apres suppression de la premiere recurrence de "<<" element2strip : ";
        Tab.afficherTableau();
        cout << "La moyenne du tableau est egal a : moyenne =  " << Tab.moyenne() << endl;
    }
    else  // si l'élement n'a pas été trouve
    {
        cout << "La valeur que vous souhaitez supprimer pas partie des echantillons de ce tableau, la moyenne reste donc inchangee." << endl;
    }

    return 0;
}
