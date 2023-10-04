# Python Tutorial

Welcome to this basic Python tutorial! In this tutorial, we will cover the fundamentals of Python programming. Whether you're a beginner or looking to refresh your Python skills, this guide is here to help you get started.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Variables and Data Types](#variables-and-data-types)
4. [Control Structures](#control-structures)
5. [Functions](#functions)
6. [Lists](#lists)
7. [Dictionaries](#dictionaries)
8. [File Handling](#file-handling)
9. [Conclusion](#conclusion)

<a name="introduction"></a>

## 1. Introduction

Python is a versatile and beginner-friendly programming language known for its simplicity and readability. It's widely used in various domains, including web development, data analysis, and artificial intelligence. This tutorial will cover the basics of Python to get you started on your programming journey.

<a name="getting-started"></a>

## 2. Getting Started

### Installing Python

To begin, you need to have Python installed on your computer. You can download the latest version of Python from the official website: [Python.org](https://www.python.org/downloads/).

### Writing Your First Python Program

Create a file with a `.py` extension, such as `hello.py`, and open it in a text editor. Write the following code:

```python
print("Hello, World!")
```

Save the file and open your terminal or command prompt. Navigate to the directory containing your `hello.py` file and run the program using the following command:

```bash
python hello.py
```

You should see the output: "Hello, World!" Congratulations, you've just executed your first Python program!

<a name="variables-and-data-types"></a>

## 3. Variables and Data Types

### Variables

In Python, you can create variables to store data. Variables can hold various data types, including numbers, strings, and more. Here's how you define a variable:

```python
name = "Alice"
age = 30
```

### Data Types

Python supports various data types:

- **int**: Integer numbers (e.g., 42).
- **float**: Floating-point numbers (e.g., 3.14).
- **str**: Strings (e.g., "Hello, Python!").
- **bool**: Boolean values (True or False).
- **list**: Ordered collections of items.
- **dict**: Key-value pairs.

For example:

```python
# Examples of data types
name = "Alice"   # str
age = 30         # int
height = 5.8     # float
is_student = True  # bool
```

<a name="control-structures"></a>

## 4. Control Structures

Python provides control structures like `if`, `for`, and `while` to manage program flow.

### Conditional Statements (if-elif-else)

```python
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

### Loops (for and while)

```python
# for loop
for i in range(5):
    print(i)

# while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1
```

<a name="functions"></a>

## 5. Functions

Functions allow you to reuse code by defining custom actions. Here's how to create a simple function:

```python
def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("Alice")
```

<a name="lists"></a>

## 6. Lists

Lists are collections of items. They are defined using square brackets `[]`.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accessing the first item
fruits.append("orange")  # Adding an item
```

<a name="dictionaries"></a>

## 7. Dictionaries

Dictionaries are collections of key-value pairs, defined with curly braces `{}`.

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["name"])  # Accessing values by key
```

<a name="file-handling"></a>

## 8. File Handling

You can read from and write to files in Python using the `open` function.

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Python!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

<a name="conclusion"></a>

## 9. Conclusion

This tutorial provides a brief introduction to Python programming. As you continue your journey, explore Python's rich ecosystem of libraries and frameworks that cater to various domains. Practice coding regularly to improve your skills, and don't hesitate to consult the Python documentation and online resources for further learning.

Happy coding!