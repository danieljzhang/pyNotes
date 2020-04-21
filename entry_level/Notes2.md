These operations get a little more complicated as we use non-boolean operands:

    >>> 1 and 0
    0
    >>> 'This' and 'That'
    'That'
    >>> 'This' and 0 and 'That'
    0
    >>> 0.0 and 1
    0.0
Remember that and requires both operands to be true in order to return true, and this means that it will automatically return the first falsy value that it finds or the rightmost operand if they're both true.

The or operator works in the opposite way. It will return the first object that would evaluate to true, or the rightmost falsy value.

    >>> 1 or 0
    1
    >>> 0 or 1
    1
    >>> 0 or ""
    ""
    >>> 0 or 1 or 'This'
    1

#### Input function
age = int(input("How old are you today? "))
If the input above is not a number, the ValueError will be raised.

    >>> print("1", "2", "3")
    1 2 3
    >>> print("1", "2", "3", sep="/")
    1/2/3
    >>> print("1", "2", "3", sep = "/", end=".")
    1/2/3.
    >>> 
* build-in functions are lower case.

#### String
String is immutable 
    >> my_str = 'testing'
    >>> my_str.capitalize()
    'Testing'
    >>> my_str
    'testing' 

#### Slicing with step
The last thing to mention about slicing is that there is a third number that we can use: the "step" value. By default, this value is 1 and just means that we'll go one-by-one through the sequence. But we can change this to grab every other item if we'd like by adding a second colon and the step size that we'd like to use:

    >>> test_str
    'testing'
    >>> test_str[1:5:2]
    'et'
    >>> test_str[1::2]
    'etn'

#### Reverse the string
One neat thing that we can do with this step option is stepping backward by using a negative step value. We can reverse an entire string by leaving off the start and end indexes and setting the step value to -1:

    >>> test_str[::-1]
    'gnitset'

In Python 3, strings are Unicode by default (specifically UTF-8 encoded).
UTF-8 stands for "Unicode Transformation Format," with the "8" meaning that values are 8-bits in length. 

#### Split and Join
If we have a delimiter that we'd like to use to separate the string into smaller strings, then we're able to use the split method to get a list of substrings. 

    >>> phrase = "This is a simple phrase"
    >>> words = phrase.split()
    >>> ", ".join(words)
    'This, is, a, simple, phrase'

    >>> lines = ['First line', 'Second line', 'Third line']
    >>> output = '\n'.join(lines)
    >>> print(output)
    First line
    Second line
    Third line

#### Format
print("This is {} plus {} equals {}".format(1, 2, 3))
This is 1 plus 2 equals 3
>>> 

 
Unlike strings, which can't be modified (we can't change a character in a string), we can change a value in a list using the subscript equals operation:

concatenate

    >>> my_list + [8, 9, 10]

Another way that we can remove an item from a list is by using the del statement and the indexing operation:

#### List

delete an item from list
    >>> my_list = ['a', 'b', 'c', 'd']
    >>> del my_list[0]
    >>> my_list
    ['b', 'c', 'd']

delete a list
    del my_list

append an element

The in and not in Operators
Sequence types have a few additional operators that make it easy for us to check the contents. The in and not in operators take a value that we'd like to search the sequence for on the left-hand side and a sequence on the right-hand side:

Reverse a list
    l[::-1]

sort a list
    sorted(l)

#### Reference:
Certified Entry-Level Python Programmer Certification, Linux Academy