# -*- coding: iso-8859-15 -*-

## On peut cr�er un set de deux mani�res, soit avec un literal
## soit en passant une une liste comme argument de la
## fonction set

s1 = {1, 2, 3, 4, 4, 4, 5}

l = [3, 4, 8]
s2 = set(l)

print s1, s2

## on peut ajouter ou enlever des �l�ments d'un set
s1.add('spam')
s2.update([38, 9, 'egg'])
s2.remove(38)

## le test d'appartenance est sans surprise fait avec
## l'instruction in et not in

print 'spam' in s1
print 8 not in s1

print len(s1)

## je peux calcular la diff�rence, l'union et l'intersection
## de deux set

print s1 - s2
print s1 | s2
print s1 & s2

## il y a d'autres op�rations possibles sur les sets que je
## vous encourage � d�couvrir dans la documentation Python.

## pour finir vous pouvez cr�er un frozen set � partir
## d'un s�quence ou d'un set ainsi

fs = frozenset(s1)
print fs

