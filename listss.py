Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> [1, 2, 3]
[1, 2, 3]
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']
>>> spam[0]
'cat'
>>> spam[1]
'bat'
>>> spam[3]
'elephant'
>>> spam[2]
'rat'
>>> ['cat', 'bat', 'rat', 'elphant'][3]
'elphant'
>>> 'Hello ' + spam[0]
'Hello cat'
>>> 'The ' + spam[0] + ' ate the ' + spam [2]
'The cat ate the rat'
>>> spam[1]
'bat'
>>> spam[1.0]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    spam[1.0]
TypeError: list indices must be integers or slices, not float
>>> spam[int(1.0)]
'bat'
>>> spam[['cat', 'bat']],[[45,65,89,65,78]]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    spam[['cat', 'bat']],[[45,65,89,65,78]]
TypeError: list indices must be integers or slices, not list
>>> spam[['cat','bat'], [45, 65, 98, 68, 33]]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    spam[['cat','bat'], [45, 65, 98, 68, 33]]
TypeError: list indices must be integers or slices, not tuple
>>> spam=[['cat','bat'], [45, 65, 98, 68, 33]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][0]
'cat'
>>> spam[1][3]
68
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[-1]
'elephant'
>>> spam[-3]
'bat'
>>> 'The ' + spam[-1] + ' is afraid of the ' + spam[-3] '.'
SyntaxError: invalid syntax
>>> 'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
'The elephant is afraid of the bat.'
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[1:3]
['bat', 'rat']
>>> spam[0:2]
['cat', 'bat']
>>> spam[0:5]
['cat', 'bat', 'rat', 'elephant']
>>> spam[0:3]
['cat', 'bat', 'rat']
>>> spam[0,-2]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    spam[0,-2]
TypeError: list indices must be integers or slices, not tuple
>>> spam[0:-1]
['cat', 'bat', 'rat']
>>> spam[0:-2]
['cat', 'bat']
>>> spam[:2]
['cat', 'bat']
>>> spam[:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[0:3]
['cat', 'bat', 'rat']
>>> spam[:]
['cat', 'bat', 'rat', 'elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']
>>> len(spam)
4
>>> spam[1]='game'
>>> spam
['cat', 'game', 'rat', 'elephant']
>>> spam[0]='Watch'
>>> spam[1]='of'
>>> spam[1]='Game'
>>> spam[2]='of'
>>> spam[3]='Thrones'
>>> spam
['Watch', 'Game', 'of', 'Thrones']
>>> [1, 2, 3] + spam
[1, 2, 3, 'Watch', 'Game', 'of', 'Thrones']
>>> spam
['Watch', 'Game', 'of', 'Thrones']
>>> [1, 2, 3] + spam = spam
SyntaxError: can't assign to operator
>>> spam = [1, 2, 3] + spam
>>> spam
[1, 2, 3, 'Watch', 'Game', 'of', 'Thrones']
>>> spam *3
[1, 2, 3, 'Watch', 'Game', 'of', 'Thrones', 1, 2, 3, 'Watch', 'Game', 'of', 'Thrones', 1, 2, 3, 'Watch', 'Game', 'of', 'Thrones']
>>> del spam[3]
>>> spam
[1, 2, 3, 'Game', 'of', 'Thrones']
>>> spam[6] = 'season'
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    spam[6] = 'season'
IndexError: list assignment index out of range
>>> spam = spam + ['season']
>>> spam
[1, 2, 3, 'Game', 'of', 'Thrones', 'season']
>>> del spam[0][1][2]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    del spam[0][1][2]
TypeError: 'int' object is not subscriptable
>>> del spam[0]
>>> del spam[1]
>>> del spam[2]
>>> spam
[2, 'Game', 'Thrones', 'season']
>>> spam[0]
2
>>> spam[1]
'Game'
>>> spam[4]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    spam[4]
IndexError: list index out of range
>>> del spam
>>> spam
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    spam
NameError: name 'spam' is not defined
>>> spam=[]
>>> str(len(spam) + 1)
'1'
>>> 
===================== RESTART: C:/Python34/allMyCats.py =====================
Enter the name of cat 1 (Or enter nothing to stop):
May
Enter the name of cat 2 (Or enter nothing to stop):
Kate
Enter the name of cat 3 (Or enter nothing to stop):
Nagi
Enter the name of cat 4 (Or enter nothing to stop):
Chiku
Enter the name of cat 5 (Or enter nothing to stop):
Monu
Enter the name of cat 6 (Or enter nothing to stop):
Pinky
Enter the name of cat 7 (Or enter nothing to stop):
Tinku
Enter the name of cat 8 (Or enter nothing to stop):
Aku
Enter the name of cat 9 (Or enter nothing to stop):

The cat names are :
 May
 Kate
 Nagi
 Chiku
 Monu
 Pinky
 Tinku
 Aku
>>> supplies = ['pens', 'staples', 'flame-throwers', 'binders']
>>> for i in range(len(supplies)):
	print('Index ' + str(i) + 'in supplies is ' + supplies[i])

Index 0in supplies is pens
Index 1in supplies is staples
Index 2in supplies is flame-throwers
Index 3in supplies is binders
>>> for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is ' + supplies[i])

Index 0 in supplies is pens
Index 1 in supplies is staples
Index 2 in supplies is flame-throwers
Index 3 in supplies is binders
>>> 
