/** 
\mainpage Exemple d'utilisaiton de Doxygen

\author : Juste Un Petit Cours

\section INFO 
    On peut faire un petit blabla avec des sections et tout pour avoir une belle doc
\subsection INFO2 
    Et même des sous sections, comme ca tout le monde peut comprendre à quoi sert le code
    (bon ici c'est vrai il sert pas à grand chose)
    
\section Sérieusement
    Si on veut quand même expliquer à quoi sert ce code, ou plutot ce qu'il fait.
    Il permet d'illustrer le concept de fonction virtuelle pure et la notion de polymorphisme (si on veut faire un exo dessus).

\brief C'est juste un petit fichier c++ qui contient quelques classes pour 
        montrer que Doxygen peut faire des docs sympas.
**/


#include <iostream>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */


using namespace std;

/// La classe Periph est abstraiteet  définit de la manière la plus générale le fonctionnement d'un périphérique

class Periph {
public:
	/** 
         \fn double GetValue(int num) Fonction qui renvoie la valeur pour l'entree numéro num (par défaut 0)
         \param numéro de l'entrée 
         \return la valeur de de l'entrée
         **/
	virtual double GetValue(int num = 0) = 0;
	
        /// \fn fonction qui renvoie le nombre d'entree du peripherique
        /// \return le nombre d'entree
	unsigned int GetNumberValue() const
	{
		return nb_value;
	}
	
protected:
        /// stocke le nombre d'entree
	unsigned int nb_value;
};

/// Ce Periph ne renvoie qu'une valeur aléatoire (la valeur change à chaque appel)
class PeriphRandom : public Periph {
public:
	/// le constructeur
	PeriphRandom(){
		/// initialize random seed:
		srand (time(NULL));  
		nb_value = 1;
	}
	
	/// \fn la fonction virtuelle pure qu'on doit définir vu qu'on hérite de Periph
	virtual double GetValue(int num = 0)
	{
		return  (rand() % 1000 )/10 - 50;
	}
};

/// Ce Periph renvoie un nombre aléatoire de valeurs aléatoires  (on sait que ca sert à rien mais c'est pour l'exemple)
class PeriphRandomX : public Periph {
public:
	
        // le constructeur
	PeriphRandomX(){
		///  initialize random seed:
		srand (time(NULL));  
                /// On choisit aléatoire le nombre d'entrée
		nb_value = 1+ rand() % 10;
	}
	
	/// \fn la fonction virtuelle pure qu'on doit définir vu qu'on hérite de Periph
	virtual double GetValue(int num = 0)
	{
		return  (rand() % 1000 )/10 - 50;
	}
};

/// Ce Periph ne renvoie qu'une valeur qui est 42 (la réponse universelle bah oui !!)
class Periph42 : public Periph {
public:
	/// le constructeur
	Periph42(){
		nb_value = 1;
	}
	
	/// \fn la fonction virtuelle pure qu'on doit définir vu qu'on hérite de Periph
	virtual double GetValue(int num = 0)
	{
		return  42;
	}
};

/// Ici la fonction main qui n'utilse qu'un periph (et qu'il faudra modifier si on veut faire un exo dessus)
int main(int argc, char** argv)
{
	PeriphRandomX periph;

	for(int i=0;i<periph.GetNumberValue();i++)
		cout << "value : " << periph.GetValue(i) << endl;

    return 0;
}

