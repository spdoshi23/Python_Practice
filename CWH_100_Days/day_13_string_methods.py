# Python provides a set of built-in methods that we can use to alter and modify the strings.
# STRINGS ARE IMMUTABLE in Python, which means that we cannot change the original string. However, we can create a new string based on the original string using these methods.

# upper() : This method converts all the characters in the string to uppercase.
str1 = "AbcDeFg"
print(str1.upper())      #output=ABCDEFG

# lower() : This method converts all the characters in the string to lowercase.
str2 = "AbcDeFg"
print(str2.lower())      #output=abcdefg

# rstrip() : This method removes any trailing characters (characters at the end of a string).
#  space is the default trailing character to remove.
# only trailing characters are removed, leading characters are left untouched.
str3 = "Hello!!!"
print(str3.rstrip("!"))    #output=Hello

#upper() and lower() dont have any arguments, but rstrip() can take an argument to specify which trailing characters to remove. If no argument is provided, it will remove whitespace by default.

# replace() : This method replaces a specified phrase with another specified phrase.
str4 = "Silver Spoon"
print(str4.replace("Sp", "M"))   #output=Silver Moon

# split() : This method splits the string into a list where each word is a list item.
#  The split() method splits the string at the specified separator. If no separator is specified, it splits at whitespace by default.
str5 = "Silver-Spoon"
print(str5.split("-"))  #output=['Silver', 'Spoon']
# also there should be space in argument of split() method if splitting by space, otherwise it will give error.

# capitalize() : This method converts the first character of the string to uppercase and the rest to lowercase. the capitalize() method does not take any arguments. 
# the strring has no effect if the first character is already uppercase.
str6 = "hello worLD"
print(str6.capitalize())   #output=Hello world

# center() : This method returns a centered string of a specified length.
#  The center() method takes two arguments: the width of the string and an optional fill character (default is space).
str7 = "Welcome to the Console!!!"
print(str7.center(50, "*"))   #output=********Welcome to the Console!!!********
# The first argument must be an integer (without double quotes), and the second argument must be a string of length 1. If the second argument is not provided, it will default to a space character.
print(len(str7.center(50, "*")))   #output=50

# count() : This method returns the number of occurrences of a specified value in a string.
#  The count() method takes one argument, which is the sub-string to search for. It returns an integer representing the number of times the sub-string appears in the string.
str8 = "Abracadabra"
print(str8.count("a"))  #output=4"
print(str8.count("A"))  #output=1

# endswith() :The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str9 = "Welcome to the Console!!!" 
print(str9.endswith("!!!"))   #output=True
# We can even also check for a value in-between the string by providing start and end index positions.
str9 = "Welcome to the Console!!!"
print(str9.endswith("to", 4, 10))   #output=True     this shows that the string ends with "to" between index 4 and 10.

# find() : This method searches the string for a specified value and returns the position of where it was found.
#  If the value is not found, it returns -1.
str10 = "He's name is Dan. He is an honest man."
print(str10.find("is"))  #output=10th index
print(str10.find("ishh"))  #output=-1   because "ishh" is not present in the string.
# As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

# index() : This method is similar to the find() method, but it raises a ValueError if the specified value is not found.
str10 = "He's name is Dan. He is an honest man."
print(str10.index("is"))  #output=10th index
# print(str10.index("ishh"))  #output=ValueError: substring not found   because "ishh" is not present in the string.           this will show an error if we uncomment it.because "ishh" is not present in the string.
# As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

# isalnum() : This method checks if all the characters in the string are alphanumeric (either alphabets or numbers). 
# It returns True if all characters are alphanumeric, otherwise it returns False.
str11 = "WelcomeToTheConsole"
print(str11.isalnum())    #output=True

# isalpha() : This method checks if all the characters in the string are alphabetic (only letters).?
str12 = "Welcome"
print(str12.isalpha())    #output=True
str13 = "Welcome123"
print(str13.isalpha())    #output=False   because it contains numbers as well.

# islower() : This method checks if all the characters in the string are lowercase. It returns True if all characters are lowercase, otherwise it returns False.
str14 = "welcome"
print(str14.islower())    #output=True
str15 = "Welcome"
print(str15.islower())    #output=False

# isprintable() : This method checks if all the characters in the string are printable. It returns True if all characters are printable, otherwise it returns False.
str16 = "We wish you a Merry Christmas"
print(str16.isprintable())  #output=True
# characters like \n, \t, etc. are not printable characters.

# isspace() : This method checks if all the characters in the string are whitespace characters. It returns True if all characters are whitespace, otherwise it returns False.
str17 = "        "       #using Spacebar
print(str17.isspace())   #output=True
str18 = "        "       #using Tab
print(str18.isspace())   #output=True

# istitle() : The istitle() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str19 = "Hello, How Are You?"
print(str19.istitle())   #output=True
str20 = "Hello, how are you?"
print(str20.istitle())   #output=False

# isupper() : This method checks if all the characters in the string are uppercase. It returns True if all characters are uppercase, otherwise it returns False.
str21 = "WELCOME"
print(str21.isupper())   #output=True

# startswith() : This method checks if the string starts with a given value. If yes then return True, else return False.
str22 = "Python is a Interpreted Language" 
print(str22.startswith("Python"))   #output=True
str23 = "my name is shubham"
print(str23.startswith("is"))   #output=false

# swapcase() : This method converts all uppercase characters to lowercase and all lowercase characters to uppercase.
str24 = "Hello, How Are You?"
print(str24.swapcase())   #output=hELLO, hOW aRE yOU?

# title() : This method converts the first character of each word to uppercase and the rest to lowercase. The title() method does not take any arguments.
str25 = "He's name is Dan. Dan is an honest man."
print(str25.title())    #output=He'S Name Is Dan. Dan Is An Honest Man.




