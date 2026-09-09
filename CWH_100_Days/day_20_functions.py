# Python Functions
# A function is a block of code that performs a specific task whenever it is called.
#  In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.
# There are two types of functions:

# 1. Built-in functions
# 2. User-defined functions

# Built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# User-defined functions:
 #syntax
def function_name(parameters):       
  pass
  # Code and Statements

# 1. Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
# 2. Any parameters and arguments should be placed within the parentheses.
# 3. Rules to naming function are similar to that of naming variables.
# 4. Any statements and other code within the function should be indented.


# Calling a function:
# We call a function by giving the function name, followed by parameters (if any) in the parenthesis.
def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")

# We can create functions to perform specific tasks as per our needs. 

# consider we wanna calc the HM of 2 nos.
a = 9
b = 8
hmean1 = (a*b)/(a+b)
print(hmean1)

# if we wanna do same process again then we'll have to write same code again
c = 8
d = 7
hmean2 = (c*d)/(c+d)
print(hmean2)

# similiarly, if we have to calc more HMs then we'd have to define code lot of times.
#  to save time and make code less big we can define function using def( ) function.
# eg:

def calculateHmean(a, b):               #a, b are arguments. calculateHmean is name of function.
    hmean = (a*b)/(a+b)
    print(hmean)

def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a, b):
    pass               #pass means we can write function body later. it'll not give an error.
                       #if we don't write pass then it'll give indent error
e = 4
f = 4
calculateHmean(e, f)
isGreater(e, f)

g = 8
h = 6
calculateHmean(g, h)
isGreater(g, h)




















