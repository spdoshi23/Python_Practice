# strings: anything enclosed between DOUBLE/SINGLE quotes is considered as a string.
# A string is essentially a sequence or array of textual data. 
# Strings are used when working with Unicode characters.
name = "Shubham"
print("Hello,", name)   #output== Hello, Shubham
# Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

# Sometimes,we might need to put quotation marks in between the strings. 
# Example: He said, “I want to eat an apple”.
# To print this statement we will use single quotes for our convenience.
# We can also use escape sequence commands.
print('He said, "I want to eat an apple".')

# MULTILINE STRINGS
# If string has multiple lines, we can create them like this: (IN TRIPLE DOUBLE/SINGLE QUOTES)
apple = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(apple)

# ACCESSING CHARACTERS OF A STRING
# In Python, string is LIKE an array of characters. ARRAY=CORRECTION OF ITEMS
# We can access parts of string by using its index which starts from 0.
# Square brackets can be used to access elements of the string.
# INDEX STARTS FROM 0. eg:
print(name[0])     #will print 1st letter of variable 'name', i.e. 'S'
print(name[1])     #will print 2nd letter of variable 'name', i.e. 'h'
print(name[2])     #will print 3rd letter of variable 'name', i.e. 'u'
print(name[3])     #will print 4th letter of variable 'name', i.e. 'b'
print(name[4])     #will print 5th letter of variable 'name', i.e. 'h'
print(name[5])     #will print 6th letter of variable 'name', i.e. 'a'
print(name[6])     #will print 7th letter of variable 'name', i.e. 'm'
# print(name[7])     #SINCE THERE IS NO 8TH ELEMENT IN VARIABLE'NAME', IT WILL SHOW AN index error

# if we want to do same thing for a bigger string like 'apple', we have to use 'looping through the string concept'

# LOOPING THROUGH THE STRING 
# We can loop through strings using a for loop like this:

for characters in name:    #for is a loop. dont forget to add (:) at last.
    print(characters)      #'CHARACTER' is just a temperory variable name. we can also use 'letters', 'digits', 'mango', as temp. variable.
                           #since they are temp. variable names python doesnt care if it is really a digit or not. output remains same.
for characters in apple:
    print(characters)