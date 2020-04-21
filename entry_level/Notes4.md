
### pass statement
The pass statement is what is known as a null operation. Absolutely nothing happens when we execute a pass statement, but they are useful as a code placeholder:

#### While loop

>>> count = 1
>>> while count <= 4:
...     print("looping")
...     count += 1

#### For loop
The general structure for a for loop is:

for TEMP_VAR in SEQUENCE:
    pass
	
>>> for key, value in ages.items():
...     print(key, value)

The else clause for loops in Python allows us to define an additional code context that will execute when the loop has naturally finished its iteration. 
In a for loop, this means that we've reached the end of our iteration, and in a while loop it means the conditional has evaluated to False. 

# Range
A range is an immutable sequence type that defines a start, a stop, and a step value. The values within the range start with the beginning value and are incremented until the last value in the range is reached. This allows for ranges to be used in place of sequential lists while taking less memory and including more items.

    >>> my_range = range(10)
    >>> my_range
    range(0, 10)
    >>> list(my_range)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(range(1, 14, 2))
    [1, 3, 5, 7, 9, 11, 13]

We have _ (Scala learned from Python or Python learned from scala)
    >>> for _ in range(1, 5):
    ...     print("looping")
    ...
    looping
    looping
    looping
    looping
    >>>

#### List comprehension

These have a unique syntax where we essentially put the for loop within square brackets ([]). Here's the equivalent for the above, using a list comprehension:

    >>> colors = ['red', 'blue', 'orange', 'green', 'yellow']
    >>> uppercase_colors = [color.upper() for color in colors]
    >>> uppercase_colors
    ['RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW']

If we remove the concept of warm_colors being used within the loop, we can write it as a list comprehension:

    >>> colors = ['red', 'blue', 'orange', 'green', 'yellow']
    >>> warm_colors = [color.upper() for color in colors if color in ['red', 'orange', 'yellow']]
    >>> warm_colors
    ['RED', 'ORANGE', 'YELLOW']

#### Function

The difference between a parameter and an argument is all about timing. 
When we're working with the definition of a function, then the variables defined in the function declaration are the "parameters." 
When we're calling the function, the data that we provide for each parameter is the "argument." 

#### Reference:
Certified Entry-Level Python Programmer Certification, Linux Academy