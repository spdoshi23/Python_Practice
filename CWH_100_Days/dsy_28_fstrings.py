# String formatting in python
# String formatting can be done in python using the format method.

#string formatting eg:
letter = ("Hey my name is {} and i am from {}")
country = "India"
name = "Shubham"
print(letter.format(name, country))             #by doing this, 'name' variable will go in first{} and 'country' variable will go in second{}
# output = Hey my name is Shubham and i am from India

letter = ("Hey my name is {1} and i am from {0}")            #since we changed place of country and name, to get desired output we have to specify indices of arguments
print(letter.format(country, name))

txt = "For only {price:.2f} dollars!"                               #.2f means it'll take only 2 decimal places
print(txt.format(price = 49.989999))                                #For only 49.00 dollars!


# f-strings:
letter = (f"Hey my name is {name} and i am from {country}")  #this directly populates the value of name and country in whichever bracket we give input

# It is a new string formatting mechanism introduced by the PEP 498. 
# It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). 
# The primary focus of this mechanism is to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the f-string itself.
# The f-string can be formatted in much same as the str.format() method. 
# The f-string offers a convenient way to embed Python expression inside string literals for formatting.

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")                  #GeeksforGeeks is a portal for Geeks

name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")     #Hello, My name is Tushar and I'm 23 years old.

# In the above code, we have used the f-string to format the string. 
# It evaluates at runtime; we can put all valid Python expressions in them.

# We can use it in a single statement as well.
print(f"{2 * 30}")                                             #60  
# this will be printed as a string and not an integer

price = 49.989999
txt = f"For only {price:.2f} dollars!"  
print(txt)

# VIMP:  DOUBLE {{}}
# if we use double curly brackets {{}} inside f string then it prints the thing inside inner {} and not what is stored in that variable
print(f"Hello, My name is {{name}} and I'm {{age}} years old.")
# so here, LITERALLY {name} and {age} will be printed, AND NOT WHAT IS STORED INSIDE name & age VARIABLE
# output = Hello, My name is {name} and I'm {age} years old.








