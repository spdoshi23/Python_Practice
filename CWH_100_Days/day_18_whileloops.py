# WHILE LOOP    
# first set a counter variable to a certain value, then check the condition of the while loop.
# while loops execute statements while the condition is True. 
# As soon as the condition becomes False, the interpreter comes out of the while loop.

#initialisation
#while (condition):
    #statements
    #update

# Example:
count = 5
while (count > 0):
  print(count)
  count = count - 1    #output = 5, 4, 3, 2, 1
# Here, the count variable is set to 5 which decrements after each iteration.
#  Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever. IT  WOULD HAVE BEEN AN INFINITE LOOP IF IT WERE x = x+1 instead of x = x-1.

# Else with While Loop
# We can even use the else statement with the while loop.
# what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

x = 5
while x>0:
    print(x)
    x = x - 1
else:
    print("x is no longer greater than 0")   #output = 5, 4, 3, 2, 1, x is no longer greater than 0

i = 0
while i<3:
   print(i)
   i = i + 1

k = int(input("Enter a number: "))           # just to define the variable k before the while loop starts.
while (k<=38):
    k = int(input("Enter a number: "))
    print(k)
# means it will keep taking input from the user until the user enters a number greater than 38.
#  once user enters a number greater than 38, the while loop condition becomes False and the interpreter comes out of the while loop.


# Do-While loop in python:
# do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. 
# It is also known as an exit-controlled loop.

# How to emulate do while loop in python?
# To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.
# The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

# # syntax
# do {
#    #loop body
# }
# while (condition);

# eg:












