# -*- coding: cp1252 -*-

## op�rations communes � toutes les s�quences
## on prend comme example une cha�ne de caract�re
## o� chaque caract�re est un �l�ment de la s�quence

s1 = 'spam'
s2 = 'eggs'

## test d'appartenance

's' in s1
'x' in s1

'x' not in s1

## concat�nation (retourne une nouvelle s�quence)
## les deux s�quences doivent �tre de m�me type

s1 + s2

## autres op�rations
len(s1)
min(s1)
max(s1)

## indice de la premi�re occurence de 'g'
s2.index('g')

## nombre d'occurence de 'g' dans la s�quence
s2.count('g')

s1*3
'*'*20


s1[2]


## list
L = [1, 2.3, 'spam', False, 2354555L]
print L

## tuple
#Pour un tuple on remplace les croch�s par des parenth�ses
T = (1, 2.3, 'spam', False, 2354555L)
print T
