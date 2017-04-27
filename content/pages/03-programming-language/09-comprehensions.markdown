title: Comprehensions
category: page
slug: comprehensions
sortorder: 0309
toc: False
sidebartitle: Comprehensions
meta: Python comprehensions concisely create data for lists, dictionaries and sets. Read more on Full Stack Python.


# Comprehensions
Comprehensions are a Python language construct for concisely creating data
in lists, dictionaries and sets. List comprehensions are included in Python 2
while dictionary and set comprehensions were introduced to the language in
Python 3.


## Why are comprehensions important?
Comprehensions are a more clear syntax for populating conditional data in the 
core Python data structures. Creating data without comprehensions often 
involves nested loops with conditionals that can be difficult for code
readers to properly evaluate.


## Example code
List comprehension:

    >>> double_digit_evens = [e*2 for e in range(5, 50)]
    >>> double_digit_evens
    [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]


Set comprehension:

    >>> double_digit_odds = {e*2+1 for e in range(5, 50)}
    {11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99}

Dictionary comprehension:
    
    >>> {e: e*10 for e in range(1, 11)}
    {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}


## Comprehension resources
* Intermediate Python's 
  [Python Comprehensions](http://intermediatepythonista.com/python-comprehensions)
  post gives a well written overview of comprehensions for the three core 
  Python data structures.

* [Python List Comprehensions: Explained Visually](http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)
  explains how the common idiom for iteration became syntactic sugar in
  the language itself and how you can use it in your own programs.

* The Python 3 Patterns and Idioms site has an overview of 
  [comprehensions](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Comprehensions.html)
  including code examples and diagrams to explain how they work.

* [Comprehensions in Python the Jedi way](https://gist.github.com/bearfrieze/a746c6f12d8bada03589)
  shows off comprehensions with a Star Wars theme to walk through the nuts
  and bolts. All examples use Python 3.5.

* [Idiomatic Python: Comprehensions](https://blogs.msdn.microsoft.com/pythonengineering/2016/03/14/idiomatic-python-comprehensions/)
  explains how Python's comprehensions were inspired by Haskell's list
  comprehensions. It also provides clear examples that show how comprehensions
  are shorthand for common iteration code, such as copying one list into
  another while performing some operation on the contained elements.

* [Learning Python by example: list comprehensions](http://blog.cdleary.com/2010/04/learning-python-by-example-list-comprehensions/)
  gives an example of an incorrect list comprehension then shows how to
  correct its issues.

* [List comprehensions in Python](http://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
  covers what the code for list comprehensions looks like and gives some
  example code to show how they work.

* [An Introduction to Python Lists](http://effbot.org/zone/python-list.htm)
  is a solid overview of Python lists in general and tangentially covers 
  list comprehensions.

