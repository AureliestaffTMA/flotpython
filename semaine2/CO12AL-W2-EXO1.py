# -*- coding: latin_1 -*-

## l'instruction print afficher simplement la valeur d'un objet sur le terminal
## on dit �galement que l'on affiche une valeur sur la sortie standard

## print peut aussi bien accepter une variable (et dans ce cas il affiche
## la valeur de l'objet r�f�renc� par la variable) ou directement un objet.
## regardons cela en pratique

s = 'spam'
print s
print 'spam'

## l'instruction print permet aussi d'afficher plusieurs objets ou variable
## en les s�parant par une virgule

i = 10

print i, s

## lorsqu'il y a une virgule entre les arguments (variable ou objet) pass�
## � print, print ajoute un espace entre les valeurs des arguments retourn�s

## print ajoute automatiquement un retour chariot (c'est-�-dire, un saut de ligne)
## apr�s la derni�re valeur affich�e. On peut supprimer ce saut de ligne en ajoutant
## une virgule apr�s le dernier argument pass� � print.

print s
print s

print s,
print s


## lorsque l'on est dans le terminal interactif, on peut aussi directement
## taper le nom de la variable suivi d'un retour chariot.

i

## On voit ainsi la repr�sentation interne de l'objet ?
## c'est souvent �quivallent � print (mais pas toujours).
## La repr�sentation interne peut donner des informations
## suppl�mentaires.

