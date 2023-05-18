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


:blue_book: <strong><b>62)</b></strong> What are the steps to create 1D, 2D and 3D arrays?

:blue_book: <strong><b>63)</b></strong> You are given a numpy array and a new column as inputs. How will you delete the second column and replace the column with a new column value?

:blue_book: <strong><b>64)</b></strong> How will you efficiently load data from a text file?

:blue_book: <strong><b>65)</b></strong> How will you read CSV data into an array in NumPy?

:blue_book: <strong><b>66)</b></strong> How will you sort the array based on the Nth column?

:blue_book: <strong><b>67)</b></strong> How will you find the nearest value in a given numpy array?

:blue_book: <strong><b>68)</b></strong> How will you reverse the numpy array using one line of code?

:blue_book: <strong><b>69)</b></strong> How will you find the shape of any given NumPy array?

:blue_book: <strong><b>70)</b></strong> Differentiate between a package and a module in python.

:blue_book: <strong><b>71)</b></strong> What are some of the most commonly used built-in modules in Python?

:blue_book: <strong><b>72)</b></strong> What are lambda functions?

:blue_book: <strong><b>73)</b></strong> How can you generate random numbers?

:blue_book: <strong><b>74)</b></strong> Can you easily check if all characters in the given string is alphanumeric?

:blue_book: <strong><b>75)</b></strong> What are the differences between pickling and unpickling?

:blue_book: <strong><b>76)</b></strong> Define GIL.

:blue_book: <strong><b>77)</b></strong> Define PYTHONPATH.

:blue_book: <strong><b>78)</b></strong> Define PIP.

:blue_book: <strong><b>79)</b></strong> Are there any tools for identifying bugs and performing static analysis in python?

:blue_book: <strong><b>80)</b></strong> Differentiate between deep and shallow copies.

:blue_book: <strong><b>81)</b></strong> What is main function in python? How do you invoke it?

:blue_book: <strong><b>82)</b></strong> Write python function which takes a variable number of arguments.

:blue_book: <strong><b>83)</b></strong> WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.

:blue_book: <strong><b>84)</b></strong> Write a program for counting the number of every character of a given text file.

:blue_book: <strong><b>85)</b></strong> Write a program to check and return the pairs of a given array A whose sum value is equal to a target value N.

:blue_book: <strong><b>86)</b></strong> Write a Program to add two integers >0 without using the plus operator.

:blue_book: <strong><b>87)</b></strong> Write a Program to solve the given equation assuming that a,b,c,m,n,o are constants:

:blue_book: <strong><b>88)</b></strong> Write a Program to match a string that has the letter ‘a’ followed by 4 to 8 'b’s.

:blue_book: <strong><b>89)</b></strong> Write a Program to convert date from yyyy-mm-dd format to dd-mm-yyyy format.

:blue_book: <strong><b>90)</b></strong> Write a Program to combine two different dictionaries. While combining, if you find the same keys, you can add the values of these same keys. Output the new dictionary

:blue_book: <strong><b>91)</b></strong> How will you access the dataset of a publicly shared spreadsheet in CSV format stored in Google Drive?

# :speaking_head: Part II - Django 

:blue_book: <strong><b>1)</b></strong> Explain Django Architecture?

:blue_book: <strong><b>2)</b></strong> Explain the django project directory structure?

:blue_book: <strong><b>3)</b></strong> What are models in Django?

:blue_book: <strong><b>4)</b></strong> What are templates in Django or Django template language?

:blue_book: <strong><b>5)</b></strong> What are views in Django?

:blue_book: <strong><b>6)</b></strong> What is Django ORM?

:blue_book: <strong><b>7)</b></strong> Define static files and explain their uses?

:blue_book: <strong><b>8)</b></strong> What is Django Rest Framework(DRF)?

:blue_book: <strong><b>9)</b></strong> What is django-admin and manage.py and explain its commands?

:blue_book: <strong><b>10)</b></strong> What is Jinja templating?

:blue_book: <strong><b>11)</b></strong> What are Django URLs?

:blue_book: <strong><b>12)</b></strong> What is the difference between a project and an app in Django?

:blue_book: <strong><b>13)</b></strong> What are different model inheritance styles in the Django?

:blue_book: <strong><b>14)</b></strong> What are Django Signals?

:blue_book: <strong><b>15)</b></strong> Explain the caching strategies in the Django?

:blue_book: <strong><b>16)</b></strong> Explain user authentication in Django?

:blue_book: <strong><b>17)</b></strong> How to configure static files?

:blue_book: <strong><b>18)</b></strong> Explain Django Response lifecycle?

:blue_book: <strong><b>19)</b></strong> What databases are supported by Django?

:blue_book: <strong><b>20)</b></strong> What's the use of a session framework?

:blue_book: <strong><b>21)</b></strong> What’s the use of Middleware in Django?

:blue_book: <strong><b>22)</b></strong> What is context in the Django?

:blue_book: <strong><b>23)</b></strong> What is django.shortcuts.render function?

:blue_book: <strong><b>24)</b></strong> What’s the significance of the settings.py file?

:blue_book: <strong><b>25)</b></strong> How to view all items in the Model?

:blue_book: <strong><b>26)</b></strong> How to filter items in the Model?

:blue_book: <strong><b>27)</b></strong> How to use file-based sessions?

:blue_book: <strong><b>28)</b></strong> What is mixin?

:blue_book: <strong><b>29)</b></strong> What is Django Field Class?

:blue_book: <strong><b>30)</b></strong> Why is permanent redirection not a good option?

:blue_book: <strong><b>31)</b></strong> Difference between Django OneToOneField and ForeignKey Field?

:blue_book: <strong><b>32)</b></strong> How can you combine multiple QuerySets in a View?

:blue_book: <strong><b>33)</b></strong> How to get a particular item in the Model?

:blue_book: <strong><b>34)</b></strong> How to obtain the SQL query from the queryset?

:blue_book: <strong><b>35)</b></strong> What are the ways to customize the functionality of the Django admin interface?

:blue_book: <strong><b>36)</b></strong> Difference between select_related and prefetch_related?

:blue_book: <strong><b>37)</b></strong> Explain Q objects in Django ORM?

:blue_book: <strong><b>38)</b></strong> What are Django exceptions?
