# -*- coding: latin_1 -*-

## une liste est une s�quence, donc toutes les fonctions et op�rations
## que l'on a vues pour les s�quences s'appliques aux listes : en particulier
## testes d'appartenance in, not in ; concat�nation avec le signe + ;
## longeur avec la fonction built-in len ; r�cup�ration d'un �l�ment
## par son index entre crochet ; et le slicing.

## on cr�e une liste vide ainsi
l = []

## on s�pare les �l�ments d'une liste par des virgules
## notons que l'on peut directement mettre un objet dans
## la liste, ou utiliser une variable r�f�rencant l'objet

i = 4

l = [i, 'spam', 3.2, True]

print l[0]

l[0] = 20

print l

## on peut �galement directement effectuer une op�ration et r�affecter
## cette op�ration � un �l�ment de la liste. Je rappelle qu'en Python
## on �value d'abord ce qu'il y a � droite du signe �gal et ensuite
## on affecte le r�sultat � la variable de gauche.

l[0] = l[0] + 1

print l

## on peut utiliser le slicing dans une liste parce que c'est
## une s�quence

print l[1:2]

## mais comme une liste est mutable on peut affecter sur slice

l[1:2] = ['egg', 'beans']

print l

## il faut bien comprendre ce que fait cette op�ration. Python commence
## par effacer les �l�ments sp�cifi�s par le slide dans l, puis il va
## ajouter les �l�ments de la liste de droite � la place. S'il y a plus
## d'�l�ments la liste est agrandie, s'il y en a moins, elle est raccoucie

## on peut donc supprimer des �l�ments sur un slice en affectant un slice � une
## liste vide

l[1:2] = []

print l

## je peux �galement utiliser l'instruction del pour effacer tous les �l�ments
## sp�cifi�s dans un slice

del l[0:3:2]

print l

## par contre s'il on �crit L[1] = ['spam', 'good'], on va simplement ajouter
## une liste � la position 1 de la liste l

l[1] = ['spam', 'good']

print l

## avant de continuer, sur les fonctions sp�cifiques aux listes, je vais
## introduire la fonction built-in range() qui permet d'obtenir une liste
## d'entiers.

print range(10)

print range(1, 10)

print range(1, 10, 2)

## Regardons maintenant les 7 fonctions qui permettent de modifier
## les listes en place.

l = range(10)

l.append('spam')
print l

l.extend([11, 12])
print l

## insert l'objet juste avant la position, mais n'efface et ne remplace rien
l.insert(2, 'egg')
print l

l.sort() # attention sort ne retourne pas la liste, mais la modifie en place
print l

l.reverse()
print l

print l.pop()

print l.pop(2)

print l

l.remove(5) # efface la premiere occurence de l'�l�ment pass� en parametre

## 8 minutes
