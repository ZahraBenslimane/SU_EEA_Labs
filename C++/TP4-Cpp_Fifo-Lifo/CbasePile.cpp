#include "CBasePile.h"


CBasePile :: CBasePile(int n)
{
    cout << "The constructor is called." << endl;
	if (n > 0)
		mMax = a;
	else
		mMax = TAILLE_PILE;

	mSommet = 0;
	pile = new int[mMax];
}

CBasePile :: ~CBasePile()
{
    delete []pile;
	cout << "Deconstruction done." << endl;
}

void CBasePile::EmpilerElem(int element)
{
	if (mSommet >= mMax) { cout << "You can not stack anymore elements, the pile is full." << endl; }
	else
	{
		pile[mSommet] = element;
		mSommet += 1;
	}
}

CBasePile& CBasePile::operator<( int element){
	EmpilerElem(element);
	return *this;
}


ostream& operator<<(ostream& flux,CBasePile const& p)
{
    for(int i =0;i <p.mSommet;i++){flux << p.pile[i] << " ";}
    return flux;
}
