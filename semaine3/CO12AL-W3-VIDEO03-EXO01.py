# -*- coding: iso-8859-15 -*-

## il y a trois op�rateurs de tests bool�ens en Python
## and, or et not. A and B est vrai si A et B sont vrais,
## A or B est vrai A ou B est vrai, not A est vrai si A
## est faux.Regardons quelques exemples. 
print 1 < 2 and 3 < 4

print 1 < 2 or 3 > 4

print not 1 < 2

## On remarque qu'encore une fois la syntaxe est proche
## du langage naturel

## Les op�rateurs and et or sont shortcircuits, c'est-�-dire
## que l'argument de droite n'est pas toujours �valu�.
## Si on fait A and B, B n'est �valu� que si A est vrai
## Si on fait A ou B, B n'est �valu� que si A est faux.
## Regardons un exemple :
## la fonction func() n'est pas d�finie

#func()

print 3 < 2 and func()

print 1 < 2 or func()

## pour finir on peut combiner les op�rateurs, chaque
## op�rateur ayant un priorit� sp�cifique. Je ne vous
## expliquerai pas ces r�gles, parce qu'il vaut mieux
## les rendre explicites en utilisant des paranth�ses

print (1 < 2 and (not 3 > 4)) or 1 == 1
