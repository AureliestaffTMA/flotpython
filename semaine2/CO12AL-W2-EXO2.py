# -*- coding: latin_1 -*-

## Je vous rappelle que Python utilise le typage dynamique, c'est-�-dire
## que l'on ne donne jamais le type d'un objet � l'�criture du programme,
## ce type est d�termin� � l'execution. �a simplifie beaucoup l'�criture
## des programmes.

## le type entier
## pour entrer un entier, on n'a rien d'autre � faire que d'�crire
## cet entier
1

## on peut �galement l'affecter � une variable
i = 1

## Comment on connait le type d'un objet en Python ?
## On utilise la fonction built-in type() qui accepte comme
## argument une variable ou un objet. 

type(i)

## en python on a deux type entiers, les int et les long
i = 10 ## cod� sur 32 bits sur une machine 32 bits
l = 23480284028402840289482184018 # pr�cision illimit�e
print l * l     # pr�cision illimit�e sur les long

## pourquoi avons nous deux types entier en Python ?
## le type int est plus compact que le type long, par cons�quent
## pour les petits entier, Python va utiliser le type int pour reduire
## la consommation m�moire, et le type long s'il y a vraiement besoin de
## grands entiers.

## heureusement, Python fait automatiquement la conversion
## de int vers long s'il y a besoin. Donc en pratique vous n'avez
## jamais � vour pr�ocup� du type d'entier que vous utilisez

type(i + l)     

## Les d�cimaux. On s�pare la partie enti�re et d�cimale par un .
f = 4.3

## les float sont en g�n�ral �quivallent aux double en C,
## c'est � dire que ce sont des nombres cod�s sur 53 bits
## avec un maximum de 15 � 17 chiffres significatifs

c = 1 + 3j

print c.real, c.imag


## Par contre on peut perdre en pr�cision.
## Un int et un long donne toujours un long
## Un type entier (int, long) et un float donne toujours un float
## Un type entier (int, long) ou un float et un complex
## donne toujours un complex

print i + l

print i + l + f

print i + l + f + c

## On peut convertir des types de bases entre eux (avec risque
## de perte de pr�cision ou d'information, troncation).

print int(4.32)
print long(5.3)
print float(9879729572895792375948)
print complex(10)

## op�rations de base

print 5 + 3
print 5 - 3
print -3
print 5/3       # division enti�re
print 5%3       # reste de la division enti�re
print 5/3.0     # division sur des floats
print 5/float(3)
print 5.2//3.1  # force la division sur des entiers (5.0/3.0)
print 2 ** 32   # puissances
print abs(-5.3) # valeur absolue





