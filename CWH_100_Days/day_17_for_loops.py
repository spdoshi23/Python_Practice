# Introduction to Loops:
# Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops.
#  Based on this loops are further classified into following main types;
# 1. For Loop 
# 2. While Loop

# FOR LOOP:
# for loops can iterate over a sequence of iterable objects in python.
#  Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

# eg, to print from 1 to 20000 using print statement is very time consuming and not a good practice.
#  Instead we can use for loop to print from 1 to 20000 in a very efficient way.

# we can loop string, list, tuple, set and dictionary using for loop in python.

# example of iteration of string:
name = "Abhishek"
for x in name:
    print(x)           # prints each character of the string
    if x == "h":
        print("h for house")  # prints "h for house" when x is equal to "h"

# eg of iteration of list:
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)           # prints each color in the list
    if color == "blue":
        print("blue for sky")  # prints "blue for sky" when color is equal to "blue"


# using for loop inside for loop:
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)           #now color is a string and we can iterate over it using for loop
    for i in color:
        print(i)           # prints each character of the color string

#INNER LOOP RUNS COMPLETELY FOR EACH ITERATION OF OUTER LOOP. 
# SO OUTPUT IS AS red, r, e, d,green, g, r, e, e, n, blue, b, l, u, e, yellow, y, e, l, l, o, w

# range():
# it is used to use for loop to iterate over a sequence of numbers. 
# It generates a sequence of numbers starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# eg?:
for k in range(5):
    print(k)           # prints 0, 1, 2, 3, 4
# Here, we can see that the loop starts from 0 by default and increments at each iteration.

# the range() function can also take two arguments, the starting and ending values. The loop will start from the starting value and stop before the ending value.
for k in range(5):
    print(k+1)         # prints 1, 2, 3, 4, 5
                #OR
for k in range(1,6):
    print(k)           # prints 1, 2, 3, 4, 5

# But we can also loop over a specific range.
for k in range(4,9):
    print(k)           # prints 4, 5, 6, 7, 8

# to print from 1 to 100 using for loop and range() function:
for k in range(1,101):
    print(k)           # prints 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,

# INSHORT range(x,y) will generate a sequence of numbers starting from x and ending at y-1. It will not include y in the sequence.
# AND range(z) will generate a sequence of numbers starting from 0 and ending at z-1. It will not include z in the sequence.

# IF WE INCLUDE 3 VALUES IN range() FUNCTION, THEN THE THIRD VALUE WILL BE CONSIDERED AS STEP VALUE.
#  IT WILL INCREMENT THE VALUE OF i BY STEP VALUE AT EACH ITERATION.

for k in  range(1, 12, 2):  # here 1 is starting value, 12 is ending value and 2 is step value.
    print(k)           # prints 1, 3, 5, 7, 9, 11
for k in  range(1, 12, 3):  # here 1 is starting value, 12 is ending value and 3 is step value.
    print(k)           # prints 1, 4, 7, 10

# 3 FORMS OF range() FUNCTION:
# 1. range(stop) - Generates numbers from 0 to stop-1
for x in range(5):
    print(x)           # prints 0, 1, 2, 3, 4

# 2. range(start, stop) - Generates numbers from start to stop-1
for x in range(1, 6):
    print(x)           # prints 1, 2, 3, 4, 5

# 3. range(start, stop, step) - Generates numbers from start to stop-1 with a step value of step
for x in range(1, 12, 2):
    print(x)           # prints 1, 3, 5, 7, 9, 11



