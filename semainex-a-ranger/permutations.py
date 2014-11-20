#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import math

class Permutations:
    """
    Un it�rateur qui �num�re les permutations de n
    sous la forme d'une liste d'indices commen�ant � 0
    """
    def __init__ (self, n):
        # le constructeur bien s�r ne fait (presque) rien
        self.n=n
        # le compteur va aller de 0 � n-1
        # puis comme �a en boucle sans fin
        self.counter=0
        # on se contente d'allouer un iterateur de rang n-1
        # si bien qu'une fois qu'on a fini de construire
        # l'objet d'ordre n on a n objets Permutations en tout
        if n>=2:
            self.subiterator=Permutations(n-1)

    # pour satisfaire le protocole de l'iterable
    def __iter__ (self):
        return self

    # c'est ici bien s�r que se fait tout le travail
    def next (self):

        # pour n ==1
        # le travail est tr�s simple
        if self.n==1:
            # on doit renvoyer une fois la liste [0]
            # car les indices commencent � 0
            if self.counter==0: 
                self.counter +=1
                return [0]
            # et ensuite c'est termin�
            else:
                raise StopIteration

        # pour n >= 2
        # lorsque counter est nul,
        # on traite la permutation d'ordre n-1 suivante 
        if self.counter==0:
            self.subsequence = self.subiterator.next()
        #
        # dans laquelle
        # on va ins�rer n 
        # � n places diff�rentes
        # on ins�re alors n (en fait n-1 car les indices commencent � 0)
        # successivement dans la sous-sequence � l'indice counter
        #
        # naivement on ecrirait
        # result = self.subsequence[0:self.counter] + [ self.n - 1 ] + self.subsequence [self.counter:self.n-1]
        # mais �a revient � mettre le nombre le plus �lev� en premier
        # et donc � it�rer les permutations dans le mauvais ordre,
        # en commen�ant par la fin
        #
        # donc on fait plut�t une sym�trie
        # pour ins�rer en commen�ant par la fin
        cutter = self.n-1 - self.counter
        result = self.subsequence[0:cutter] + [ self.n - 1 ] + self.subsequence[cutter:self.n-1]
        # 
        # on n'oublie pas de maintenir le compteur et de le remettre � z�ro
        # tous les n tours
        self.counter = (self.counter+1) % self.n
        return result

    # la longeur de cet it�rateur est connue
    def __len__ (self):
        return math.factorial(self.n)


# show the <max> first permutations - or all of them if max is None or False
def show_first_permutations  (n,max=None):
    iterator = Permutations (n)
    print "Il y a ",len(iterator),"permutations d'ordre",n
    counter=0
    for s in iterator:
        print s
        counter+=1
        if max and counter>=max:
            print '....'
            break

from argparse import ArgumentParser

def main ():
    parser=ArgumentParser()
    parser.add_argument("-f","--first",dest='max',default=None,type=int,help="list only the <N> first permutations")
    parser.add_argument("n",type=int)
    args=parser.parse_args()
    show_first_permutations (args.n, args.max)

if __name__ == '__main__':
    main()
