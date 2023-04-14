#include <iostream>

/**Exercice 4 : Cr�er une classe Tableau. Le programme devra demander � l�utilisateur combien de valeurs sont �
traiter, il m�morise ensuite chaque valeur (ce seront des r�els simple pr�cision : float). La classe
comprend mis � part les constructeurs une m�thode moyenne() pour calculer la moyenne de ces valeurs
et l�afficher. Le programme propose ensuite de supprimer une des valeurs du tableau. L�utilisateur tape
une valeur num�rique qui est transmise � une m�thode enleveelement() qui supprime du tableau la
premi�re occurrence de cette valeur rencontr�e dans le tableau.
On consid�re qu�ici "supprimer" consiste � d�caler les �l�ments suivants du tableau d�un cran. Ainsi,
la valeur dispara�t du tableau. Si la fonction parvient � trouver la valeur indiqu�e par l�utilisateur (et
donc � l�enlever), elle renvoie la valeur bool�enne true et sinon la valeur false. En fonction du r�sultat
de la fonction, soit on recalcule la nouvelle moyenne une fois la valeur supprim�e, soit on affiche un
message signalant que la valeur ne faisait pas partie des �chantillons et que la moyenne n�a donc pas
chang�e.*/

using namespace std;

class Tableau{

    public :
        // Les attributs
        int tailleTab;  //Taille du tableau
        float *tab; // Le tableau

        // D�finition du constructeur Tableau
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
        void afficherTableau(); // M�thode surcharg�e

        float moyenne() //calculer la moyenne de ces valeurs et l�afficher
        {
            float somme = 0;  // Initialiser la somme � zero

            for(int i = 0;i <tailleTab ; i ++)
            {
                somme += tab[i];
            }
            // Afficher la moyenne si on le souhaite : Je pr�fere pas
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

void Tableau :: afficherTableau() // pr�ciser dans quel scope (Tableau) notre  fonction afficherTabelau se trouve.
{
    cout << "[ ";
    for (int i=0;i<tailleTab; i++){cout << tab[i] <<" ";}
    cout << "]" << endl;
}


int main()
{
    int tailleTableau = 4; // � modifi�
    Tableau Tab(tailleTableau); // on cree un objet de type Tableau de taille tailleTableau

    float element2strip;  // L'element que l'utilisateur souhaite supprimer
    bool isStiped;   // Le flag qui indique si l'element est supprimer ou pas

    cout << "Affichage du tableau : ";
    Tab.afficherTableau();
    cout << "La moyenne du tableau est egal a : moyenne =  " << Tab.moyenne() << endl;   // affichage de la moyenne
    cout << "Veuillez inserer la valeur numerique que vous souhaitez supprimer : ";
    cin >> element2strip;

    isStiped = Tab.enleveelement(element2strip);
    if (isStiped)   // si l'element � �t� trouve et supprim�
    {
        cout << "Affichage du tableau apres suppression de la premiere recurrence de "<<" element2strip : ";
        Tab.afficherTableau();
        cout << "La moyenne du tableau est egal a : moyenne =  " << Tab.moyenne() << endl;
    }
    else  // si l'�lement n'a pas �t� trouve
    {
        cout << "La valeur que vous souhaitez supprimer pas partie des echantillons de ce tableau, la moyenne reste donc inchangee." << endl;
    }

    return 0;
}
