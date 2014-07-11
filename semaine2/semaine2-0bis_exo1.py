# -*- coding: cp1252 -*-

## On va voir dans cette vid�o 4 types de base en Python, le type entier
## le type d�cimal, le type cha�ne de charact�res et le type liste.

## le type entier
## pour entrer un entier, on n'a rien d'autre � faire que d'�crire
## cet entier et de l'affecter � une variable
val_int = 1

## le type d�cimal
val_float = 3.5 # attention, la virgule d�cimale est un point un Python

## pour afficher la valeur d'un objet r�f�renc� par une variable,
## on utilise l'instruction print

print val_int

## on a les op�rations num�riques classiques sur les types num�riques
##(c'est-�-dire entier et decimal) et Python fait automatiquement
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

print 'spam' + 'egg'

print [1, 2] + [3, 4]

## la liste est une structure de donn�e tr�s puissante et au coeur
## de tous les programmes Python. On verra plus tard cette semaine
## toutes les possibilit�s que l'on a avec une liste

## 3 minutes 30 secondes

## maintenant que nous avons introduit certains types de base, j'aimerai
## vous parler d'une intruction tr�s importante qui permet d'ex�cuter ou
## de ne pas executer une portion de code en fonction d'une condition,
## c'est l'instruction if elif else. Passons maintenant dans un �diteur de texte...

