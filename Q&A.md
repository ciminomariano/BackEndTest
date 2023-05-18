### :speaking_head: Instructions
<img src="https://raw.githubusercontent.com/MicaelliMedeiros/micaellimedeiros/master/image/computer-illustration.png" min-width="400px" max-width="400px" width="400px" align="right" alt="TomDatalab">

<p align="left"> 
  Choose a quiet and peaceful place to perform the tests. The main objective is that we can understand the level of knowledge of the candidate. Be honest with your answers. There is no pre-established time for completing the tests, <strong>do your best</strong>.<br>
</p>

## <img width="45" alt="about" src="https://raw.github.com/elizarov/elizarov/master/about.png"> Good luck !

# :speaking_head: Part I - Python 

:blue_book: <strong><b>1)</b></strong> What is Python? What are the benefits of using Python
Python is a high level programming language,
some of his benefits are simplicity, reliability, versatility and is easy
to learn.
Also benefit is that python has a Large standard library

:blue_book: <strong><b>2)</b></strong> What is a dynamically typed language?
Is a language where the variables types are checked during runtime

:blue_book: <strong><b>3)</b></strong> What is an Interpreted language?

Is a language in which the source code is read and interpreted line by line

:blue_book: <strong><b>4)</b></strong> What is PEP 8 and why is it important?

Is an standard for programming python code it is important because
it makes the code more easy to understand and read and maintain

:blue_book: <strong><b>5)</b></strong> What is Scope in Python?

Is the visibility of and access of the variables in python
there are Global Scope, Local Scope an Non local scope 

:blue_book: <strong><b>6)</b></strong> What are lists and tuples? What is the key difference between the two?

Are data structures the main diference is that list are mutable and tuples are inmutables.


:blue_book: <strong><b>7)</b></strong> What are the common built-in data types in Python?

Numeric types(int,float), mapping type(dict), sequence types (lists,tuples,strings),
set types, boolean type, None type.


:blue_book: <strong><b>8)</b></strong> What is pass in Python?

Is a statement that is used when you want that your code do nothing.

:blue_book: <strong><b>9)</b></strong> What are modules and packages in Python?

Modules and packages are python files containing definitions functions 
is used to organize the code logically

:blue_book: <strong><b>10)</b></strong> What are global, protected and private attributes in Python?

Are definitions about how the attributes can be accesed from different parts of the code.

:blue_book: <strong><b>11)</b></strong> What is the use of self in Python?

Is a convenctionally parameter to reference an instance of a class

:blue_book: <strong><b>12)</b></strong> What is __init__?

Is the constructor method it is used to initialize the attributes 
of the object.

:blue_book: <strong><b>13)</b></strong> What is break, continue and pass in Python?

Are control flow statements used in loops break is used to terminate the
current loop, continue to move to the next iteration and pass is used when
no action is needed

:blue_book: <strong><b>14)</b></strong> What are unit tests in Python?

Is a way to verify the correct functionality of code usually functions
method or classes

:blue_book: <strong><b>15)</b></strong> What is docstring in Python?

Is a comment to add documentation in the code

:blue_book: <strong><b>16)</b></strong> What is slicing in Python?

is a way to extract part of an element giving an start end position and an increment

:blue_book: <strong><b>17)</b></strong> Explain how can you make a Python Script executable on Unix?

You have to add the execution permisions to the file and run the script like ./script.py 
also you have to active your python virtual enviroment or interpreter

:blue_book: <strong><b>18)</b></strong> What is the difference between Python Arrays and lists?

Arrays have a size predefined while lists can be resided.
Lists has more built in methods but arrays have more efficiency managing memory 

:blue_book: <strong><b>19)</b></strong> How is memory managed in Python?

Memory is handled automatically

:blue_book: <strong><b>20)</b></strong> What are Python namespaces? Why are they used?

Is a way to organize the code to be more clean modular and reusable

:blue_book: <strong><b>21)</b></strong> What is Scope Resolution in Python?

Is the way in which python resolves the scopes normally python
resolves variables and function from local scope then enclosing scope and then
global scople

