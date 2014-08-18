# -*- coding: iso-8859-15 -*-

## Commen�ons pas sauvegarder notre �diteur dans un fichier
## finissant en .py, par exemple scope.py.
## Lorsque nous allons ex�cuter ce fichier
## (je vous rappelle que dans IDLE
## on peut simplement taper sur la touche F5, ou on
## peut en ligne de commande taper python scope.py)
## l'interpr�teur Python va transformer le code dans ce
## fichier en un objet module. 
## Toutes les variables d�finies dans
## ce fichier appartiennent au scope global de ce module
## sauf les variables d�finies dans les fonctions.

## Il y a deux notions importantes � comprendre lorsque
## l'on parle de variables. La premi�re notion est celle
## de scope qui explique comment les variables peuvent
## acc�der aux diff�rentes parties du code d'un m�me module.
## c'est ce que l'on va voir dans cette vid�o. La deuxi�me
## notion est celle d'espace de nommage qui explique
## comment acc�der aux variables d'autres modules et d'autres
## objets. C'est ce que l'on verra lorsque l'on parlera
## des modules un peu plus tard. En r�sum�, le scope
## concerne l'acc�s aux variables internes au module,
## et les espaces de nommage concernent l'acc�s
## aux variables entre les modules.

## cr�eons deux variables a et b
a, b = 1, 1

## c'est une variable globale parce que d�finie dans un module
## et en dehors d'une fonction. Toutes les variables globales
## sont acc�ssibles � tout le code d'un module.

for i in range(10):
    print a


## je d�finis maintenant une fonction f avec deux variables
## b et c. Comme elles sont d�finies dans la fonction,
## elle sont locales, c'est-�-dire cr��es uniquement �
## l'appelle de la fonction et d�truite lorsque la fonction
## retourne (c'est-�-dire lorsque l'on sort de la fonction)

def f():
    b, c = 2, 3
    print a, b, c

## lorsque je fais 'print a, b, c', comment l'interpr�teur
## sait quelle variable 'a' utiliser. C'est tr�s simple !
## la r�gle est de chercher d'abord la variable localement o�
## elle est utilis�e. Ici, c'est dans une fonction, donc
## on cherche 'a' localement dans la fonction,
## puis, si 'a' n'est pas trouv� dans le scope de la fonction,
## on cherche 'a' globalement, c'est-�-dire dans le module.
## Ici, a et b sont trouv�es localement c'est eux
## que l'on utilise. 

f()

## 'print a' cherche 'a' localement o� elle est utilis�e,
## c'est-�-dire dans le scope global du module. 
print b

## par contre, on ne peut pas faire print 'c', puisque
## 'c' est une variable locale � la fonction, donc pas acc�ssible
## en dehors de la fonction. De plus, les variables locales
## des fonctions sont cr��es � chaque appel de la fonction
## et d�truite lorsque la fonction retourne. 

#print c

## Les variables d�finies dans l'ent�te de la fonction sont
## �galement des variables locales

def f2(a):
    print a

f2(8)

print a

## mais gardons en t�te qu'utiliser localement dans une
## fonction un nom global est toujours une mauvaise id�e.
## En Python on doit utiliser des noms de variables explicites
## et nous verrons prochainement qu'utiliser localement
## un nom de variable globale peut conduire � des erreurs
## surprenantes.

## Maintenant, que ce passe-t-il si on d�finit une fonction
## dans une fonction.

a, b, c = 1, 1, 1
def g():
    b, c  = 3, 4
    def h():
        c = 5
        print a, b, c
    h()
g()

## Python va suivre dans ce cas une nouvelle r�gle. Lorsque
## l'on fait 'print a, b, c' dans la fonction h(),
## Python cherche les variables dans le scope local de h(),
## il trouve 'c' qui vaut 5, puis, et c'est la nouvelle r�gle,
## dans tous les scopes des fonctions englobante, c'est-�-dire
## des fonctions qui contiennent le bloc de code de h(),
## de la fonction la plus proche de h,
## jusqu'� la plus �loign�e. Python trouve 'b' qui vaut 3, 
## puis Python cherche dans le scope global et trouve 'a' qui
## vaut 1.

## r�sumons, le scope d'une variable est d�termin� par le bloc
## de code dans lequel est d�fini la variable. Il peut �tre
## local (dans une fonction) ou global (dans le module).
## Ensuite on cherche la d�finition d'une variable localement,
## puis dans le scope des fonctions englobantes, puis
## globalement. On appelle cette r�gle LEG.
