title: Basic Data Types in Python 3: Booleans
slug: python-basic-data-types-booleans
meta: Learn to use boolean (True and False) values in your Python 3 code
category: post
date: 2019-11-15
modified: 2019-11-15
newsletter: False
headerimage: /img/191115-python-basic-data-types-booleans/header.jpg
headeralt: Learn basic Python data types in TwilioQuest 3 - Booleans
author: Kevin Whinnery
authorlink: https://www.twilio.com/quest


Welcome back to our ongoing series of blog posts on basic data types in 
[Python 3](/python-2-or-3.html)! Last time, we explored the functionality of
[strings](/blog/python-basic-data-types-strings.html). Today, we dive in to
another key data type - booleans. Booleans (and "boolean logic") are an 
important concept in programming, representing the concept of "true" and "false".

If you're learning Python, you might also want to
[check out TwilioQuest 3](https://www.twilio.com/quest/download).
You'll learn about basic data types like the boolean, and much more about 
Python programming.

Ready to learn how to use booleans in Python 3? Let's get started!


## Booleans in Python 3
[Booleans](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
are a concept that exists in every programming language. A boolean represents
the idea of "true" or "false". When you are writing a program, there
are often circumstances where you want to execute different code in different
situations. Booleans enable our code to do just that.

You can declare a boolean value in your code using the keywords `True` and 
`False` (note the uppercase). The following code would create two boolean
values and assign them to variables.

```python
mullet_looks_good = False
python_is_fun = True
```

More commonly, a boolean value is returned as a result of some kind of
comparison. The following code example would store a boolean value of `False`
in the `have_same_name` variable after using the 
[equality comparison operator](https://docs.python.org/3/library/stdtypes.html#comparisons),
the `==` symbol.

```python
my_name = "Wammu"
your_name = "Kars"

have_same_name = my_name == your_name
```


### Boolean logic
Booleans are used in your code to make it behave differently based on current
conditions within your program. You can use boolean values and comparisons in 
conjunction with the `if`, `elif`, and `else` keyoards as one means to achieve 
this.

```python
my_age = 10

if my_age >= 100:
  print("One hundred years old! Very impressive.")
elif my_age <= 3:
  print("Awwww. Just a baby.")
else:
  print("Ah - a very fine age indeed")
```

In addition to testing for truth, you can also check if conditions are not
true using the `not` keyword.

```python
favorite_team = "Vikings"

if not favorite_team == "Vikings":
  print("Oh - how unfortunate.")
else:
  print("Skol, Vikings!")
```


### More complex boolean logic
Sometimes you will need to evaluate multiple conditions in your boolean logic.
For this purpose, you'll combine the `and` and `or` keywords. The `and` keyword
compares two boolean values and returns `True` if both are true. The `or` keyword
compares two values and returns `True` if any of the statements are true.

Let's look at an example. That uses the `in` keyword to see if a string is
inside a **list** of values (we'll cover lists in a future article).

```python
favs = ["Donatello", "Raphael"]

if "Michelangelo" in favs and "Donatello" in favs:
  print("Those are my favorite ninja turtles too!")
elif "Michelangelo" in favs or "Donatello" in favs:
  print("Well, one out of two isn't bad...")
else:
  print("Huh - not what I would have chosen.")
```


## Wrapping up
Booleans are an important tool in any programming language. Using boolean logic,
your code can react to data inside your program, and carry out different
instructions under different circumstances. Hopefully, you've learned a bit 
about how to work with booleans in Python 3! Stay tuned for more blog posts in 
this series to learn more about basic data types like strings, numbers, 
booleans, lists, and dictionaries.

Also, be sure to 
[download and play TwilioQuest 3](https://www.twilio.com/quest/download)
to learn even more about Python! 
