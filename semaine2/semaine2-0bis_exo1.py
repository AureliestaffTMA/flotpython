# -*- coding: cp1252 -*-

## types de base en python
## les types num�riques
val_int = 1
val_float = 3.5 # attention, la virgule d�cimale est un point un Python

## on a les op�rations num�riques classiques, Python fait automatiquement
## les convertions si n�cessaire

print val_int + val_float
print val_int - val_float
print val_int * val_float
print val_int / val_float

## le type cha�ne de catact�res
val_str = 'une chaine'

## le type liste
val_list = [] # une liste vide, suite quelconque d'�l�ments index�s de 0 � n-1
val_list = [val_int, val_float, val_str]

print val_list[0] # premier �l�ment de la liste
print val_list[2]

## l'op�rateur + est d�finit pour les cha�nes de caract�res et les listes
## il retourne un nouvel objet de m�me type qui est la concat�nation
## des deux objets initiaux

print 'spam' + 'ham'

print [1, 2] + [3, 4]

## la liste est une structure de donn�e tr�s puissante et au coeur
## de tous les programmes Python. On verra plus tard cette semaine
## toutes les possibilit�s que l'on a avec une liste

