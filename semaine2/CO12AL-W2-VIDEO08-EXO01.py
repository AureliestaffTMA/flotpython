# -*- coding: iso-8859-15 -*-

## il existe deux mani�res totalement �quivallentes de cr�er
## une cha�ne de caract�res. Soit on met la cha�ne que l'on
## veut cr�er entre apostrophes ou entre guillemets

s1 = 'spam'
s2 = "spam"

print s1, s2

print s1 == s2

## l'int�r�t d'avoir deux notations est que si dans la
## cha�ne on veut avoir un guillement ou une apostrophe
## en peut l'�crire en utilisant l'autre notation pour
## ne pas avoit d'ambigu�t�

s1 = "l'herbe"
s2 = 'un guillemet : "'

print s1, s2

## Il est possible d'�crire dans une cha�ne de caract�res
## des caract�res sp�ciaux qui sont toujours pr�c�d�s
## d'une barre oblique invers�e que l'on appelle backslash

print '\' \" \\ \n spam'

## mais supposons que l'on ait une cha�ne de caract�res
## qui contienne beaucoup de backslash qui ne repr�sente
## pas de caract�res sp�ciaux. C'est le cas notamment
## des chemins des fichiers sous Windows.

nom = 'c:\temp\test\f.py'
print nom

## on a deux solutions � ce probl�mes, soit on double
## tous les backslash, mais c'est fastidieux et sujet
## � erreur, soit on utilise une raw string, c'est-�-dire
## une cha�ne de caract�res qui n'interpr�te plus aucun
## backslash comme caract�re sp�cial.

nom = 'c:\\temp\\test\\f.py'
print nom

nom = r'c:\temp\test\f.py'
print nom

## un derni�re utilisation du backslash est lorsque l'on
## veut �crire une chaine de caract�res sur plusieurs lignes

text = 'Spam, Spam, Spam, Spam, \
lovely Spam, wonderful Spam'
print text

## il exite un dernier type de notation, en plus de l'apostrophe
## et du guillemet, pour cr�er une cha�ne de caract�res,
## c'est la triple apostrophe ou le triple guillemet.
## l'int�ret de cette notation est que les retours chariots
## sont automatiquement transform� en \n. C'est tr�s pratique
## pour �crire par exemple de l'aide ou de la documentation.

s = """
Usage : fft(n)
        calcule la fft de n
"""
s
print s

## comme les cha�nes de caract�res sont immuable, on ne peut
## pas les modifier en place, par contre, il existe de
## nombreuses fonctions qui retournent une nouvelle cha�ne
## modifi�e. Regardons quelques unes des ces fonctions.

s = "le spam, c'est bon"
s = s.upper()
print s
s = s.lower()
print s
s = s.replace('spam', 'poulet')
print s

## il y a ensuite deux fonctions tr�s importantes qui
## permettent de passer d'une cha�ne de caract�re � une liste
## et vice versa. Je rappelle que la liste et le type central
## en Python, il est donc naturel pour travailler
## sur une cha�ne de caract�re de la transformer en liste
## regardons un example

s = 'marc 35 175'
a = s.split()
print a
a[-1] = a[-1] + 'cm'
print a
s = ' '.join(a)
print s
s = ', '.join(a)
print s
a = s.split(', ')
print a

