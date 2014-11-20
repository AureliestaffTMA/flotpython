#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import itertools

class Permutations:
    """
    Un it�rateur qui �num�re les permutations de n
    sous la forme d'une liste d'indices commen�ant � 0
    """
    def __init__(self, n):
        self.n = n
        # on commence � ins�rer � la fin 
        self.cycle = itertools.cycle (range(n)[::-1])
        if n >= 2:
            self.subiterator = Permutations(n-1)
        # pour savoir quand terminer le cas n==1
        if n == 1:
            self.done = False

    def __iter__(self):
        return self

    def next(self):
        cutter = self.cycle.next()

        # quand n==1 on a toujours la m�me valeur 0
        if self.n == 1:
            if not self.done:
                self.done = True
                return [0]
            else:
                raise StopIteration

        # au d�but de chaque s�quence de n appels
        # il faut appeler une nouvelle sous-s�quence
        if cutter == self.n-1:
            self.subsequence = self.subiterator.next()
        # dans laquelle on ins�re n-1
        return self.subsequence[0:cutter] + [ self.n - 1 ] \
                 + self.subsequence[cutter:self.n-1]

    # la longeur de cet it�rateur est connue
    def __len__(self):
        import math
        return math.factorial(self.n)

    
# show the <max> first permutations - or all of them if max is None or False
def show_first_items  (iterable, nb_items=None):
    print "Il y a {} items dans l'iterable".format(len(iterable))
    counter = 0
    for item in iterable:
        print item
        counter += 1
        if nb_items and counter >= nb_items:
            print '....'
            break

from argparse import ArgumentParser

def main ():
    parser=ArgumentParser()
    parser.add_argument("-f","--first",dest='max',default=None,type=int,help="list only the <N> first permutations")
    parser.add_argument("n",type=int)
    args=parser.parse_args()
    show_first_items (Permutations(args.n), args.max)

if __name__ == '__main__':
    main()
