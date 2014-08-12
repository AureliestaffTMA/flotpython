# -*- coding: iso-8859-15 -*-

## La syntaxe d'une fonction lambda est simple.
## Elle commence par le mot clef lambda, suivi
## d'une liste d'argument s�par� par des virgules
## et d'un expression pouvant utiliser ses arguments.

lambda x: x**2 + 2*x -1

## Cependant les fonctions lambda n'ont pas de nom
## alors comment les utiliser ? Le r�sultat
## de l'�valuation du code de la fonction lambda est une
## r�f�rence vers l'objet fonction qui vient d'�tre cr��

## On peut donc utiliser une fonction lambda de deux
## manieres, soit on lui donne un nom en l'assignant �
## une variable, soit on la d�finie directement l� o�
## elle va �tre utilis�e. 

f = lambda x: x**2 + 2*x - 1

print f(1)

L = [lambda x: x**2 + 2*x - 1, lambda x: x**3 -2]

print L[0](10), L[1](10)

## on peut �galement directement passer une fonction
## lambda � une fonction

def func(x):
    for i in range(10):
        print i, x(i)

## Je suppose lors de l'�criture de ma fonction func
## que l'argument x sera une fonction. Si x n'est pas
## une fonction j'aurai une exception

# func(1)

func(lambda x: x**2 -3)

## il est tr�s important de comprendre que je peux
## faire exactement la m�me chose avec une fonction
## classique. Apr�s tout en Python, tout est un objet
## et une variable n'est qu'un nom qui r�f�rence un
## objet, en particulier, le nom d'un fonction
## r�f�rence l'objet fonction d�fini par le def.

def g(x):
    return x**2 -3
func(g)

## la fonction lambda permet simplement d'�crire
## plus rapidement les fonctions qui sont limit�e
## � une seule expression. En effet, dans une fonction
## lambda, on ne peut pas mettre d'instructions comme
## des if ou des for. 

# 4 minutes

## Un usage classique des fonctions lambda en Python est
## de les utiliser avec les fonctions built-in map() et
## filter().

## Je vous rappelle qu'en Python les it�rateurs sont au coeur
## de la programmation et qu'avec les boucles for,
## on peut de mani�re simple et efficace exploiter la
## puissance des it�rateurs. Il existe cependant d'autres
## moyen d'exploiter les it�rateurs en Python