:blue_book: <strong><b>22)</b></strong> What are decorators in Python?

Is a way of modify the behavior of functions methods or classes 
without having to modify the source code of them

:blue_book: <strong><b>23)</b></strong> What are Dict and List comprehensions?

List comprehensions is a way to create new list from an existing one giving
some conditions and using an loop
Is similar to list comprehensions but creating a dictionary instead a list

:blue_book: <strong><b>24)</b></strong> What is lambda in Python? Why is it used?

is a function that can be defined without a name are commonly used when
a function is required as an argument.
the syntax is  lambda: parameters: expression

:blue_book: <strong><b>25)</b></strong> How do you copy an object in Python?
you can use copy module
import copy
new_object = old_object.copy() or new_object=old_object.deepcopy()
the first option creates a copy but it refers to the old object so if you
modify the new object it also modify the old, the second option will
create a totally new object and will not modify the old object

:blue_book: <strong><b>26)</b></strong> What is the difference between xrange and range in Python?
range returns a list of numbers and xrange an iterator  

:blue_book: <strong><b>27)</b></strong> What is pickling and unpickling?

Are process to serialize and deserialize python objects

:blue_book: <strong><b>28)</b></strong> What are generators in Python?

Is a kind of variable similar to list or tuples but they generate
values on the fly 

:blue_book: <strong><b>29)</b></strong> What is PYTHONPATH in Python?

Is an env variable in which python looks for additional modules and packages

:blue_book: <strong><b>30)</b></strong> What is the use of help() and dir() functions?

Are functions to get info about objects and get valid attributes and methods of them 

:blue_book: <strong><b>31)</b></strong> What is the difference between .py and .pyc files?

.py is the source code file and .pyc files are the compiled files

:blue_book: <strong><b>32)</b></strong> How Python is interpreted?

Is executed by an interpreter without need of being compiled

:blue_book: <strong><b>33)</b></strong> How are arguments passed by value or by reference in python?

by reference

:blue_book: <strong><b>34)</b></strong> What are iterators in Python?

are objects that allows iteration over a collection of elements one by one 

:blue_book: <strong><b>35)</b></strong> Explain how to delete a file in Python?

you can use the os.remove() function
import os 

file_path = "/path/file.txt"
try:    
    os.remove(file_path)
except Exception as e:
    print(f"Error deleting file: {e}")

:blue_book: <strong><b>36)</b></strong> Explain split() and join() functions in Python?

split is to split a string into a list of substring based on a specific delimiter
and join concatenate a sequence of strings using a specified separator 

:blue_book: <strong><b>37)</b></strong> What does *args and **kwargs mean?

allows to accept a variable number of arguments in a function

:blue_book: <strong><b>38)</b></strong> What are negative indexes and why are they used?

are indexes used to access an element from right to left 
the start from -1 
ex if we have a list of number  numbers = [1,2,3,4,5]

numbers[-1] refers to element 5
numbers[-2] refers to element 4


:blue_book: <strong><b>39)</b></strong> How do you create a class in Python?

using the keyword class
example

class MyClass:
    def __init__(self,parameter,second_parameter)
        self.instance_variable=parameter
        self.instance_variable2=second_parameter
    def instance_method(self):
        pass


:blue_book: <strong><b>40)</b></strong> How does inheritance work in python? Explain it with an example.

Inheritance allows a class inherit properties from another class called derived class.
For example, we can have an animal class which refers to all animals and a derived class dog
that inherits from animal and have specific methods and attributes that are just for dogs


:blue_book: <strong><b>41)</b></strong> How do you access parent members in the child class?
you can use super() to call a method defined in the parent class from the child class

:blue_book: <strong><b>42)</b></strong> Are access specifiers used in python?

No, python does not uses access specifiers but there is a good practice to
define public protected and private attributes and methods starting with _ __ and ___ 
respectively


:blue_book: <strong><b>43)</b></strong> Is it possible to call parent class without its instance creation?
No, you need to create an instance of the class

:blue_book: <strong><b>44)</b></strong> How is an empty class created in python?
you can use the pass staments

