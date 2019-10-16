title: Basic Data Types in Python 3: Strings
slug: python-basic-data-types-strings
meta: Learn to create and manipulate strings in this series of blog posts on basic data types in Python programming.
category: post
date: 2019-10-18
modified: 2019-10-18
newsletter: False
headerimage: /img/191018-python-basic-data-types-strings/header.jpg
headeralt: Learn basic Python data types in TwilioQuest 3 - Strings
author: Kevin Whinnery
authorlink: https://www.twilio.com/quest


There is a lot to learn on your Python journey when you are
[new to the programming language](/learning-programming.html). Once you are 
comfortable writing and executing code, your first stop becomes understanding 
how to represent data in
your code. No matter the language, there are a few basic data types you'll use
all the time - strings, numbers, booleans, lists, and dictionaries.

Those data types, and how to use them in Python 3, are the topic of this blog 
post series. Today, we're starting with __strings__.

If you're learning Python, you might also want to
[check out TwilioQuest 3](https://www.twilio.com/quest/download).
You'll learn about basic data types and much more about Python programming.

Ready to learn how to use strings in Python 3? Let's get started!


## Strings in Python 3
One of the most common data types in any programming language is a `string`. A
__string__ represents a series of characters, which you would use to represent
usernames, blog posts, tweets, or any text content in your code. You can create
a string and assign it to a variable like this.

```python
my_name = "Jonathan Joestar"
```


### Strings are "immutable"
In Python, strings are considered [immutable](https://www.merriam-webster.com/dictionary/immutable) - 
once you create them, they can't be changed. You can, however, use a variety of
methods to create new strings from existing strings. This type of work in
programming is called __string manipulation__. Some web developers joke that at
the end of the day, their job is just mashing strings together - and this isn't
far from the truth!

Here are some common tasks you might undertake when using strings in your code.


### Common task - combining strings together
Combining strings together - __concatenating__ them - is a very common task. In
Python 3, you can use the `+` operator for this purpose. You can use the `+`
operator multiple times to concatenate multiple strings.

```python
first_name = "Jonathan"
last_name = "Joestar"

full_name = first_name + " " + last_name
```


### Common task - inserting data into strings
Another common task with strings is inserting data into a specific place
within a string. In programming, we call this __string interpolation__. Python 3
provides a handy tool for doing this called ["f" strings](https://www.python.org/dev/peps/pep-0498/).
The "f" in "f strings" stands for __format__ - you can insert other data from
your program into a string when you define it rather than doing complex string
concatenation as demonstrated previously.

Here is an example of creating a formatted string - note the letter `f` is
included just before the first double quote when defining the `message` variable.
When you want to insert data from your program into the string, you can include 
it between two "curly braces" - the `{` and `}` characters.

```python
first_name = "Jonathan"
last_name = "Joestar"
age = 24

message = f"My name is {first_name} {last_name}, and I am {age} years old."
print(message)
```


### Common task - using built-in string methods to manipulate strings
String objects have a number of [methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
to perform common tasks, like changing the case of strings or trimming their 
content. Below, you'll find a few examples. In two of these examples, we are
creating a string variable, and then assigning the same variable a new value,
which is the result of calling a method on a string object.

__Example 1:__ Convert a string to all caps using the `upper` method.

```python
example_string = "am I stoked enough yet?"
example_string = example_string.upper()
print(example_string) # prints "AM I STOKED ENOUGH YET?"
```

__Example 2:__ Replace all instances of the word `kale` with `tacos`.

```python
example_string = "We're having kale for dinner! Yay kale!"
example_string = example_string.replace("kale", "tacos")
print(example_string) # prints "We're having tacos for dinner! Yay tacos!"
```

__Example 3:__ Split a comma-delimited string into a list of strings.

```python
example_string = "Apples,Oranges,Pears"
groceries = example_string.split(',')

# Code below prints:
# Apples
# Oranges
# Pears
for item in groceries:
    print(item)
```

[Check our more strings can do](https://docs.python.org/3/library/stdtypes.html#string-methods)
in the Python 3 docs!


## Type casting
Frequently, you will want to convert data from one type into another. In 
programming, we call this process __type casting__. There are a number of 
__functions__ built in to Python which allow us to do these type conversions
on basic data types.

__Example 1:__ Convert a number into a string using the `str` function.

```python
example_number = 42
converted = str(example_number)
message = "The meaning of life is " + converted
```

__Example 2:__ Convert a string into a whole number (integer) using `int`.

```python
example_string = "2"
converted = int(example_string)
message = f"Two plus two equals { converted + 2 }"
```


## Wrapping up
Strings of text are one of the most common pieces of data you will work with
in programming. Hopefully, you've learned a bit about how to work with strings
in Python 3! Stay tuned for more blog posts in this series to learn more about
basic data types like strings, numbers, booleans, lists, and dictionaries.

Also, be sure to 
[download and play TwilioQuest 3](https://www.twilio.com/quest/download)
to learn even more about Python! 

