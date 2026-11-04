# Enumerate function in python:
# The enumerate function is a built-in function in Python that allows to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. 

# METHOD-1
index = 0
marks = [12, 56, 32, 98, 45, 1, 4]
for mark in marks:
    print(mark)
    if index == 3:
        print("Shubham, awesome!")
    index += 1
print("\n\n")
# METHOD-2
marks = [12, 56, 32, 98, 45, 1, 4]
for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Shubham, awesome!")

print("\n\n")

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
# output:
# 0 apple
# 1 banana
# 2 mango
# the enumerate function returns a tuple containing the index and value of each element in the sequence. 
# You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.


# Changing the start index
# By default, the enumerate function starts the index at 0, but we can specify a different starting index by passing it as an argument to the enumerate function:

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# output:
# 1 apple
# 2 banana
# 3 mango

# The enumerate function is often used when we need to loop over a sequence and perform some action with both the index and value of each element. 
# For example, we might use it to loop over a list of strings and print the index and value of each string in a formatted way:

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')
# output:
# 1: apple
# 2: banana
# 3: mango

# In addition to lists, we can use the enumerate function with any other sequence type in Python, such as tuples and strings. 
# Here's an example with a tuple

# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)
# output
# 0 red
# 1 green
# 2 blue

# example with a string:
# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)
# output
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o

