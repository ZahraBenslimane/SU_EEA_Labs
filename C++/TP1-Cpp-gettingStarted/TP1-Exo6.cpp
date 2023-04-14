#include <iostream>
#include <math.h>

/** EXO6 : Ecrire une classe Polynome, qui contient les param�tres d�un polyn�me d�un degr� n. Il serait int�ressant
de pouvoir r�aliser deux autres op�rations : int�grer et d�river. Ces op�rations cr�eront � partir d�un
polyn�me existant, un nouveau polyn�me r�sultat. A vous de proposer une d�claration de classe.**/

using namespace std;

class Polynome
{
    public:
        float* coefs; // les coeficients du polynome ecrits en BACKWARDS : le la valeur d'indice z�ro corespond au parametre de puissance x^0.
        int degre;    // Le degree du polynome creee

        // Le constructeur de la classe Polynome
        Polynome (int degrePolynome, bool toFill = true)  // Si on souhaite cree t saisir les parametre au moment de la creation, on laisse l'argument
                                                          // toFill = true, sinon si on souhaite cree un polynome vide ; on pose toFill = False
        {
            degre = degrePolynome ;  // Le degree du polynome est renseigner par l'utilisateur
            coefs = new float[degre +1] ; // On cree un array de taille degre+1
            if (toFill)  // si l'utilisateur souhaite saisir les parametre, on lui propose de les introduire.
            {
                cout << "Vuillez saisir les parametres du polynome BACKWARDS" << endl;
                for (int i=0 ; i <= degre ; i++)
                {
                    cout<< "le parametre *x^"<< i<< ":" ;
                    cin>> coefs[i] ;
                }
            }
        }

        Polynome getDerivee() // Methode qui calcule la d�rivee du polynome et renvoie un nouveau polynome resulant
        {
            Polynome polynomeDerive(degre-1, false); // On cree un polynome vide de degre inferieur
            for( int i=0;i<degre;i++)
                    polynomeDerive.coefs[i] = coefs[i+1]*(i+1);  //on realise la derivee de chaque parametre
            //polynomeDerive.afficherPolynome();
            return polynomeDerive; // on renvoie le polynome resulant
        }

        Polynome getIntegral() // Methode qui calcul l'integral d'un polynome
        {
            Polynome polynomeIntegral(degre+1, false); // On cree un polynome vide de degre superieur
            polynomeIntegral.coefs[0]=0; // Le dernier parametre constant nul
            for( int i=1;i<=degre+1;i++)
                    polynomeIntegral.coefs[i] = float(coefs[i-1])/float(i);
            //polynomeIntegral.afficherPolynome();
            return polynomeIntegral;
        }


        void afficherPolynome() // Methode qui affiche le polynome.
        {
            for(int i=degre;i>0;i--)
            {   // On regarde le signe du prochain parametre � afficher pour ajuster les signes.
                if (coefs[i-1] < 0){ cout << coefs[i] << "*x^" <<  i;} else { cout << coefs[i] << "*x^" <<  i << " + "; }
            }
            cout << coefs[0] << endl;
        }

        void deletePolynome()
        {
            delete [] coefs;  //On lib�re l'espace memoire alou�e

        }
};

int main()
{
    int degre = 2;  // A renseigner
    Polynome p(degre); // On appelle le constructeur avec toFill = true par d�fault
    cout << "\nLe polynome : f(x) = ";
    p.afficherPolynome();

    Polynome pDerivee = p.getDerivee();
    cout << "La derivee  : f'(x) = ";
    pDerivee.afficherPolynome();

    Polynome pIntegral = p.getIntegral();
    cout << "L'integrale : F(x) = ";
    pIntegral.afficherPolynome();


    p.deletePolynome();
    pDerivee.deletePolynome();
    pIntegral.deletePolynome();

    return 0;
}