class Empty:
    pass

:blue_book: <strong><b>45)</b></strong> Differentiate between new and override modifiers.

new modifier is used to create a new method to the base class , override
is used to provide a new implementation for a method that exists

:blue_book: <strong><b>46)</b></strong> Why is finalize used?

is a method to define custom clean up actions in a class

:blue_book: <strong><b>47)</b></strong> What is init method in python?

Is a method that is called when you create an instance of a class, is
used to initialize the attributes and properties of the class

:blue_book: <strong><b>48)</b></strong> How will you check if a class is a child of another class?

you can use issubclass() method it will return True or False
ex  print(issubclass(Child,Parent)) 

:blue_book: <strong><b>49)</b></strong> What do you know about pandas?

Is a known library for data manipulation and analysis 

:blue_book: <strong><b>50)</b></strong> Define pandas dataframe.

Is a 2 dimension labeled data structure 

:blue_book: <strong><b>51)</b></strong> How will you combine different pandas dataframes?

depending on the requirements but there are different methods like concat(),merge(),join()

:blue_book: <strong><b>52)</b></strong> Can you create a series from the dictionary object in pandas?

Yes it is possible

:blue_book: <strong><b>53)</b></strong> How will you identify and deal with missing values in a dataframe?

you can use the df.isnull() to identify null values
also you can use dropna() function to erase dataframes

:blue_book: <strong><b>54)</b></strong> What do you understand by reindexing in pandas?

is a way to create a new dataframe with new set of labels

:blue_book: <strong><b>55)</b></strong> How to add new column to pandas dataframe?

you can use the next sintax 

df['new_field'] = ['value','value2'] note that the df must be created

:blue_book: <strong><b>56)</b></strong> How will you delete indices, rows and columns from a dataframe?

for index you can use df.reset_index(drop=True,inplace=True)
for rows df.drop([index],inplace=True)
for columns df.drop(['column1'],['column2'],axis=1,inplace=True)

:blue_book: <strong><b>57)</b></strong> Can you get items of series A that are not available in another series B?

yes

import pandas as pd

# Create Series A and Series B
series_a = pd.Series([1, 2, 3, 4, 5])
series_b = pd.Series([3, 4, 5, 6, 7])

# Get items of Series A not available in Series B
not_in_b = series_a[~series_a.isin(series_b)]

print(not_in_b)

:blue_book: <strong><b>58)</b></strong> How will you get the items that are not common to both the given series A and B?

not_common = pd.concat([series_a[~series_a.isin(series_b)], series_b[~series_b.isin(series_a)]])


:blue_book: <strong><b>59)</b></strong> While importing data from different sources, can the pandas library recognize dates?

yes pandas has different functions to import dates from different sources as csc excel sql json etc

:blue_book: <strong><b>60)</b></strong> What do you understand by NumPy?

is a library that offers support for array and matrices with a lot
of mathematical functions to operate between them

:blue_book: <strong><b>61)</b></strong> How are NumPy arrays advantageous over python lists?
They provide powerful and efficient data structure for numerical and computations proccesing
tasks

:blue_book: <strong><b>62)</b></strong> What are the steps to create 1D, 2D and 3D arrays?
#import the library
import numpy as np

create a 1d array arr = np.array([1, 2, 3, 4, 5])
create a 2d array arr2 =np.array([[1, 2, 3], [4, 5, 6]])
create a 3d array arr3 =np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

:blue_book: <strong><b>63)</b></strong> You are given a numpy array and a new column as inputs. How will you delete the second column and replace the column with a new column value?

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

array_without_column = np.delete(array, 1, axis=1)

new_column_vector = np.expand_dims(new_column, axis=1)

array_without_column[:, 1] = new_column_vector[:, 0]


:blue_book: <strong><b>64)</b></strong> How will you efficiently load data from a text file?

data = np.loadtxt('data.txt')

:blue_book: <strong><b>65)</b></strong> How will you read CSV data into an array in NumPy?

data = np.genfromtxt('data.csv', delimiter=',')

