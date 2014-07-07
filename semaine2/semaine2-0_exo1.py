# -*- coding: cp1252 -*-

## Comment manipule-t-on des objets en Python ?
## On utilise l'affectation (typage dymamique).
## On dit que l'on affecte un nom � un objet ou que
## le nom r�f�rence l'objet. Parler du typage dynamique.

# abcdefghijklmnopqrstuvwxyz0123456789_
prix_articles = 10

## on ne commence pas par un chiffre

1prix = 10

## on ne met pas de caract�res accentu�s dans un nom de variable

carr�_val = 8

## types de base en python
val_int = 1
val_float = 3.5 # attention, la virgule d�cimale est un point un Python
val_str = 'une chaine'
val_list = [] # une liste vide, suite quelconque d'�l�ments index�s de 0 � n-1
val_list = [val_int, val_float, val_str]

print val_list[0] # premier �l�ment de la liste
print val_list[2]

## la liste est une structure de donn�e tr�s puissante et au coeur
## de tous les programmes Python. On verra plus tard cette semaine
## toutes les possibilit�s que l'on a avec une liste

