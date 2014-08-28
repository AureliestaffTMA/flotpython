# -*- coding: iso-8859-15 -*-

## Supposons que l'on veuille compter le nombre d'instances
## cr��es par une classe. On peut facilement maintenir un
## compteur du nombre de r�f�rence dans contructeur de la
## classe, mais l'acc�s � ce compteur n'est pas trivial.
## Regardons cela...


class C:
    nb_i = 0
    def __init__(self):
        C.nb_i  = C.nb_i + 1


C()
C()
## je peux �vidamment acc�der � l'attribut de la
## classe directement. 
print C.nb_i

## Je peux aussi faire une fonction dans mon module

def f():
    return C.nb_i


print f()

## Mais cela complique la maintenance d'avoir une fonction
## travaillant sur une classe en dehors de la classe.
## Par contre, je ne peux pas faire une m�thode d'instance
## dans ma classe puisqu'il me faut une instance pour acc�der
## au compteur, et que cette instance va changer le compteur
## � sa cr�ation.

## La solution ici est d'avoir une m�thode statique.
## une m�thode statique s'�crit comme une fonction,
## mais doit �tre d�clar�e comme statique avec la
## fonction staticmethod. 

class C:
    nb_i = 0
    def __init__(self):
        C.nb_i  = C.nb_i + 1
    def f():
        return C.nb_i
    f = staticmethod(f)

C()
C()
print C.f()

## notons qu'une m�thode statique peut aussi �tre appel�e sur
## une instance, mais que l'instance n'est pas pass�e � la
## m�thode

print C().f()
