#### Keywords
Three uppercase keywords:
None, True, False

#### REPL
To exit the REPL, you can either type exit() (the parentheses are important) or you can hit Ctrl+d on your keyboard.

#### Shebang
Setting a Shebang
We'll most likely want our scripts to be:

Executable from anywhere (in our $PATH)
Executable without explicitly using the python3.7 CLI
Thankfully, we can set the process to interpret our scripts by setting a shebang at the top of the file:

hello.py:

    #!/usr/bin/env python3.7
    print("Hello, World")`

We're not quite done. Now we need to make the file executable using chmod:

    $ chmod u+x hello.py
Run the script now by using ./hello.py and we'll see the same result. If we'd rather not have a file extension on our script, we can remove it since we've put a shebang in the file. Running mv hello.py hello then performing ./hello will still result in the same thing.

#### Variable
if we assign a variable with another variable, it will be assigned to the initial result of the variable and not whatever that variable points to later.

    >>> my_str = 1
    >>> my_int = my_str
    >>> my_str = "testing"
    >>> print(my_int)
    1
    >>> print(my_str)
    testing


#### String
find locates the first instance of a character (or string) in a string.
This function returns the index of the character or string.

    "string".find('s')
    
lower()
upper()

#### True or False
Notice the upper case here
We can check the Boolean value for any object in Python by using the bool function. For instance, the empty string "" has the boolean value of False where any other string as a boolean value of True.

    5 // 3 # Floor division, always returns a number without a remainder as an int
    1
    >>> 8 % 3 # Modulo division, returns the remainder as an int
    2
    >>> 2 ** 3 # Exponent

#### Representing Binary, Octal, and Hexadecimal Numbers in Python
Now that we know how various and common number systems work let's go about actually using them in Python. To represent a number in a different number system in Python, we do this by prefixing the number with a 0 and the number system identifier:

Binary uses b
Octal uses o
Hexadecimal uses x
Here are examples in the REPL:

    >>> 0b1001
    9
    >>> 0o7424
    3860
    >>> 0xFF012
    1044498

The result printed out will be the decimal value. If we want to work in decimal values and represent them in a different numbering system we can use the bin, oct, and hex functions like so:

    >>> bin(10)
    '0b1010'
    >>> oct(59)
    '073'
    >>> hex(1024)
    '0x400'

#### Bitwise operators:
~ & | << >>

#### boolean operators
and or not
notice here they are all lower case

#### The Identity Operators
If we want to know if two objects are or are not exactly the same object, then we can use the identity operators. The identity operator is the keyword is and the opposite is is not (with a space).

    >>> 1 is 1
    True
    >>> 1 is 1.0
    False
    >>> 'a' is 'a'
    True
    >>> 'a' is not 'b'
    True
    >>> 'a' is not 'a'
    False
The identity operators work based on the id of the object, and most of the basic types in Python are immutable (meaning they cannot be changed), so every time that we reference a specific literal it will point to the same item in memory. We can check the id of an object by using the id function (your return values will be different):

    >>> id('a')
    4444195248
    >>> id('a')
    4444195248
    >>> id('a') == id('a')
    True
We'll discuss immutability later, but not all objects are immutable, so you'll run into situations where you can compare two objects that look the same using is and have False returned. Here are two list literals (which aren't immutable):

    >>> [] is []
    False
    
    >>> int(1.3)
    1
    >>> int(2.6)
    2
Notice that the result from converting 2.6 to an integer doesn't round, it truncates. It's as though the decimal point value doesn't exist.

There are a select few items that convert into False. These are detailed in the Python truth value testing documentation, but can be summed up as False, None, any 0 value, and any empty sequence (an empty string for instance).

#### Reference:
Certified Entry-Level Python Programmer Certification, Linux Academy