:blue_book: <strong><b>66)</b></strong> How will you sort the array based on the Nth column?

sorted_indices = np.argsort(data[:, N])

:blue_book: <strong><b>67)</b></strong> How will you find the nearest value in a given numpy array?

value=8
absolute_diff = np.abs(data - target_value)
nearest_index = np.argmin(absolute_diff)
nearest_value = data[nearest_index]

:blue_book: <strong><b>68)</b></strong> How will you reverse the numpy array using one line of code?
reversed_array = data[::-1]


:blue_book: <strong><b>69)</b></strong> How will you find the shape of any given NumPy array?
num_rows, num_columns = np.shape(array)

:blue_book: <strong><b>70)</b></strong> Differentiate between a package and a module in python.
Package is a way of organize modules in a directory structure while modules
are simple python files that contains code and definitions 

:blue_book: <strong><b>71)</b></strong> What are some of the most commonly used built-in modules in Python?
datetime,sys,json,random,math,urlib,collections,logging

:blue_book: <strong><b>72)</b></strong> What are lambda functions?
answered before

:blue_book: <strong><b>73)</b></strong> How can you generate random numbers?

you can use the random module 
import random
random = random.random()

:blue_book: <strong><b>74)</b></strong> Can you easily check if all characters in the given string is alphanumeric?
string = "hi123df"
is_alphanumeric = string.isalnum()
print(is_alphanumeric)

:blue_book: <strong><b>75)</b></strong> What are the differences between pickling and unpickling?

Not sure about this question

:blue_book: <strong><b>76)</b></strong> Define GIL.

Is the global interpreter lock ensure that only one thread executes python
bytecode at time
 
:blue_book: <strong><b>77)</b></strong> Define PYTHONPATH.

answered before

:blue_book: <strong><b>78)</b></strong> Define PIP.

is an utility to install python packages

:blue_book: <strong><b>79)</b></strong> Are there any tools for identifying bugs and performing static analysis in python?

Yes, i know Pylint and Flake 8.

:blue_book: <strong><b>80)</b></strong> Differentiate between deep and shallow copies.
deep creates a completely new object while shallow creates a new object with references to the original

:blue_book: <strong><b>81)</b></strong> What is main function in python? How do you invoke it?

is a convention to the entry point in a python program 
to invoke you can write the next code

def main():
    # Main logic of the program

if __name__ == "__main__":
    main()

:blue_book: <strong><b>82)</b></strong> Write python function which takes a variable number of arguments.

def variable_args(*args):
    for arg in args:
        print(arg)


variable_arguments(1,2,3)
variable_arguments("hi","ouronova")
variable_arguments(True)

:blue_book: <strong><b>83)</b></strong> WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.

def are_unique(numbers):
    unique_numbers = set(numbers)
    return len(numbers) == len(unique_numbers)

# Example usage
sequence1 = [1, 2, 3, 4, 5]
print(are_numbers_unique(sequence1))  # Output: True

sequence2 = [1, 2, 3, 2, 4]
print(are_numbers_unique(sequence2))  # Output: False

:blue_book: <strong><b>84)</b></strong> Write a program for counting the number of every character of a given text file.

def count_characters(filename):
    character_counts = {}

    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read the contents of the file
        contents = file.read()

        # Iterate over each character in the contents
        for char in contents:
            # Skip whitespace characters
            if char.isspace():
                continue

            # Increment the count for the character
            character_counts[char] = character_counts.get(char, 0) + 1

    return character_counts

# Example usage
file_path = 'path/to/your/file.txt'
counts = count_characters(file_path)

# Print the character counts
for char, count in counts.items():
    print(f"Character '{char}': {count}")


:blue_book: <strong><b>85)</b></strong> Write a program to check and return the pairs of a given array A whose sum value is equal to a target value N.

def find_pairs(A, N):
    pairs = []
    seen = set()

    for num in A:
        complement = N - num
        if complement in seen:
            pair = (num, complement)
            pairs.append(pair)
        seen.add(num)

    return pairs

# Example usage
array = [1, 2, 3, 4, 5, 6]
target = 7
result = find_pairs(array, target)

