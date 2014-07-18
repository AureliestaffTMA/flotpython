# -*- coding: latin_1 -*-

## une liste est une s�quence, donc toutes les fonctions et op�rations
## que l'on a vues pour les s�quences s'appliques aux listes : en particulier
## testes d'appartenance in, not in ; concat�nation avec le signe + ;
## longeur avec la fonction built-in len ; r�cup�ration d'un �l�ment
## par son index entre crochet ; et le slicing.

## on cr�e une liste vide ainsi
L = []

## on s�pare les �l�ments d'une liste par des virgules

L = [4, 'spam', 3.2, True]

## notons que l'on peut directement mettre un objet dans
## la liste, ou utiliser une variable r�f�rencant l'objet

print L[1]

L[0] = L[0] + 1

print L
