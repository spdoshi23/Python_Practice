a = "1"
b = "2"
print(a+b)   #here, output=12 and not '3'. because we have desined a and b as string variables bcz they are in double quotes
# a is a string, b is a string. python doesnt know that 1 and 2 are numbers, as they are defined as strings.
#  so when we do a+b it CONNECTS/JOINS a and b
# but if a and b are not written in double quotes then output will be 3. bcz they were not br=e classified as strings
# eg: 
p = "shubham "  
q = "doshi"
print(p+q)   #output= shubham doshi
print(int(a)+int(b))     #we forcefully converted(typecasted) a and b as integers rather than strings


# TYPECASTING
# conversion of one data type into the other data type is known as type casting in python or type conversion in python.
# Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc.
#  for the type casting in python.

# there are 2 types of type casting
# 1. Explicit typecasting:  The conversion of one data type into another data type, done by developer or programmer manually.
#                          It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .
# Example of explicit typecasting:
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
#output= The Sum of both the numbers is:  22

# 2.Implicit type casting:Data types in Python do not have the same level i.e. ordering of data types is not the same in Python.
#                              Some of the data types have higher-order, and some have lower order.
#                              While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type
#                              According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.
# Python converts a smaller data type to a higher data type to prevent data loss.
# eg:
 # Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
# output= <class 'int'>
#         <class 'float'>
#         10.0
#         <class 'float'>

c = 1.9
d = 7          #convertef implicitly to float by python interpretor
print(c+d)     #output= 8.9 (float)