# Print the pairs
for pair in result:
    print(pair)



:blue_book: <strong><b>86)</b></strong> Write a Program to add two integers >0 without using the plus operator.

def add_without_plus(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Example usage
num1 = 5
num2 = 7
result = add_without_plus(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")

:blue_book: <strong><b>87)</b></strong> Write a Program to solve the given equation assuming that a,b,c,m,n,o are constants:

:blue_book: <strong><b>88)</b></strong> Write a Program to match a string that has the letter ‘a’ followed by 4 to 8 'b’s.

import re

def regex(string):
    pattern = r'a[b]{4,8}'
    match = re.search(pattern, string)
    return match is not None

# Example usage
test_string1 = 'abbbb'  # Matches
test_string2 = 'abbbbbbbb'  # Matches
test_string3 = 'ab'  # Does not match
test_string4 = 'abb'  # Does not match

print(regex(test_string1))  # Output: True
print(regex(test_string2))  # Output: True
print(regex(test_string3))  # Output: False
print(regex(test_string4))  # Output: False


:blue_book: <strong><b>89)</b></strong> Write a Program to convert date from yyyy-mm-dd format to dd-mm-yyyy format.

def convert_date(date):
    parts = date.split('-')
    formatted_date = parts[2] + '-' + parts[1] + '-' + parts[0]
    return formatted_date

# Example usage
date_input = '2023-05-18'
converted_date = convert_date(date_input)
print(f"The converted date is: {converted_date}")

:blue_book: <strong><b>90)</b></strong> Write a Program to combine two different dictionaries. While combining, if you find the same keys, you can add the values of these same keys. Output the new dictionary


def combine_dictionaries(dict1, dict2):
    combined_dict = dict1.copy()

    for key, value in dict2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value

    return combined_dict

# Example usage
dictionary1 = {'a': 10, 'b': 20, 'c': 30}
dictionary2 = {'b': 5, 'c': 15, 'd': 25}
combined_dictionary = combine_dictionaries(dictionary1, dictionary2)

# Print the combined dictionary
print(combined_dictionary)

:blue_book: <strong><b>91)</b></strong> How will you access the dataset of a publicly shared spreadsheet in CSV format stored in Google Drive?

I will get the link and make a request to the url using requests library 
then i will create a new file with open function and write the content of the response on it

# :speaking_head: Part II - Django 

:blue_book: <strong><b>1)</b></strong> Explain Django Architecture?
Is a model view controller architectural pattern in which you have different components
that work together 

:blue_book: <strong><b>2)</b></strong> Explain the django project directory structure?

Project Root Directory: Contains project-level configuration files and settings.

manage.py: Command-line utility for managing the Django project.

Project-level Configuration Files: settings.py (configuration settings) and urls.py (URL patterns and views).

Apps: Represent specific functionalities or modules within the project.

Static and Media Files: static/ directory for project-wide static files and media/ directory for user-uploaded media files.

Database-related Files: migrations/ directory for managing database schema changes, and the database file itself (e.g., db.sqlite3).

Other Files and Directories: templates/ directory for shared templates, requirements.txt for project dependencies, .env for environment-specific variables, and logs/ directory for log files.

:blue_book: <strong><b>3)</b></strong> What are models in Django?

are a representation of a table, define the schema and provide an abstraction to interact
with the database using an orm

:blue_book: <strong><b>4)</b></strong> What are templates in Django or Django template language?
are files that define the representation layer of a web application

:blue_book: <strong><b>5)</b></strong> What are views in Django?

are functions that handle the requests and generate the response to the endpoints

:blue_book: <strong><b>6)</b></strong> What is Django ORM?

is a component to interact with the database it simplifies operations and promotes
more efficient and secure way of working data

:blue_book: <strong><b>7)</b></strong> Define static files and explain their uses?


Static files in web development refer to the files that are served directly to the client's web browser without any 
processing by the server
In Django, static files are stored in a directory named static within each app or in a project-wide static directory.
Django provides a built-in mechanism to handle static files.
The static files can be collected and served using the collectstatic management command.
Additionally, during development, Django's development server automatically serves static files.



