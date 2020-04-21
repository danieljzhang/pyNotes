#### Tuples
Tuples are a fixed width, immutable sequence type. 
We create tuples using parenthesis (()) and at least one comma (,):

    >>> point = (2.0, 3.0)
    Since tuples are immutable, we don't have access to the same methods that we do on a list. We can use tuples in some operations like concatenation, but we can't change the original tuple that we created:
    
    >>> point_3d = point + (4.0,)
    >>> point_3d
    (2.0, 3.0, 4.0)

When we use tuple:
Tuples make more sense in two general situations:

When we're trying to return more than one piece of information from a function
If we want to model something that has a specific number of fields that we can positionally hold in a tuple:

#### Dictionary
Unlike Python 2 dictionaries, Python 3.7 keys are ordered in dictionaries.

Create dictionaries
    ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
There are a few other ways to create dictionaries that we might see, which are those using the dict constructor with key/value arguments and a list of tuples:

    >>> weights = dict(kevin=160, bob=240, kayla=135)
    >>> weights
    {'kevin': 160, 'bob': 240, 'kayla': 135}
    >>> colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
    >>> colors
    {'kevin': 'blue', 'bob': 'green', 'kayla': 'red'}

Keys can be added or changed using subscripting and assignment:
Keys can be added or changed using subscripting and assignment:

Just like with lists and tuples, dictionaries have access to the in and not in operators. Notably, this only considers the keys:

There are a few other ways to create dictionaries that we might see, which are those using the dict constructor with key/value arguments and a list of tuples:

    >>> weights = dict(kevin=160, bob=240, kayla=135)
    >>> weights
    {'kevin': 160, 'bob': 240, 'kayla': 135}
    >>> colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
    >>> colors
    {'kevin': 'blue', 'bob': 'green', 'kayla': 'red'}

#### Reference:
Certified Entry-Level Python Programmer Certification, Linux Academy