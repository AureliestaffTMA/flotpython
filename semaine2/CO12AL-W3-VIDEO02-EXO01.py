# -*- coding: iso-8859-15 -*-

## Il existe deux mani�res de cr�er un dictionnaire, la
## plus simple lorsque l'on cr�e un dictionnaire � la main
## est d'utiliser les accolades

d = {}

d = {'marc':35, 'alice':30, 'eric':38}

## la deuxi�me mani�re est tr�s utile lorsque les couples
## clefs valeurs sont obtenues par une op�ration, dans
## ce cas on peut automatiquement cr�er un dictionnaire
## � partir d'une liste de tuple clef,valeur

a = [('marc', 35), ('alice', 30), ('eric', 38)]
d = dict(a)

## je rappelle qu'il n'y a pas d'ordre dans un dictionnaire
## donc le dictionnaire n'affiche pas n�c�ssairement
## les valeurs dans l'ordre dans lesquels on les a entr�

print d

## il existe de tr�s nombreuse op�rations et fonctions
## sur les dictionnaires, nous allons voir les principales
## commen�ons par les deux suivantes

print len(d)
print 'marc' in d
print 'marc' not in d

## m�me si les dictionnaires ne sont pas des s�quences,
## dans un soucis d'uniformit� et de simplification,
## la fonction len et l'op�rateur in ont �t� impl�ment�
## sur les dictionnaires.

## on peut acc�der et modifier la valeur d'une clef de la
## mani�re suivante

print d['marc']
d['marc'] = 40

## on peut effacer une la clef et sa valeur dans le dictionnaire
## avec l'instruction del

del d['marc']

d.copy() # shallow copie du dictionnaire
print 

## et on a des m�thodes pour r�cup�rer les clefs dans une liste
## les valeurs dans une liste, et les tuples (clefs, valeur)
## dans une liste. 

print d.keys()
print d.values()
print d.items()