:blue_book: <strong><b>8)</b></strong> What is Django Rest Framework(DRF)?

Django Rest Framework (DRF) is a powerful and flexible toolkit for building Web APIs (Application Programming Interfaces) in Django

:blue_book: <strong><b>9)</b></strong> What is django-admin and manage.py and explain its commands?

are command line tools that provide several commands for managing django projects and 
applications 

django-admin:

django-admin startproject <project_name>: Creates a new Django project with the specified name.
django-admin startapp <app_name>: Creates a new Django application (referred to as "app") within the project with the specified name.
django-admin shell: Starts a Python interactive shell with the Django environment loaded. Useful for running Django code and executing queries interactively.
django-admin runserver: Starts the development server, allowing you to run the Django project locally for testing and development purposes.
django-admin makemigrations: Creates new database migration files based on the changes made to the models in the project.
django-admin migrate: Applies database migrations to update the database schema according to the defined models and migrations.
manage.py:

python manage.py runserver: Starts the development server, similar to django-admin runserver.
python manage.py makemigrations: Creates new database migration files for the current application(s) based on model changes.
python manage.py migrate: Applies database migrations to update the database schema for the current application(s).
python manage.py createsuperuser: Creates a superuser account for accessing the Django admin interface.
python manage.py shell: Starts a Python interactive shell with the Django environment loaded.
python manage.py test: Runs the tests for the project or specified applications.


:blue_book: <strong><b>10)</b></strong> What is Jinja templating?

Jinja is a popular templating engine for Python web frameworks, including Django and Flask. 
It provides a powerful and flexible way to generate dynamic content and generate 
HTML, XML, or other markup formats. Jinja templating separates the presentation layer from the business logic, 
allowing developers to focus on the data and structure of the content without mixing it with the code.


:blue_book: <strong><b>11)</b></strong> What are Django URLs?

In Django, URLs (Uniform Resource Locators) are used to map URL patterns to views in order to handle incoming requests 
and direct them to the appropriate code for processing. URLs define the structure and routing of a Django web application
, allowing users to access different pages and functionalities by navigating through the defined URLs.


:blue_book: <strong><b>12)</b></strong> What is the difference between a project and an app in Django?
A project refers to the entire web application while an app refers to an specific
modular component of the app


:blue_book: <strong><b>13)</b></strong> What are different model inheritance styles in the Django?

:blue_book: <strong><b>14)</b></strong> What are Django Signals?

Django Signals are a way to allow decoupled applications to get notified when certain actions occur elsewhere in the application.
Signals provide a mechanism for sending and receiving notifications or "signals" between different parts of a Django project.

:blue_book: <strong><b>15)</b></strong> Explain the caching strategies in the Django?

:blue_book: <strong><b>16)</b></strong> Explain user authentication in Django?

User authentication in Django refers to the process of verifying the identity of users and granting them access 
to certain resources or functionalities within a web application.
Django provides a robust and customizable 
authentication system that simplifies the implementation of user authentication feature

:blue_book: <strong><b>17)</b></strong> How to configure static files?

Define Static URL and Root:

In your project's settings module (usually settings.py), define the URL and root directory for serving static files.
Add the following lines to your settings module:

:blue_book: <strong><b>18)</b></strong> Explain Django Response lifecycle?

:blue_book: <strong><b>19)</b></strong> What databases are supported by Django?
postrgresql,mysql,sqllite,oracle,microsoft-sql-server

:blue_book: <strong><b>20)</b></strong> What's the use of a session framework?

A session framework in web development refers to a mechanism that allows storing and retrieving u
ser-specific data across multiple HTTP requests


:blue_book: <strong><b>21)</b></strong> What’s the use of Middleware in Django?

Middleware in Django is a key component that sits between the web server and the view layer of a Django application.
It provides a way to process requests and responses globally, allowing developers to add extra functionality to the
request/response processing flow. Middleware operates on each request-response cycle, performing actions before and 
after the view function is executed.

