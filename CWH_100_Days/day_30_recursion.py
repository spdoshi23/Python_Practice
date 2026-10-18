# Recursion in python:
# Recursion is the process of defining something in terms of itself.

# Python Recursive Function
# In Python, we know that a function can call other functions. 
# It is even possible for the function to call itself. These types of construct are termed as recursive functions.

# Example:
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
# Driver Code 
num = 7
print("Number: ",num)
print("Factorial: ",factorial(num))
# Output:
# number:  7
# Factorial:  5040

print(factorial(7))
# 7*factorial(6)
# 7*6*factorial(5)
# 7*6*5*factorial(4)
# 7*6*5*4*factorial(3)
# 7*6*5*4*3*factorial(2)
# 7*6*5*4*3*2*factorial(1)
# 7*6*5*4*3*2*1

# FIBONACCI SEQUENCE:
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

def fibonacci_terms(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_terms(n - 1) + fibonacci_terms(n - 2)

def print_series(n):
    if n == 0:
        return
    print_series(n - 1)
    print(fibonacci_terms(n))

print_series(7)

# Base case: Stops recursion.
# Recursive call: The function calls itself.
# Call stack: Statements after a recursive call execute when that call returns

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Definition: Recursion is a programming technique in which a function calls itself to solve a problem.
def number(n):
    if n == 0:
        return

    print(n)
    number(n - 1)

number(5)

# output:
# 5
# 4
# 3
# 2
# 1

# number(n - 1) ---------- Call the same function again, but give it a smaller value of n
# number(5)---------------The function receives n = 5. It prints 5 and calls number(4). The new function call receives n = 4. It prints 4 and calls number(3). This continues until n reaches 0.
# base case---------------The function prints 5, then 4, then 3, and continues. Eventually, it reaches negative numbers. It never stops calling itself. Eventually, Python raises a RecursionError because the recursion becomes too deep.
# if n == 0:--------------this is base case
    # return


# | Term           | Meaning                            |
# | -------------- | ---------------------------------- |
# | Base case      | The condition that stops recursion |
# | Recursive call | A function calling itself          |




def number(n):
    if n == 0:
        return

    print(n)
    number(n - 1)
    print(n)

number(3)
# When Python encounters number(n - 1), it DOESN'T forget about the remaining print(n) statement
# Python pauses the current function call while the new call executes
# Once the new call finishes, Python resumes the previous call and continues executing the remaining statements.
# hence, it si printen=d in reverse direction

def number(n):
    if n == 0:
        return

    print("Going down:", n)
    number(n - 1)
    print("Coming up:", n)

number(2)

# Going down: 2
# Going down: 1
# Coming up: 1
# Coming up: 2


# THE GOLDEN RULE:
# Statements before the recursive call execute as the function goes deeper. Statements after the recursive call execute as the function returns.
# This isn't a special rule exclusive to recursion. It's how normal function execution works, combined with nested function calls.


# CALL STACK:
# Python pauses one function call and executes another, But how does it remember where to resume?
# Python maintains a structure called the call stack.
# Every time a function is called, Python keeps track of that call's information, including its local variables and where execution should continue.






































