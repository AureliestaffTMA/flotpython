# -*- coding: iso-8859-15 -*-

## Je vais cr�er une variable globale et une fonction
L = 10

def f():
    L = 11

print L
f()
print L

## La variable locale L ne modifie par la variable globale L
## Par contre, si l'on rajoute l'instruction global, alors
## �a veut dire que la variable L assign�e dans la fonction
## est bien la variable globale. L'instruction global permet
## de changer le scope d'une variable assign�e localement
## dans une fonction. 

def f():
    global L
    L = 11

print L
f()
print L

## globale est une intruction un peu particuli�re en Python
## �a n'est pas une instruction interpr�t� comme toutes les
## autres instruction, c'est une directive au compilateur
## qui g�n�re le byte code avant l'ex�cution. Donc, une
## variable d�finie comme �tant globale le sera pour tout le
## scope dans lequel l'instruction global est pr�sente,
## quelque soit la position de global dans ce scope.

def f():
    L = 12
    global L
f()
print L

## L est globale pour toute la fonction h(), m�me si globale
## est d�finie apr�s l'assignation 'L = 12'. Attention,
## dans les nouvelles version de Python, il sera interdit
## de mettre la directive global apr�s la variable que l'on
## veut rendre global. Il faut donc prendre l'habitude
## de mettre global au tout d�but des fonctions. 

# 2 minutes 30

## Pour finir, la directive global doit �tre utilis�e avec
## parcimonie. En effet, modifier une variable global
## dans une fonction en utilisant la directive globale
## rend le code difficile � suivre. Il faut toujours
## privil�gier les moficication explicite par retour
## de fonction. Regardon ces deux exemples

x = 100
def f():
    global x
    x = x + 10
f()
print x

## Regardons maintenant une autre mani�re d'�crire
## le m�me code

x = 100
def f():
    return x + 10
x = f()
print x

## dans le premier cas la modification de x est implicite,
## mais dans le deuxi�me cas  c'est explicique avec
## l'assignation du resultat de f() � la variable x. Il faut
## toujours privil�gier ce deuxi�me cas. 

## 4 minutes. 