:blue_book: <strong><b>22)</b></strong> What is context in the Django?

is a dictionary-like object that holds variables and their corresponding values,
which can be accessed within templates. 
It provides a way to pass data from the view layer to the template layer,
enabling dynamic rendering of templates based on the provided data.

:blue_book: <strong><b>23)</b></strong> What is django.shortcuts.render function?

:blue_book: <strong><b>24)</b></strong> What’s the significance of the settings.py file?

The settings.py file in Django is a vital configuration file that holds various settings and configurations for a Django project.
It plays a significant role in controlling the behavior and features of a Django application

:blue_book: <strong><b>25)</b></strong> How to view all items in the Model?
from myapp.models import Item

items = Item.objects.all()

for item in items:
    print(item.name)

:blue_book: <strong><b>26)</b></strong> How to filter items in the Model?

filtered_items = Item.objects.filter(condition)
example 
filtered_items = Item.objects.filter(price__gt=10)


:blue_book: <strong><b>27)</b></strong> How to use file-based sessions?
add this configuration to your setting.py file
SESSION_ENGINE = 'django.contrib.sessions.backends.file'

:blue_book: <strong><b>28)</b></strong> What is mixin?

A mixin is a specific type of class that provides reusable functionalities and behavior that can be incorporated into
Django class-based views or models. 
Mixins in Django are commonly used to extend the functionality of views or models without the need for multiple inheritance.

:blue_book: <strong><b>29)</b></strong> What is Django Field Class?

In Django, a field class represents a database column and defines the type of data that can be stored in that column.
Field classes are an essential part of Django's Object-Relational Mapping (ORM) system, as they provide a way to define
the structure and characteristics of database fields in a Django model.

:blue_book: <strong><b>30)</b></strong> Why is permanent redirection not a good option?

:blue_book: <strong><b>31)</b></strong> Difference between Django OneToOneField and ForeignKey Field?
OneToOneField: This field represents a one-to-one relationship between two models. 
ForeignKey: This field represents a many-to-one relationship between two models. 

:blue_book: <strong><b>32)</b></strong> How can you combine multiple QuerySets in a View?


To combine multiple QuerySets in a view in Django, you can use the union() method, which is available on QuerySets.
The union() method allows you to combine QuerySets while eliminating duplicate results.

:blue_book: <strong><b>33)</b></strong> How to get a particular item in the Model?

You can do it by using the primary key,the field lookup or using a queryset filtering


:blue_book: <strong><b>34)</b></strong> How to obtain the SQL query from the queryset?


queryset = MyModel.objects.filter(condition=value)

# Get the SQL query
sql_query = queryset.query.__str__()

# Print or use the SQL query as needed
print(sql_query)

:blue_book: <strong><b>35)</b></strong> What are the ways to customize the functionality of the Django admin interface?

ModelAdmin Class: Customize specific models by overriding methods and attributes.
Customizing Templates: Modify the appearance of the admin interface by overriding templates.
AdminSite Class: Create separate admin interfaces with their own configurations.
InlineModelAdmin: Display related models within the parent model's edit form.
Custom Actions: Define custom actions for bulk operations or specific actions on objects.
Admin Middleware: Modify the admin interface behavior using middleware.
Third-Party Packages: Explore external packages for additional customization options.

:blue_book: <strong><b>36)</b></strong> Difference between select_related and prefetch_related?,

The main difference between select_related and prefetch_related in Django is how they handle database queries 
and data retrieval when working with related objects.

:blue_book: <strong><b>37)</b></strong> Explain Q objects in Django ORM?

In Django's ORM (Object-Relational Mapping), Q objects provide a powerful way to construct complex queries using logical 
operators. Q objects allow you to combine multiple conditions using logical operators such as AND, OR, and
NOT to create dynamic and flexible queries.

:blue_book: <strong><b>38)</b></strong> What are Django exceptions?


In Django, exceptions are predefined error classes that are raised when certain exceptional 
conditions occur during the execution of your application. 
These exceptions are part of Django's exception hierarchy and provide a standardized way
to handle and manage errors in your Django projects. 