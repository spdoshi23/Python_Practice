# Function Arguments and return statement:
# There are four types of arguments that we can provide in a function:
#1. Default Arguments
#2. Keyword Arguments
#3. Variable length Arguments
#4. Required Arguments

# Default arguments:
# We can provide a default value while creating a function. 
# This way the function assumes a default value even if a value is not provided in the function call for that argument.
# eg:
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")           #output = Hello, Amy John Wharton
# here we only gave fname value. and mname and lnaame took default values feom abocve...

# Keyword arguments:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. 
# Hence, the the order in which the arguments are passed does not matter.
# eg:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")            #output = Hello, Jade Peter Wesker
# here, we can change order of arguments as we recognise it by parameter.

# Required arguments:
# In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.
# eg like in line 12 IT IS COMPULSARY FOR US TO GIVE VALUE OF fname, that is called required argument. mname and lname are optional.

# Example 1:
#  when number of arguments passed does not match to the actual function definition
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")        
# name("Peter", "Quill")\
# TypeError: name() missing 1 required positional argument: 'lname'

# Example 2: when number of arguments passed matches to the actual function definition
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")             #Hello, Peter Ego Quill

# Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function.
#  This can be done using variable-length arguments.

# There are two ways to achieve this:

# Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function.
#  The function accesses the arguments by processing them in the form of TUPLE

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")                      #output = Hello, James Buchanan Barnes

def average(*numbers):
    print(type(numbers))                                   #it'll take numbers as a tuple bcz of (*)  
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum / len(numbers))
average(6, 7, 8, 9)

# Keyword Arbitrary Arguments:
# While creating a function, pass a ** before the parameter name while defining the function.
#  The function accesses the arguments by processing them in the form of DICTIONARY.

def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")                 #Hello, James Buchanan Barnes


# Return Statement:

# The return statement is used to return the value of the expression back to the calling function.
# for eg, on line 62
# we can return sum / len(numbers) rather than printing it.
#  and then store it in some variable 'c = average(a,b,c,d)' and then print c

# IF WE APPLY n RETURN STATEMENTS THEN FIRST STATEMENT IS CONSIDERED AND RETURNED

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))                    #Hello, James Buchanan Barnes















